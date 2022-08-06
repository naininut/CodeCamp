# for
print("Welcome!")
print()
print()
print()
print()
print()
print("Loading...")

print("Welcome!")
for i in range(5):
    print()
print("Loading..")

for i in range(10):
    print("Hi")

for i in range(10):
    print(i)

# syntax
# for i in range(number):
#     _____

# intendation
for i in range(3):
    print("Hi")
    print("there")

# error
# for i in range(3):
# print("Hi")
# print("there")

# range
for i in 1, 2, 3:
    print(i)

for i in range(4):  # same as for i in 0, 1, 2, 3
    print(i)
    print(i * i)

for i in range(3):
    print("Hi")
    print("there")

for i in range(5):
    print("Hi")
    print("there")

# start counting with 0
for i in range(3):
    print(i)

i = 0
print(i)
i = i + 1
print(i)
i = i + 1
print(i)

for i in range(4):
    print(i)

for i in range(3):
    print(i + 1)

# range(1, 5)
for i in range(1, 5):
    print(i)

for i in range(7, 11):
    print(i)
    
for a in range(3):
    print(a)

for num in range(3):
    print(num)



y = 2
y = y + 5
y = y + 1
print(y)

# sum of numbers
print(1 + 2 + 3)

cnt = 0
cnt = cnt + 1
cnt = cnt + 2
cnt = cnt + 3
print(cnt)

print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

cnt = 0
cnt = cnt + 1
cnt = cnt + 2
cnt = cnt + 3
cnt = cnt + 4
cnt = cnt + 5
cnt = cnt + 6
cnt = cnt + 7
cnt = cnt + 8
cnt = cnt + 9
cnt = cnt + 10
print(cnt)

cnt = 0
for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    cnt = cnt + i
print(cnt)

cnt = 0
for i in range(1, 11):
    cnt = cnt + i
print(cnt)

cnt = 0
for i in range(1, 20):
    cnt = cnt + i
print(cnt)

# if inside a for loop
for i in range(1, 20):
    if i > 12:
        print("too big")
    else:
        print("ok")