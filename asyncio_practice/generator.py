# examples taken from https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc
# %%
def gen():
    yield "Hello"
    yield "World"
    return "Hello World"

g = gen()
print(next(g))
print(next(g))
print(next(g)) # this will get StopIteration Exception

try: # this will retrieve the return value
    next(g)
except StopIteration as e:
    print(e)
# %%
def gen():
    print("First number")
    a = yield
    print("Second number")
    b = yield
    print("Addition result:", a+b)
    c = yield

# def gen():
#     print("First number")
#     a = yield
#     print("Second number")
#     b = yield
#     print("Addition result:", a+b)
#     c = yield