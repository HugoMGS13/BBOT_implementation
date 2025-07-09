from bbot.scanner import Scanner, Preset
async def main():
    scan = Scanner('app1.evilcorp.com', 'app2.evilcorp.com', 'app3.evilcorp.com', preset=Preset.from_yaml_file("/home/teste/Documentos/bbot_cru/scan_vuln.yml"))
    async for event in scan.async_start():
        print(event.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())