import sqlite3

connect = sqlite3.connect("uni.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT ,
               age INTEGER,
               major TEXT)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT ,
               instructor TEXT)""")

cursor.execute(''' CREATE TABLE IF NOT EXISTS student_courses(
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY(student_id) REFERENCES students(id),
               FOREIGN KEY(course_id) REFERENCES course(course_id))
''')


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Введіть ім'я студента")
        age = input("Введіть вік студента")
        major = input("Введіть специалізацію студента")
        cursor.execute(""" 
            INSERT INTO students (name, age, major)
            VALUES (?, ?, ?)
        """, (name, age, major))
        connect.commit()

    elif choice == "2":
        course_name = input("Введіть назву курсу")
        instructor = input("Введіть ім'я викладача")
        cursor.execute(""" 
            INSERT INTO courses (course_name, instructor)
            VALUES (?, ?)
        """, (course_name, instructor))
        connect.commit()

    elif choice == "3":
        output = cursor.execute(""" SELECT * FROM students""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
     
    elif choice == "4":
        cursor.execute(""" SELECT * FROM courses """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == "5":
        student_id = input("Введіть ID студента: ")
        course_id = input("Введіть ID курсу: ")
        cursor.execute(""" 
            INSERT INTO student_courses (student_id, course_id)
            VALUES (?, ?)
        """, (student_id, course_id))
        connect.commit()

    elif choice == "6":
        course_id = input("Введіть ID курсу: ")
        cursor.execute(""" 
            SELECT students.name, students.age, students.major
            FROM students
            JOIN student_courses ON students.id = student_courses.student_id
            WHERE student_courses.course_id = ?
        """, (course_id,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")