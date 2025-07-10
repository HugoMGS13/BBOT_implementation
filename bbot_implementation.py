from bbot.scanner import Scanner, Preset
async def main():
    scan = Scanner(
        'target',
        preset=Preset.from_yaml_file(
            "caminho"
        )
    )
    async for event in scan.async_start():
        print(event.json())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())