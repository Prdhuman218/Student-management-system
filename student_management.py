# ==============================
# STUDENT MANAGEMENT SYSTEM
# ==============================


class Student:

    def __init__(self, name, roll_no, class_name, age, marks):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name
        self.age = age
        self.marks = marks

    def display_info(self):
        print("\n===== Student Details =====")
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Class   : {self.class_name}")
        print(f"Age     : {self.age}")
        print(f"Marks   : {self.marks}")


students = []


# ==============================
# DISPLAY STUDENTS
# ==============================

def display_student():

    try:
        with open("student.txt", "r") as file:

            first_line = file.readline()

            if first_line == "":
                print("No student found.")
                return

            file.seek(0)

            for line in file:

                name, roll_no, class_name, age, marks = line.strip().split(",")

                print("\n----------------------")
                print(f"Name    : {name}")
                print(f"Roll No : {roll_no}")
                print(f"Class   : {class_name}")
                print(f"Age     : {age}")
                print(f"Marks   : {marks}")

    except FileNotFoundError:
        print("Student file not found.")


# ==============================
# ADD STUDENT
# ==============================

def add_student():

    try:
        name = input("Enter name: ")

        roll_no = int(input("Enter roll no: "))

        # Duplicate roll number check
        try:
            with open("student.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) >= 2 and data[1] == str(roll_no):
                        print("Roll number already exists!")
                        return

        except FileNotFoundError:
            pass

        class_name = input("Enter class: ")

        age = int(input("Enter age: "))

        marks = float(input("Enter marks: "))

        # Marks validation
        if marks < 0 or marks > 100:
            print("Invalid marks! Marks should be between 0 and 100.")
            return

        details = f"{name},{roll_no},{class_name},{age},{marks}"

        with open("student.txt", "a") as file:
            file.write(details + "\n")

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")


# ==============================
# SEARCH STUDENT
# ==============================

def search_student():

    try:

        roll_no = int(input("Enter roll no: "))

        found = False

        with open("student.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) >= 5 and data[1] == str(roll_no):

                    print("\n===== Student Found =====")
                    print("Name   :", data[0])
                    print("Roll No:", data[1])
                    print("Class  :", data[2])
                    print("Age    :", data[3])
                    print("Marks  :", data[4])

                    found = True
                    break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

    except ValueError:
        print("Invalid input! Enter a valid roll number.")


# ==============================
# UPDATE STUDENT
# ==============================

def update_student():

    try:

        roll_no = int(input("Enter roll no: "))

        updated_students = []
        found = False

        with open("student.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) >= 5 and data[1] == str(roll_no):

                    print("\n===== Student Found =====")

                    new_name = input("Enter new name: ")

                    new_roll_no = int(input("Enter new roll no: "))

                    new_class_name = input("Enter new class: ")

                    new_age = int(input("Enter new age: "))

                    new_marks = float(input("Enter new marks: "))

                    if new_marks < 0 or new_marks > 100:
                        print("Invalid marks!")
                        return

                    new_record = (
                        f"{new_name},{new_roll_no},"
                        f"{new_class_name},{new_age},{new_marks}\n"
                    )

                    updated_students.append(new_record)

                    found = True

                else:
                    updated_students.append(line)

        with open("student.txt", "w") as file:
            file.writelines(updated_students)

        if found:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

    except ValueError:
        print("Invalid input! Enter valid numbers.")


# ==============================
# GRADE STUDENT
# ==============================

def grade_student():

    try:

        roll_no = int(input("Enter roll no: "))

        found = False

        with open("student.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) >= 5 and data[1] == str(roll_no):

                    marks = float(data[4])

                    print("\n===== Student Grade =====")
                    print("Name :", data[0])
                    print("Marks:", marks)

                    if marks >= 90:
                        print("Grade: A")

                    elif marks >= 80:
                        print("Grade: B")

                    elif marks >= 70:
                        print("Grade: C")

                    elif marks >= 60:
                        print("Grade: D")

                    elif marks >= 50:
                        print("Grade: E")

                    else:
                        print("Grade: Fail")

                    found = True
                    break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

    except ValueError:
        print("Invalid input! Enter a valid roll number.")


# ==============================
# DELETE STUDENT
# ==============================

def delete_student():

    try:

        roll_no = int(input("Enter roll no: "))

        updated_students = []
        found = False

        with open("student.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) >= 5 and data[1] == str(roll_no):

                    found = True
                    print("Student deleted successfully!")

                else:
                    updated_students.append(line)

        with open("student.txt", "w") as file:
            file.writelines(updated_students)

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")

    except ValueError:
        print("Invalid input! Enter a valid roll number.")


# ==============================
# TOTAL STUDENTS
# ==============================

def total_student():

    try:

        count = 0

        with open("student.txt", "r") as file:

            for line in file:

                if line.strip():
                    count += 1

        print("\nTotal Students:", count)

    except FileNotFoundError:
        print("Student file not found.")


# ==============================
# MAIN MENU
# ==============================

try:

    while True:

        print("\n==============================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Display Student")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Grade Student")
        print("6. Delete Student")
        print("7. Total Student")
        print("8. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_student()

            elif choice == 2:
                add_student()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                grade_student()

            elif choice == 6:
                delete_student()

            elif choice == 7:
                total_student()

            elif choice == 8:
                print("Thank you!")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter a number.")

except KeyboardInterrupt:
    print("\nProgram stopped.")