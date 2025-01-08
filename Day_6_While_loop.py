# Print the reverse order series  using a while loop
numbers = [4,5,6,7,8,9]
index = -1 
while index>=-6: 
   print(f"Value of list at index {index} is  = {numbers[index]}")
   index  = index - 1

# 2.      Create a code that describe the use of break statement in while loop
n = [1,2,3,4,5,6,7]
i = 0
while i <= len(n):
    print(f"Count is: {i}")
    i += 1
    if i == 4:
        break
print("Loop ended.")

#3. Write a Python program using a while loop to iterate through each character of 
# the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.
string = "Python"
i = 0
while i < len(string):
    print(f"charecter of {i} is {string[i]}")
    i += 1  
print(f"Length of the string: {len(string)}")

#4.      Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. 
# Display the result as the factorial of the entered number.
num = int(input("Enter a non-negative numbers: "))
if num < 0:
    print("Factorial is not defined negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    print(f"The factorial of {num} is {factorial}")

#Write a python program to reverse a number using a while loop.
# Input from the user
number = int(input("Enter a number: "))
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10  
print(f"The reversed number is: {reversed_number}")


# Write a python program to check whether a number is palindrome or not?
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit  
    number //= 10 
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")


#Write a python program finding the factorial of a given number using a while loop.
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

user_input = input("Enter a non-negative integer: ")
if user_input.isdigit():
    number = int(user_input)
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}.")
else:
    print("Please enter a valid non-negative integer.")


#Accept numbers using input() function until the user enters 0. If user input 0 then break the 
# while loop and display the sum of all the numbers.
# Initialize the sum variable
total_sum = 0
while True:
    number = int(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break  
    total_sum += number

print(f"The sum of all numbers is: {total_sum}")


# Program to check whether the given number is palindrome or not.
def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

# Program to check whether the given number is Armstrong or not
def is_armstrong(number):
    digits = str(number)
    power = len(digits)  
    armstrong_sum = sum(int(digit) ** power for digit in digits)
    return armstrong_sum == number
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#  Program to find the factorial of a number.
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")







 
