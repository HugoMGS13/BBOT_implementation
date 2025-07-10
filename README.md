# Implementação do BBOT
Implementei o BBOT como uma biblioteca do python seguinda a sua documentação oficial.
Foram criados 3 presets por mim: scan de vulnerabilidades, scan de exploração de domínios e scan de vazamentos de dados (!)
O scan de vazamento de dados me retorna um arquivo csv com todos os emails e senhas vazadas de determinado domínio.
O arquivo fp_filter_dataleak.py automatiza a verificação de falsos-positivos, logando com todos os logins fornecidos pelo scan.

!!!---ESSA AUTOMATIZAÇÃO ESTÁ EM TESTES---!!!

Use em ambientes controlados para evitar bloqueios.
