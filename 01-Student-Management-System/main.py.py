students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. ADD STUDENT
    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)

        print("Student added successfully!")

    # 2. VIEW ALL STUDENTS
    elif choice == 2:
        if len(students) == 0:
            print("No students found.")

        else:
            print("\n===== STUDENT LIST =====")

            for student in students:
                print("\nRoll Number:", student["roll"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Marks:", student["marks"])

    # 3. SEARCH STUDENT
    elif choice == 3:
        search_roll = int(input("Enter roll number to search: "))

        found = False

        for student in students:
            if student["roll"] == search_roll:
                print("\nStudent Found!")

                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Marks:", student["marks"])

                found = True
                break

        if found == False:
            print("Student not found.")

    # 4. UPDATE STUDENT
    elif choice == 4:
        update_roll = int(input("Enter roll number to update: "))

        found = False

        for student in students:
            if student["roll"] == update_roll:

                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["marks"] = float(input("Enter new marks: "))

                found = True

                print("Student updated successfully!")

                break

        if found == False:
            print("Student not found.")

    # 5. DELETE STUDENT
    elif choice == 5:
        delete_roll = int(input("Enter roll number to delete: "))

        found = False

        for student in students:
            if student["roll"] == delete_roll:

                students.remove(student)

                found = True

                print("Student deleted successfully!")

                break

        if found == False:
            print("Student not found.")

    # 6. EXIT
    elif choice == 6:
        print("Thank you for using Student Management System!")
        break

    # INVALID OPTION
    else:
        print("Invalid choice. Please enter 1-6.")