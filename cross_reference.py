# Week 2 - Cross Reference Match Engine

def load_students(filename):
    students = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                data = line.split(",")

                student = {
                    "id": data[0],
                    "name": data[1],
                    "department": data[2]
                }

                students.append(student)

    return students


def load_marks(filename):
    marks = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line:
                data = line.split(",")
                marks[data[0]] = data[1]

    return marks


def merge_records(students, marks):
    print("\n========== STUDENT PERFORMANCE SUMMARY ==========\n")

    for student in students:

        student_id = student["id"]

        if student_id in marks:
            mark = marks[student_id]
        else:
            mark = "Marks Not Found"

        print(f"Student ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Department : {student['department']}")
        print(f"Marks      : {mark}")
        print("-" * 40)

    print("\nStudents available in marks.txt but missing in students.txt\n")

    for student_id, mark in marks.items():

        found = False

        for student in students:
            if student["id"] == student_id:
                found = True
                break

        if not found:
            print(f"Student ID : {student_id}")
            print(f"Marks      : {mark}")
            print("-" * 40)


def main():
    students = load_students("students.txt")
    marks = load_marks("marks.txt")
    merge_records(students, marks)


if __name__ == "__main__":
    main()