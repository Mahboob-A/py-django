import os 

from contextlib import contextmanager


@contextmanager
def dir_handler(dest_dir): 
        try:
                # save the current dir 
                parent_cwd  = os.getcwd()
                
                # change the dir to the destination 
                os.chdir(dest_dir)
                yield
        finally:
                # back to the main/parent dir
                os.chdir(parent_cwd)


with dir_handler('dummy-dir-2'): 
        print(os.listdir())
        os.mkdir('new-dir')
        # still on the dest_dir directory 
        print(os.getcwd())



# out of context manager. dir changed as per parent dir for finally block. 
print(os.getcwd())


