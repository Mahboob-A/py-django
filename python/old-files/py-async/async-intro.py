"""
220324, Friday, 04.30 pm, 11th Roja
"""

import tracemalloc
import asyncio
from time import sleep, time

"""
In asynchronous programming with asyncio, the await keyword suspends 
the execution of the coroutine until the awaited coroutine completes.

### When To Use Async Programming: 
        - async programming is used in case of "Fire and Forget pattern". 
        - when we want to complete a task without needed the result immediately, 
        - we then "fire" the task, and "forget" about it. 
        
        - Hense, async programming should be applied on fire and forget pattern. 

"""



# a will not complete untill b has been completed in this case.
# async def a():
#         val = await b()  # a will not continue untill b has been completed.
#         print(val)


# async def b():
#         await  asyncio.sleep(20)
#         return 10


# asyncio.run(a())


start = time()


# simple async code
async def a():
        print('in a...\n')
        await asyncio.sleep(8)
        print('a completed...')


async def b():
        print('in b...\n')
        await asyncio.sleep(5)
        print('b completed...')


async def c(): 
        print('in c...\n')
        await asyncio.sleep(3)
        print('c is printing...')


async def main(): 
    task_a = asyncio.create_task(a())
    await b()
    await c()
    await task_a


asyncio.run(main())

end = time()


print('exe time: ', end-start)
