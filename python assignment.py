# Task 1: Variables
# Let's describe a person using basic variables!

name = "Ronik"
age = 21
height = 6.2

print("Hey there, my name is", name + "!")
print("I'm", age, "years old and", height, "feet tall. 🚀")

# Task 2: Operators
# Doing some math magic with two numbers!

num1 = 15
num2 = 4

print("\nTask 2: Let's do some math! 🔢")
print("The sum of", num1, "and", num2, "is", num1 + num2)
print("The difference is", num1 - num2)
print("Multiplication gives us", num1 * num2)
print("Division gives us", num1 / num2)

# Task 3: Conditional Statement
# Let’s make Python think by checking the type of number entered!

print("\nTask 3: Number Checker 🧠")
number = float(input("Enter a number: "))

if number > 0:
    print("This number is positive. Awesome! 🌞")
elif number < 0:
    print("This number is negative. Better luck next time! ❄️")
else:
    print("Zero it is. A perfect balance! ⚖️")
