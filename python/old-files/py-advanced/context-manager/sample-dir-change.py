import os 

# cwd: current working directory 

def to_dummy_dir_1(): 
        main_cwd = os.getcwd()
        print()
        print('parent dir: ', main_cwd)
        
        os.chdir('dummy-dir-1')
        print(os.listdir())
        cwd = os.getcwd()
        print('after changing cwd: ', cwd)
        
        os.chdir(main_cwd)
        cwd = os.getcwd()
        print('after dir change back to parent: ', cwd)
        

to_dummy_dir_1()
