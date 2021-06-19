# examples taken from https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc
# %%
import sys
sys.path.append('/Users/jack/Documents/Concurrency')
from asyncio_practice.setup_logger import logger
def gen():
    yield "Hello"
    yield "World"
    return "Hello World"

g = gen()
logger.debug(next(g))
logger.debug(next(g))
logger.debug(next(g)) # this will get StopIteration Exception

try: # this will retrieve the return value
    next(g)
except StopIteration as e:
    logger.debug(e)
# %%
import sys
sys.path.append('/Users/jack/Documents/Concurrency')
from asyncio_practice.setup_logger import logger
def gen():
    logger.debug("Stop while declaring first number")
    a = yield # stop while doing assignment
    logger.debug(f"Already declare the first number  a = {a}")
    logger.debug("Stop while declaring second number")
    b = yield
    logger.debug(f"Already declare the second number  b = {b}")
    logger.debug(f"a + b = {a+b}")
    logger.debug("Stop while declaring third number")
    c = yield
    logger.debug(f"c = {c}")
    return a + b + c

g = gen()
next(g) # trace code until finding 'yield' keyword
g.send(3) # send the value to generator
# g.send(a) # cannot declare using variables in generator, because different call stacks ?
g.send(3)
try:
    g.send(3)
except StopIteration as e:
    logger.debug(f'a + b + c = {e}')
# %% nesting generator
import sys
sys.path.append('/Users/jack/Documents/Concurrency')
from asyncio_practice.setup_logger import logger
def inner():
    inner_result = yield 2
    logger.debug('inner', inner_result)
    return 3

def outer():
    yield 1
    val = yield from inner()
    logger.debug('outer', val)
    yield 4

gen = outer()
logger.debug(next(gen))

logger.debug(next(gen)) # Goes inside inner() automatically
gen.send("abc")
logger.debug(next(gen))
# %%
