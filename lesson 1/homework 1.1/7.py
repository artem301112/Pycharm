def determine_grade(points):
    if points < 0 or points > 100:
        return "Invalid number of points. Please enter a number between 0 and 100."
    elif points <= 49:
        return "Unsatisfactory"
    elif points <= 69:
        return "Satisfactory"
    elif points <= 89:
        return "Good"
    else:
        return "Excellent"

points = int(input("Enter the number of points received on the exam: "))
grade = determine_grade(points)
print(f"The grade received is: {grade}")