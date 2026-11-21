students = {}

while True:
    print("\n--- Student Record Menu ---")
    print("1. Add a student")
    print("2. Update marks")
    print("3. Search for a student")
    print("4. Delete a student")
    print("5. Display all records")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        if roll in students:
            print("Student already exists")
        else:
            name = input("Enter name: ")
            try:
                marks = float(input("Enter marks: "))
            except ValueError:
                print("Invalid marks")
                continue
            students[roll] = {"name": name, "marks": marks}
            print("Student added")

    elif choice == "2":
        roll = input("Enter roll number: ")
        if roll in students:
            try:
                students[roll]["marks"] = float(input("Enter new marks: "))
                print("Marks updated")
            except ValueError:
                print("Invalid marks")
        else:
            print("Student not found")

    elif choice == "3":
        roll = input("Enter roll number: ")
        if roll in students:
            s = students[roll]
            print("Roll:", roll, "| Name:", s["name"], "| Marks:", s["marks"])
        else:
            print("Student not found")

    elif choice == "4":
        roll = input("Enter roll number: ")
        if roll in students:
            del students[roll]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == "5":
        if not students:
            print("No records to display")
        else:
            for roll, s in students.items():
                print("Roll:", roll, "| Name:", s["name"], "| Marks:", s["marks"])

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid choice, try again")
