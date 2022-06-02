#Lucas Eduardo Marra de Lima

import numpy as np

a1 = np.array([2, 4, 5, 6, 10])
print(a1)
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1>3)
print(a1[a1>3])

print('\n')

names = np.array(['Jin', 'Luke', 'Josh', 'Pete'])
print(names)

f = lambda s: s[0]
print(f('animal'))

print('\n')

fist_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
vectorized = np.vectorize(lambda s: s[0])(names)
print(vectorized)
print(fist_letter_j)
print(names[fist_letter_j])

print('\n')

print(a1)
print(a1%4)
print(a1%4 == 0)
print(a1[a1%4 == 0])