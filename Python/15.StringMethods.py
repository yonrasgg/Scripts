string = 'This is a string method in Python'

print(string.upper()) # Prints: THIS IS A STRING METHOD IN PYTHON
print(string.lower()) # Prints: this is a string method in python
print(string.capitalize()) # Prints: This is a string method in python
print(string.title()) # Prints: This Is A String Method In Python
print(string.swapcase()) # Prints: tHIS IS A STRING METHOD IN pYTHON
print(string.replace('Python', 'C++')) # Prints: This is a string method in C++
print(string.replace('Python', 'C++', 1)) # Prints: This is a string method in C++ (Only replaces the first occurrence)
print(string.count('i')) # Prints: 4
print(string.count('i', 0, 15)) # Prints: 2
print(string.find('i')) # Prints: 2
print(string.find('i', 0, 15)) # Prints: 2
