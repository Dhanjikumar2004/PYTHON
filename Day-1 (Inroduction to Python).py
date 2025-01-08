# Q.1 print helloworld

print("Hello World")

# Q.2 describe local variable and global variable code

'''A local variable is defined within a function and can only be accessed
inside that function'''

def my_function():
    local_var = 10  # This is a local variable
    print("Inside the function, local_var =", local_var)

my_function()

''' A global variable is defined outside of any function and can be accessed
 from any function within the same module.'''

global_var = 20  # This is a global variable

def my_function():
    print("Inside the function, global_var =", global_var)

my_function()
print("Outside the function, global_var =", global_var)

# Q.3 Write a code that describe Indentation error

''' In Python, indentation is crucial because it defines the blocks of code.An
IndentationError occurs when the levels of indentation are inconsistent or
incorrect.'''

def my_function():
    print("This line is correctly indented.")
    print("This line is also correctly indented.")
  #print("This line has incorrect indentation.")  # This will cause an IndentationError

my_function()


# Q.4 write a code that describe local and global variable with same name
#follows the roles

variable = "I am a global variable"  # Global variable

def my_function():
    # Local variable with the same name
    variable = "I am a local variable"
    print("Inside the function:", variable)
my_function()

# Print the global variable
print("Outside the function:", variable)


# Q.5 Write a code for string, int and float input
string_input = input("Enter a string: ")
print("You entered the string:", string_input)
int_input = int(input("Enter an integer: "))
print("You entered the integer:", int_input)
float_input = float(input("Enter a float: "))
print("You entered the float:", float_input)










