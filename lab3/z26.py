class Student:
    def __init__(self):
        self.students = []
        self.grades = {}

    def add_student(self, name):
        self.students.append(name)
        self.grades[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.grades[name].append(grade)
        else:
            print(f"Student {name} nie został dodany.")

# Test
s = Student()
s.add_student("Jan Kowalski")
s.add_grade("Jan Kowalski", 5)
s.add_grade("Jan Kowalski", 4.5)
print(s.students)
print(s.grades)
