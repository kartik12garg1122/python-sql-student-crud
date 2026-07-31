import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (name, age, course)
    )

    conn.commit()
    print("Student Added Successfully")


def view_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\nStudent Records")
    print("-------------------------")

    for student in students:
        print(student)


def update_student():
    student_id = int(input("Enter Student ID: "))
    new_course = input("Enter New Course: ")

    cursor.execute(
        "UPDATE students SET course=? WHERE id=?",
        (new_course, student_id)
    )

    conn.commit()

    print("Student Updated")


def delete_student():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()

    print("Student Deleted")


while True:

    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        conn.close()
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")