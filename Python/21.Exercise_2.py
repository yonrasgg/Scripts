# Enter the values of the grades for assignments, exams, and project
assignment1 = float(input("Enter the grade for assignment 1: "))
assignment2 = float(input("Enter the grade for assignment 2: "))
assignment3 = float(input("Enter the grade for assignment 3: "))
exam1 = float(input("Enter the grade for exam 1: "))
exam2 = float(input("Enter the grade for exam 2: "))
project = float(input("Enter the grade for the project: "))

average_assignments = (assignment1 + assignment2 + assignment3) / 3 # Average of the assignments
average_exams = (exam1 + exam2) / 2 # Average of the exams
final_grade = 0.3 * average_assignments + 0.4 * average_exams + 0.3 * project # Final grade

print("The final grade is: ", final_grade) # Prints: The final grade is: <final_grade>
