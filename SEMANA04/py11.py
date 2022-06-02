#Lucas Eduardo Marra de Lima

f = open('test.txt', 'r')
print(f.mode)
print(f.name)
f.close()

print(f.name)
print(f.mode)


with open('test.txt', 'r') as f:
    print(f.mode)
    print(f.name)
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents, end = '')
    f_contents = f.readline()
    print(f_contents, end = '')


print('')
print('')   


with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('test.txt', 'r') as rf:
    with open('test3.txt', 'w') as wf:
        for line in rf:
            wf.write(line)