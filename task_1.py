'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
'''

# Solution 1 :
print("Checks whether the number is even or odd")
a = int(input(("Enter your number : ")))

# Solution 2 and 3 :
if (a%2 == 0) :
    print("Your number",a," is even")

else:
    print("Your number",a," is odd")

