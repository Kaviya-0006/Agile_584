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

# Daily update example
add_student("Alice", 101)
view_students()
