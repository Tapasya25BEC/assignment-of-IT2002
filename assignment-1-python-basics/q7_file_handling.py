try:
    n = int(input("How many students? "))
except ValueError:
    print("Error: please enter a valid number")
else:
    file = open("students.txt", "w")
    for i in range(n):
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        branch = input("Enter branch: ")
        file.write(name + "," + roll + "," + branch + "\n")
    file.close()
    print("Details saved in students.txt")

    print("\nContents of the file:")
    file = open("students.txt", "r")
    for line in file:
        name, roll, branch = line.strip().rsplit(",", 2)
        print("Name:", name, "| Roll No:", roll, "| Branch:", branch)
    file.close()
