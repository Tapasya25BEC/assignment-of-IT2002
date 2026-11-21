try:
    n = int(input("Enter number of courses: "))

    total_points = 0
    total_credits = 0

    for i in range(1, n + 1):
        print("Course", i)
        grade_point = float(input("  Grade point: "))
        credit = float(input("  Credit: "))
        total_points += grade_point * credit
        total_credits += credit

    if total_credits == 0:
        print("Total credits cannot be zero")
    else:
        gpa = total_points / total_credits
        print("GPA:", round(gpa, 2))
except ValueError:
    print("Error: please enter valid numbers")
