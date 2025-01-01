# Foundation of Python

# Engage & Apply: Create a program that takes your name, age, and favorite color as an input and prints them out.
print("Hello, my name is Python!")

# Input information.
name = input("Who are you? ")
age = input("Pleased to meet you, " + name + ". How old are you? ")
favorite_color = input("What is your favorite color? ")

# Python's response.
print("So, you are " + name + ", " + age + " years old, and your favorite color is " + favorite_color + ".")
print("Thank you for introducing yourself! Have a great day!")

# Final Challenge: Build a program that asks the user to input their exam score and then prints a message.
# "Excellent" if the score is greater than 90.
# "Good" if the score is between 70 and 90.
# "Needs Improvement" if the score is below 70.

print("Welcome to the exam.")

# Input the test score.
score = int(input("What is your test score? "))
if score > 90:
    print("Excellent work!")
elif score >= 70:
    print("Good job!")
else:
    print("Needs Improvement.")

print("Thank you for taking the exam.")

# https://github.com/SandyPham092595/Foundation-of-Python.git