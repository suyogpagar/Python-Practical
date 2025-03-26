class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")



student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 92)
student3 = Student("Charlie", 103, 78)


student1.display_details()
student2.display_details()
student3.display_details()
