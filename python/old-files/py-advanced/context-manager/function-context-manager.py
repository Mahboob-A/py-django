from contextlib import contextmanager


# function based context manger
@contextmanager
def file_handler(filename, mode): 
        try: 
                file = open(filename, mode)
                yield file 
        finally: 
                file.close()


with file_handler('new2.txt', 'w') as file: 
        file.write('today is 11th roja, 220324, friday')


with file_handler('new2.txt', 'r') as file:
        print(file.read())


print("is file_handler closed: ", file.closed)
