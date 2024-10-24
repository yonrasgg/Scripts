print(10 > 2) # Prints: True
print(20 < 10 and 10 > 2) # Prints: False
print(20 < 10 or 10 > 2) # Prints: True
print(not 10 > 2) # Prints: False
print(10 > 2 and 20 < 10 or 10 > 20) # Prints: False
print(10 > 2 and (20 < 10 or 10 > 2)) # Prints: True
print(10 > 2 and not 20 < 10 or 10 > 2) # Prints: True
print(10 > 2 and not (20 < 10 or 10 > 2)) # Prints: False
print(99 != 100 and 100 == 100) # Prints: True
print(99 != 100 and 100 != 100) # Prints: False 
print(99 != 100 or 100 == 100) # Prints: True
print(99 != 100 or 100 != 100) # Prints: True
print(100 <= 99 not in [1, 2, 3, 4, 5]) # Prints: False
print(100 <= 99 not in [1, 2, 3, 4, 5] and 100 == 100) # Prints: False
