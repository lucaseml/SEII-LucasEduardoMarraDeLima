#Lucas Eduardo Marra de Lima

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[-1:])

print("\n")
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.insert(0, 'Art')

print(courses)

print("\n")
courses.pop()
print(courses)

print("\n")
courses_2 = 'CompSci'
courses.append(courses_2)
print(courses)

print("\n")
nums = [1, 5, 2, 4, 3]

sorted_courses = courses
sorted_courses.sort(reverse=True)
nums.sort(reverse=True)

print(sorted_courses)
print(nums)

print("\n")
nums = [1, 5, 2, 4, 3]

sorted_courses = sorted(courses)

print(sorted_courses)
print(nums)

print("\n")
print(courses.index('Art'))

print("\n")
for item in enumerate(courses):
    print(item)

print("\n")
for index, courses in enumerate(courses):
    print(index, courses)

print("\n")
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)

print(courses_str)

print("\n")
courses = ['History', 'Math', 'Physics', 'CompSci']

courses_str = ', '.join(courses)

new_list = courses_str.split(', ')

print(new_list)

print("\n")

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)



print("\n")

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)


print("\n")

cs_courses = {'History', 'Math', 'Math', 'Physics', 'CompSci'}

print(cs_courses)


print("\n")
print('Math' in cs_courses)


cs_courses = {'History', 'Math', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))