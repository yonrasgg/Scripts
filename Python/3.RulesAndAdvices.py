# 1. Built-in keywords in Python
import keyword
print(keyword.kwlist)  # Prints all Python keywords

# 2. Variables must start with a letter or an underscore
variable1 = "valid"
_1variable = "valid"
# 1variable = "invalid"  # Uncomment to see the error

# 3. Variables are case-sensitive
Variable = "value1"
variable = "value2"
VARIABLE = "value3"
# Prints the values of the variables
print(Variable, variable, VARIABLE) 

# 4. Spaces are not allowed in variable names
my_variable = "valid"
# my variable = "invalid"  # Uncomment to see the error

# 5. Avoid using Python special characters in variable names
# my=variable = "invalid"  # Uncomment to see the error

# 6. Use descriptive and meaningful names for variables
list_of_names = ["Alice", "Bob", "Charlie"]
# Prints the list of names
print(list_of_names)

# 7. Constants are written in uppercase
PI = 3.14159
# Prints the value of PI
print(PI)

# Reserved words in Python
# Try using a reserved word as a variable name
# for = "invalid"  # Uncomment to see the error
