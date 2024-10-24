string1 = 'I am showing an example of a boolean method for strings'
string2 = 'i am showing an example of a boolean method for strings'
string3 = 'I AM SHOWING AN EXAMPLE OF A BOOLEAN METHOD FOR STRINGS'
string4 = '1234567890'

print(string1.startswith('I am')) # Prints: True
print(string1.endswith('strings')) # Prints: True
print(string1.isalnum()) # Prints: False
print(string4.isalnum()) # Prints: True
print(string1.isalpha()) # Prints: False
print(string1.isdigit()) # Prints: False
print(string2.islower()) # Prints: True
print(string3.isupper()) # Prints: True
