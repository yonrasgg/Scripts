import cmath # Import the cmath module to work with complex numbers

"""\(ax^3 + bx^2 + cx + d = 0\)"""
# Enter the value of the variables you want to calculate
a = float(input("Enter the value of a: ")) 
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))

delta_0 = b**2 - 3*a*c # Discriminant 1
delta_1 = 2*b**3 - 9*a*b*c + 27*a**2*d # Discriminant 2
C = ((delta_1 + cmath.sqrt(delta_1**2 - 4*delta_0**3))/2)**(1/3) # Constant C

x1 = (-1/(3*a))*(b + C + delta_0/C) # Solution 1
x2 = (-1/(3*a))*(b + complex(-0.5, cmath.sqrt(3)/2)*C + delta_0/(complex(-0.5, cmath.sqrt(3)/2)*C)) # Solution 2
x3 = (-1/(3*a))*(b + complex(-0.5, -cmath.sqrt(3)/2)*C + delta_0/(complex(-0.5, -cmath.sqrt(3)/2)*C)) # Solution 3

print("The solutions of the equation are: ", x1, x2, x3) # Prints: The solutions of the equation are:  <x1> <x2> <x3>