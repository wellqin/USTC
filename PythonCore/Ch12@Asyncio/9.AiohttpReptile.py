# -*- coding: utf-8 -*-
"""
-------------------------------------------------
File Name:        9.AiohttpReptile
Description :   
Author :          wellqin
date:             2020/4/21
Change Activity:  2020/4/21
-------------------------------------------------
"""

# asyncio去重url，入库（异步的驱动aiomysql）
import aiohttp  # aiohttp requires Python '>=3.5.3' but the running Python is 3.5.2
import asyncio
import re
import aiomysql
from pyquery import pyquery

start_url = 'http://www.jobbole.com/'
waiting_urls = []
seen_urls = []
stopping = False
# 限制并发数
sem = asyncio.Semaphore(3)


async def fetch(url, session):
    async with sem:
        await asyncio.sleep(1)
        try:
            async with session.get(url) as resp:
                print('url_status:{}'.format(resp.status))
                if resp.status in [200, 201]:
                    data = await resp.text()
                    return data
        except Exception as e:
            print(e)


def extract_urls(html):
    """
    解析无io操作
    """
    urls = []
    pq = pyquery(html)
    for link in pq.items('a'):
        url = link.attr('href')
        if url and url.startwith('http') and url not in urls:
            urls.append(url)
            waiting_urls.append(url)
    return urls


async def init_urls(url, session):
    html = await fetch(url, session)
    seen_urls.add(url)
    extract_urls(html)


async def handle_article(url, session, pool):
    """
    处理文章
    """
    html = await fetch(url, session)
    seen_urls.append(url)
    extract_urls(html)
    pq = pyquery(html)
    title = pq('title').text()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into Test(title) values('{}')".format(title)
            await cur.execute(insert_sql)


async def consumer(pool):
    with aiohttp.CLientSession() as session:
        while not stopping:
            if len(waiting_urls) == 0:
                await asyncio.sleep(0.5)
                continue
            url = waiting_urls.pop()
            print('start url:' + 'url')
            if re.match('http://.*?jobble.com/\d+/', url):
                if url not in seen_urls:
                    asyncio.ensure_future(handle_article(url, session, pool))
                    await asyncio.sleep(30)
            else:
                if url not in seen_urls:
                    asyncio.ensure_future(init_urls(url, session))


async def main():
    # 等待mysql连接好
    pool = aiomysql.connect(host='localhost', port=3306, user='root',
                            password='112358', db='my_aio', loop=loop, charset='utf8', autocommit=True)
    async with aiohttp.CLientSession() as session:
        html = await fetch(start_url, session)
        seen_urls.add(start_url)
        extract_urls(html)
    asyncio.ensure_future(consumer(pool))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(loop)
    loop.run_forever(main(loop))
