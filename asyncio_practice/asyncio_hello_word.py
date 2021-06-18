import asyncio
from logging import log
from asyncio_practice.setup_logger import logger

async def hello():
    while True:
        logger.debug('hello')
        await asyncio.sleep(1)

async def world():
    while True:
        logger.debug('world')
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(hello())
    task2 = asyncio.create_task(world())
    logger.info(f'hello() is : {type(hello())}')
    logger.info(f'task1 is : {type(task1)}')
    
    
    await task1
    await task2
try:
    asyncio.run(main())
except KeyboardInterrupt as ki:
    logger.info('End Process')