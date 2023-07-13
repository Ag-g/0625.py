import asyncio, aiohttp
urls = [
    "url1", "url2", "url3"
]

# s = aiohttp.ClientSession()  # 等价于requests
async def single(url):
    async with aiohttp.ClientSession() as session:
        # session.get()
        # session.post()
        async with session.get(url) as resp:
            # resp.content.read
            # resp.text()
            # resp.json()
            with open("xxxx") as f:
                f.write(await resp.content.read())


