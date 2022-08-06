print("Hello")
print('Hello')

# create a variable
name = "Alex"
print(name)

# operations
name = "Harry "
full_name = name + "Potter"
print(full_name)

# empty string
name = "Alex"
print(name + "")

# read a string from a user
# x = input()
# print(x)

# x = input()
# print(x + " there")

# converting str to int
print("5" + "7")

print(int("5") + int("7"))

# length of str
name = "Alex"
print(len(name))

# get a character at position
x = "abcd"

# abcd
# 0123
print(x[0])
print(x[3])

print(x[2])

# print letters of a string
name = "John"
for i in range(len(name)):
    print(name[i])

x = input()
ans = "NO"
for i in range(len(x)):
    if x[i] == "x":
        ans = "YES"
print(ans)

# substrings
# "Alex Johns o  n"
#  0123456789 10 11
name = "Alex Johnson"
print(name[0:4])

text = "How is it going?"
print(text[10:15])

text = input()
print(text[0:3])

# print on the same line
print("abc", end="")
print("abc", end="")