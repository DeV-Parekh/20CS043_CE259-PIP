# Creating a class Student
class Student:
    student_name = None
    student_id = 0

    # Function to set the name and id
    def set_info(self, name, id):
        self.student_name = name
        self.student_id = id

    # Function to get info of name and id
    def get_info(self):
        print('Student Name:- ', self.student_name)
        print('Student ID:- ', self.student_id)


# Creating a class Exam from class Student
class Exam(Student):
    marks = []

    # Function to set the marks of student
    def set_marks(self, marks):
        self.marks = marks

    # Funtion to get marks list
    def get_marks(self):
        return marks


# Creating a class Result from class Exam.
class Result(Exam):
    total_marks = 0

    # Function to obtain the total marks of student
    def result(self, marks_list):
        self.total_marks = sum(marks_list)
        return self.total_marks


# Creating an object of result class.
s1 = Result()
name = input("Enter Name of the student : ")
id = input("Enter Roll Number of the student : ")

# Setting the details and marks
s1.set_info(name, id)
print(f"Enter the marks of {s1.student_name} in 6 subjects : ")
marks = []
for i in range(6):
    marks.append(int(input()))
s1.set_marks(marks)

# Getting total marks
total_marks = s1.result(marks)

# Printing results
s1.get_info()
print('Total marks is:- ', total_marks)
