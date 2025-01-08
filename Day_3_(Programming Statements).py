# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
number = int(input("Enter a number: "))
if number%2 == 0:
    print(f" {number} is even number ")
else:
    print(f" {number} is odd number ")

# 2. Using input function take two number and then swap the number
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")

# 3. Write a Program to Convert Kilometers to Miles
km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print(f"{km} kilometers is equal to {miles:.2f} miles.")

#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
principal = 200
rate = 5
time = 5
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is Rs. {simple_interest}.")
