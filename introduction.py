''' The coroutines
Note that the term coroutine can refer to either a coroutine function
or a coroutine object, depending on the context.
For the top-level entry point coroutine function, which is normally named as main(),
we need to use asyncio.run() to run it
'''

import asyncio
from datetime import datetime

async def my_coroutine_func():
    ''' This is a coroutine function which returns a coroutine object when called'''
    print('Welcome to the coroutines!')

# my_coroutine_object = my_coroutine_func()
# print(type(my_coroutine_object))

async def main():
    print('entrypoint')
    await my_coroutine_func()

asyncio.run(main())

# def gen_function():
#     yield 'duke lester'

# generator = gen_function()
# print(next(generator))


async def async_sleep(num):
    print(f'Sleeping in {num} seconds!')
    await asyncio.sleep(num)

async def main():
    start = datetime.now()

    for i in range(1, 5):
        await async_sleep(i)

    duration = datetime.now() - start
    print(f'Took {duration.total_seconds():.2f} seconds')

asyncio.run(main())
