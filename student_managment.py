class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display()
            print("Grade:", student.grade())
            print("-" * 30)


# Main Program
sms = StudentManagementSystem()

s1 = Student(101, "Parth", 92)
s2 = Student(102, "Rahul", 78)
s3 = Student(103, "Amit", 65)

sms.add_student(s1)
sms.add_student(s2)
sms.add_student(s3)

sms.display_students()