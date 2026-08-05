from grade_utils import calculate_average, determine_letter_grade

student_name = input("Enter student name: ")
midterm = float(input("Enter midterm grade: "))
final = float(input("Enter final grade: "))

average = calculate_average(midterm, final)
letter = determine_letter_grade(average)

print("\n----- RESULT -----")
print(f"Student: {student_name}")
print(f"Average: {average:.2f}")
print(f"Letter Grade: {letter}")