import requests
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
async def getNews():
    print(os.getenv("newsdata_api"))

if __name__ == "__main__":
    async def main():
        await getNews()
    asyncio.run(main())
