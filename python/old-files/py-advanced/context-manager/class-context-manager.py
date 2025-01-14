class FileHandler: 
        '''
        FileHandler behaves as a context manager 
        '''
        def __init__(self, filename, mode) -> None:
                self.filename = filename
                self.mode = mode 
        
        def __enter__(self): 
                self.file = open(self.filename, self.mode)
                return self.file 

        def __exit__(self, exe_type, exc_val, traceback): 
                self.file.close()


with FileHandler('new.txt', 'w') as file: 
        file.write('today is friday')

with FileHandler('new.txt', 'r') as file: 
        print(file.read())
        

print('is FileHandler closed: ', file.closed)
