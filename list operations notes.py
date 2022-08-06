# text = ""
# for i in range(3):
#     s = input()
#     text = text + s
# print(text)

# operations with list
# in
x = [1, 2, 3]
if 1 in x:
    print("YES")
if 0 in x:
    print("YES")

res = False
for i in range(len(x)):
    if x[i] == 1:
        res = True
if res:
    print("YES")
    
if 1 in x:
    print("YES")
if 0 in x:
    print("YES")

# count
x = [3, 0, 0]
y = x.count(0)
print(y)

# index()
a = [1, 3, 2]
print(a.index(3))

a = [1, 3, 2, 3]
print(a.index(3))

# a = [1, 3, 2]
# print(a.index(0))

# add lists
a = [1, 3]
b = [2, 0, 1]
print(a + b)

a = [1, 3]
print(a * 3)

a = [0]
print(a * 5)

# max
x = [2, 3, 1]
print(max(x))

# min
x = [2, 3, 1]
print(min(x))

# sum
x = [2, 3, 1]
print(sum(x))

# sort
x = [2, 3, 1]
x.sort()
print(x)

x = [2, 1, 5, 0, 3]
x.sort()
print(*x)
print(x[len(x) - 2])