# Variables

a = 2
b = 7
c = 8

# Example 1

sum_result = a + b
multiplication_result = a * c

example1 = (sum_result / multiplication_result) ** a

print(f"The result of example 1 is: {example1}") # Result 0.31640625


# Example 2

example2 = ((a + b) / (a * c)) ** a

print(f"The result of example 2 is: {example2}") # Result 0.31640625


# Example 3

example3 = pow((a + b) / (a * c), a)

print(f"The result of example 3 is: {example3}") # Result 0.31640625


# Example 4

print((2 + 7) / (2 * 8) ** 2) # Result 0.00390625
