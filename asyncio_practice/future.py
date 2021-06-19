# Examples taken from https://docs.python.org/3/library/asyncio-future.html
# %% 
import asyncio
from asyncio.exceptions import CancelledError
import sys
sys.path.append('/Users/jack/Documents/Concurrency')
from asyncio_practice.setup_logger import logger

async def hello(fut):
    await asyncio.sleep(1)
    
    # Set *value* as a result of *fut* Future.
    fut.set_result('hello')

async def main():
    logger.debug(asyncio.isfuture(hello))
    
    # Get the current event loop
    loop = asyncio.get_running_loop()
    
    # Create a new Future object
    fut = loop.create_future()
    logger.debug(asyncio.isfuture(fut))
    
    task = loop.create_task(hello(fut))
    logger.debug('========== All Tasks ==========')
    for t in asyncio.all_tasks():
        logger.debug(t)
        logger.debug('===============================')
    
    logger.debug(await task) # task return None # block in this line
    
    logger.debug('========== All Tasks ==========')
    for t in asyncio.all_tasks():
        logger.debug(t)
        logger.debug('===============================')
    logger.debug(fut)

# asyncio.run(main()) # Run in python 3.7
await main() # Run in juypter

# %% cancel
import asyncio
from asyncio import CancelledError
import sys
sys.path.append('/Users/jack/Documents/Concurrency')
from asyncio_practice.setup_logger import logger

async def hello(fut):
    logger.debug('========== Waiting for hello ==========')
    await asyncio.sleep(2)
    
    # Set *value* as a result of *fut* Future.
    fut.set_result('hello')

async def cancel_hello(fut):
    logger.debug('========== Waiting for cancel_hello ==========')
    await asyncio.sleep(1)
    
    fut.cancel() # Expect CancelledError
    logger.debug('========== Cancelled hello ==========')

async def main():
    
    # Get the current event loop
    loop = asyncio.get_running_loop()
    
    # Create a new Future object
    hello_fut = loop.create_future()
    hello_task = loop.create_task(hello(hello_fut))
    cancel_task = loop.create_task(cancel_hello(hello_fut))
    
    logger.debug(f'========== {len(asyncio.all_tasks())} Tasks ==========')
    for t in asyncio.all_tasks():
        logger.debug(t)
        logger.debug('===============================')
    
    logger.debug(await hello_fut)

try:
    await main() # Run in juypter
except CancelledError as e:
    logger.error(e)
    logger.error('Future is cancelled before finishing')