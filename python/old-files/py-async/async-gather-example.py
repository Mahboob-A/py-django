"""
220324, Friday, 04.45 pm, 11th Roja
"""

import asyncio
from time import sleep, time 




'''
packages:  aiofiles - for async file handling 
- aiohttp - for async http 
'''


# an example of asyncio gather

start = time()

async def open_file(): 
        print('Opening a file...')
        await asyncio.sleep(3)
        print('File open completed.')


async def main(): 
        print('Main co-routine started...')
        await asyncio.gather(
                open_file(), 
                open_file(), 
                open_file(), 
                open_file(), 
                open_file()
        )
        print('Mainco-routine completed.')


asyncio.run(main())

end = time()

print('Execution time: ', end-start)
