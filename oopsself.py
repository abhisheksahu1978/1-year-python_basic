# class brother:
#     def __init__(self):
#         print("This is class of my brother")

#     name1="Lucky"
#     name2="Abhishek"
#     educationOfName1="pursing B.Arts"
#     educationOfName2="pursing B.Tech"
#     liveIn="Both are in Indore"
#     AbhishekDream="Abhishek wants to became a software developer."
#     LuckyDream="Lucky wants to became a sdm of Bihar."

# A1 = brother()
# A2 = brother()
# print(A1.name1,A1.educationOfName1)
# print(A2.name2,A2.educationOfName2)
# print(A1.liveIn)
# print(A1.AbhishekDream)
# print(A2.LuckyDream)

# class Student:
#     def __init__ (self,name,rollno,marks):
    #   parameterized constructor.
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     print("This is information of student")

# s1 = Student("Abhishek", 1, 90)
# s2 = Student("Lucky", 2, 80)
# print(s1.name, s1.rollno, s1.marks)
# print(s2.name, s2.rollno, s2.marks)

# class Student:
#     college_name = "Sage University"

#     def __init__ (self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome to ", self.college_name)

#     def drink(self):
#         print(self.name, "is drinking water")

# s1 = Student("Abhishek", 50)
# s1.welcome()
# s1.drink()

# Question: 1. Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.
# class Student:
#     def __init__ (self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def average_marks(self):
#         average_marks = ((self.marks1 + self.marks2 + self.marks3) /3)
#         print("Average marks of ", self.name, "is ", average_marks)
    
# s1 = Student("Abhishek", 49 , 59, 20)
# print("Name",s1.name,"Marks of DSA: ", s1.marks1,"Marks of Python: ", s1.marks2,"Marks of HTML: ", s1.marks3)
# s1.average_marks()

# class Employee:
#     def __init__ (self, name, salary):
#         self.name = name
#         self.salary = salary
#     @staticmethod     #decorator
#     def hello():
#         print("hello")
# e1 = Employee("Abhishek", 50000)
# print(e1.name, e1.salary)
# e1.hello()  
