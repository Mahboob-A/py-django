'''
220324, Friday, 04.00 pm, 11th Roja
'''

import threading 
import multiprocessing
from time import sleep

def print_infinite():
    while 1:
        sleep(1)
        print("pringting infinitely!")


def print_name(): 
        print('my name is thread')




def without_thread(): 
        print_infinite()
        print_name()

def with_thread(): 
        task1 = threading.Thread(target=print_infinite)
        task2 = threading.Thread(target=print_name)
        
        task1.start()
        task2.start()


# with_thread()

# print(multiprocessing.cpu_count())
# print(multiprocessing.current_process())
