#Lucas Eduardo Marra de Lima

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print("\n")

print(student['name'])
print(student.get('name'))
print(student.get('phone', 'Not found'))

print("\n")

student['phone'] = '555-5555'
student['name'] = 'Jane'

print(student)

print("\n")

student.update({'name': 'Jack', 'phone': '333-3333'})

print(student)

print("\n")

age = student.pop('age')

print(age)
print(student)

print("\n")

print(len(student))
print(student.keys())
print(student.items())

print("\n")

for key, value in student.items():
    print(key, value)