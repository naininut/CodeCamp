# elif
print("Enter your height:")
height = int(input())
if height < 120:
    print("S")
elif height < 140:
    print("M")
else:
    print("L")
    

points = int(input())
if points < 20:
    print("Emerging")
elif points < 60:
    print("Developing")
elif points < 80:
    print("Achieved")
else:
    print("Mastered")

# nested if statement
x = int(input())
if x >= 10:
    if x <= 99:
        print("two-digit number")


x = int(input())
if x <= 0:
    print("No it's not positive. Try again:")
    x = int(input())
    if x > 0:
        print("Ok")
    else:
        print("still not positive")
else:
    print("Ok")
    
a = int(input())
if a <= 0:
    print("ERROR")
else:
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

# elif with nested loop
points = int(input())
if points < 20:
    print("Emerging")
elif points <= 60:
    print("Developing")
else:
    print("Achieved")

if points < 20:
    print("Emerging")
else:
    if points <= 60:
        print("Developing")
    else:
        print("Achieved")