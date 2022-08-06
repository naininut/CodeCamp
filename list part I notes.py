# lists
x = [1, 2, 3]

# print list
x = [5, 7, 8]
print(x)

# syntax
# [_, _, __, __]

# length
x = [5, 7, 8]
print(len(x))

print(len([8, 9]))

# empty list
x = []
print(x)

print(len(x))

# read a list from a user
a = list(map(int, input().split()))
print(a)
# print elements of a list in one line
a = [1, 3, 2]
print(*a)

# get an element of a list
# 5 7 8
# 0 1 2

x = [5, 7, 8]
print(x[0])
print(x[1])

# change elements
x = [5, 7, 8]
x[1] = 10
print(*x)

# syntax
# name[number] = __

# append
a = [1, 3, 2]
a.append(10)
print(*a)
a.append(1)
print(*a)

# remove elements
a = [1, 3, 2]
a.pop(2)
print(*a)

a = [1, 3, 2, 1]
a.pop(1)
print(*a)

a = [1, 2, 3, 4, 5]
a.pop(1)
a.pop(2)
print(*a)


# print elements on separate lines
x = [2, 3, 4]
for i in range(len(x)):
    print(x[i])

# syntax
# for i in range(len(name)):
#     ___

x = [2, 3, 4]
for i in range(len(x)):
    print(x[i])