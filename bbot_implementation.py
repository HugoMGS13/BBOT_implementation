from bbot.scanner import Scanner, Preset
async def main():
    scan = Scanner(
        'prodepa.pa.gov.br',
        preset=Preset.from_yaml_file(
            #"/home/sec/Documentos/ImpBBOT/BBOT_implementation/scan_domain.yml"
            "/home/teste/Documentos/BBOT_implementation/presets/scan_dataleak.yml"
        )
    )
    async for event in scan.async_start():
        print(event.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())