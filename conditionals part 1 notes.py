True
False

print(1 == 1)  # True
print(0 == 1)  # False

is_sky_blue = True
print(1 == 1)  # True
print(1 != 0)  # True
print(1 > 1)  # False
print(1 >= 1) # True
print(1 < 1)  # False
print(1 <= 1) # True

# logical operation

# and
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(1 == 1 and 1 > 0)
print(1 == 1 and 0 > 5)

# or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(3 == 3 or 0 > 5)
print(3 > 5 or 1 == 0)

# not
print(not True) # False
print(not False) # True

print(not 1 == 1)

print(1 == 1 or 2 > 3)

# conditional statements
if 1 > 0:
    print("That's true")

if 1 == 0:
    print("That's true")
    
# syntax
# if ___:
#     ____

# x = int(input())
# if x > 5:
#     print("bigger than five")

x = int(input())
if x >= 5:
    print("Great you can buy a ticket!")
if x < 5:
    print("Unfortunately you cannot buy a ticket.")

# else
x = int(input())
if x >= 5:
    print("You can buy a ticket")
else:
    print("You cannot buy a ticket")
    
# syntax
# if ___ :
#     _____
# else:
#     ____

if 1 == 1:
    print("one equals one")
else:
    print("one doesn't equal to one")

if 1 == 5:
    print("one equals five")
else:
    print("one doesn't equal to five")

# intendation
# ok
if 3 == 3:
    print("three equals three")

# error
# if 3 == 3:
# print("three equals three")

# more complex examples
x = int(input())
if x < 14 or x > 65:
    print("entrance is free")