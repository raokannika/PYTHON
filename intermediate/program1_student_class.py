# Program 1: Student class to store name and marks

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
    
    def average(self):
        return sum(self.marks) / len(self.marks)

# Example
s1 = Student("Alice", [90, 85, 88])
s1.display()
print("Average Marks:", s1.average())
