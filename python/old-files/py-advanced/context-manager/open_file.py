

f = open('dummy.txt', 'r')
print(f.read())
f.close()


# context manager 
with open('dummy.txt', 'r') as f: 
        print(f.read())
        