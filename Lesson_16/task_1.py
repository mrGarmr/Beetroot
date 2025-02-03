# School
# Make a class structure in python representing people at school. Make a base class called Person, a class called Student, 
# and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes, 
# and keep in mind which are common and which are not. For example, the name should be a Person attribute, 
# while salary should only be available to the teacher. 


# Base class of a Person
class Person:
    """A class structure in python representing people at school"""
    def __init__(self, name, age, gender):
        self.name = name         
        self.age = age            
        self.gender = gender      

    def full_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


#class for Students
class Student(Person):
    def __init__(self, name, age, gender, grade, student_id):
        super().__init__(name, age, gender)
        self.grade = grade 
        self.student_id = student_id   

    def full_info(self):
        return f"{super().full_info()}, Grade: {self.grade}, Student ID: {self.student_id}"


#Class for Teachers
class Teacher(Person):
    def __init__(self, name, age, gender, subject, salary):
        super().__init__(name, age, gender)
        self.subject = subject
        self.salary = salary

    def full_info(self):
        return f"{super().full_info()}, Subject: {self.subject}, Salary: {self.salary}"


student = Student("Vasj", 19, "Male", "11 A", "V12345")
teacher = Teacher("Viktor Mykolaiovych", 50, "Male", "Math", 20000)

print(student.full_info())
print(teacher.full_info())

