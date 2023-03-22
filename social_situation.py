import math

print("Welcome to the Social Situation Analyzer")
print(" ")
print("Person 1")
name1 = input("Enter your name: ")
xposition1 = int(input("Enter your x position: "))
yposition1 = int(input("Enter your y position: "))
radius1 = int(input("Enter your personal space radius: "))
print(" ")
print("Person 2")
name2 = input("Enter your name: ")
xposition2 = int(input("Enter your x position: "))
yposition2 = int(input("Enter your y position: "))
radius2 = int(input("Enter your personal space radius: "))

# calculations
# distance formula = Square root of ((x2 - x1)**2 + (y2-y1)**2)

xpiece = (xposition2 - xposition1)**2
ypiece = (yposition2 - yposition2)**2
df = math.sqrt(xpiece + ypiece)

r = radius1 + radius2
#if statements
if df == radius1:
    person = name1 +  " is in " +  name2 + "'s personal space"
    space = name1 + " and " + name2 + " personal spaces overlap"
elif df == radius2:
    person = name2 +  " is in " + name1 + "'s personal space"
    space = name1 + " and " + name2 + " personal spaces overlap"
elif df == 0:
    person = name1 + " " + name2 + " are in each others personal space"

elif df >= (radius1 + radius2):
    person = "Neither " + name1 + " or " + name2 + " are in each others personal space"
    space = name1 + " and " + name2 + " spaces do not overlap"
elif df + radius2 < radius1:
    space = name2 + "'s personal space is entirely in " + name1 + "'s personal space"
elif df + radius1 < radius2:
    space = name1 + "'s personal space is entirely in " + name2 + "'s personal space"
else:
    person = "invalid answers"
    space = "invalid answers"

print(" ")
print("Social Situation Analysis Results")
print("Person Test: " + person)
print("Space Test: " + space)



