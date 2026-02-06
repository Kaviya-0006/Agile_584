students = []

def add_student(name, roll_no):
    students.append({"name": name, "roll_no": roll_no})
    print(f"Student {name} added successfully.")

def view_students():
    if not students:
        print("No students registered yet.")
    else:
        print("Registered students:")
        for s in students:
            print(f"{s['roll_no']} - {s['name']}")


add_student("Yuri Hanamichi", 122)
view_students()
