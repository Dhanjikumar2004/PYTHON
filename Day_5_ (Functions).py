#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
def div(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2
result = div(10, 2)
print("The result of the division is:", result)
result = div(10, 5)
print("The result of the division is:", result)

#2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number .
def square(num):
    return num ** 2
num = 19
square_result = square(num)
print("The square of", num, "is:", square_result)

# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers. 
# Manually define 5 random numbers
random_numbers = [23, 45, 12, 67, 34]
print("Random numbers:", random_numbers)
maximum = max(random_numbers)
minimum = min(random_numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)

# . Accept a name from the user and display that in lower case using lower() function
name = input("Enter your name: ")
lowercase_name = name.lower()
print("Your name in lowercase is:", lowercase_name)