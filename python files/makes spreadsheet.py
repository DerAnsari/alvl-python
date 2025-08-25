# Create empty lists to store the data
names = []
classes = []
math_grades = []
physics_grades = []
chemistry_grades = []
totals = []
averages = []

# Input data for 10 students
for _ in range(10):
    name = input("Enter student name: ")
    class_name = input("Enter student class: ")
    math_grade = float(input("Enter math grade: "))
    physics_grade = float(input("Enter physics grade: "))
    chemistry_grade = float(input("Enter chemistry grade: "))

    # Append the data to the respective lists
    names.append(name)
    classes.append(class_name)
    math_grades.append(math_grade)
    physics_grades.append(physics_grade)
    chemistry_grades.append(chemistry_grade)

    # Calculate the total and average for each student
    total = math_grade + physics_grade + chemistry_grade
    average = total / 3
    totals.append(total)
    averages.append(average)

# Display the data in a tabular format
print("\nName\tClass\tMath\tPhysics\tChemistry\tTotal\tAverage")
for i in range(10):
    print(f"{names[i]}\t{classes[i]}\t{math_grades[i]}\t{physics_grades[i]}\t{chemistry_grades[i]}\t\t{totals[i]}\t{averages[i]}")
