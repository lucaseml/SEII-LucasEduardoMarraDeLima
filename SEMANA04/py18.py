#Lucas Eduardo Marra de Lima

import builtins

print(dir(builtins))
m = min([5,1.4,2,3])
print(m)

def test(z):
    x = 'local x'
    print(z)

test('local z')

x = 'global x'

def outer():
    x = 'outer x'

    def inner ():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()

print(x)