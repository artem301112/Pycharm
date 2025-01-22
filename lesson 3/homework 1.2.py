class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.energy = 100

    def teach(self, student):
        if self.energy > 0:
            print(f"{self.name} is teaching {self.subject} to {student.name}.")
            self.energy -= 10
            student.knowledge += 5
        else:
            print(f"{self.name} is too tired to teach.")

    def grade(self, student):
        if self.energy > 0:
            print(f"{self.name} is grading {student.name}'s assignment.")
            self.energy -= 5
            student.assignments_completed += 1
        else:
            print(f"{self.name} is too tired to grade.")


class Student:
    def __init__(self, name):
        self.name = name
        self.knowledge = 0
        self.assignments_completed = 0

    def study(self):
        print(f"{self.name} is studying.")
        self.knowledge += 5

    def do_assignment(self, teacher):
        print(f"{self.name} is doing an assignment.")
        teacher.grade(self)

mr_smith = Teacher(name="Mr. Smith", subject="Math")
john = Student(name="John")

for day in range(1, 6):
    print(f"Day {day}:")
    mr_smith.teach(john)
    john.study()
    john.do_assignment(mr_smith)
    print(f"{john.name}'s knowledge: {john.knowledge}")
    print(f"{john.name}'s assignments completed: {john.assignments_completed}")
    print(f"{mr_smith.name}'s energy: {mr_smith.energy}")
    print()