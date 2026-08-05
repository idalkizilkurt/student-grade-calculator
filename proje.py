from grade_utils import calculate_average, determine_letter_grade

midterm = float(input("Enter midterm grade: "))
final = float(input("Enter final grade: "))

average = calculate_average(midterm, final)
letter = determine_letter_grade(average)

print(f"\nAverage: {average:.2f}")
print(f"Letter Grade: {letter}")