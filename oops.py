# OOPS
# class Employee:
#     def __init__(self):
#         self.name = None
#         self.salary = None

#     def set_data(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show(self):
#         print(self.name, self.salary)

# # self pointss to current instance (object) of the class
# # Objects Creation
# e1=Employee()
# e2=Employee()

# e1.set_data("Abhishek",50000)
# e2.set_data("Lucky",60000)
# print(e1.name,e1.salary)
# print(e2.name,e2.salary)

# class Employee:
#     def __init__ (self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print("Name:", self.name,"salary:",  self.salary)

# # child class
# class Employee_Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)  # calling parent class constructor
#         self.department = department
#     def executesduty(self):
#         print(self.name, "is managing the ", self.department, "department")
# m1 = Employee_Manager("Abhishek", 50000, "IT")
# m1.show()
# m1.executesduty()  

# Abstract class   #It is used to force child classes to implement the methods.
# Abstract class object cannot be created.
# from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
# c1 = Circle(8)
# print("Area of circle: ", c1.area())

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
#     def eat(self):
#         print("Eating Bread")

# d= Dog()
# d.sound()
# c= Cat()
# c.sound()
# c.eat()

# class Point:
#     def __init__ (self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print("point:", self.x, self.y)
#     # Change coordenates
#     def change(self, x, y):
#         self.x = x
#         self.y = y
#     # Distance between 2 points
#     def dist(self, other):
#         d= ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
#         return d
# # Create 3 points
# p1 = Point(1, 2)
# p2 = Point(4, 6)
# p3 = Point(0, 0)
# # Access Methods
# p1.show()
# p2.show()

# p1.change(2, 3)
# p1.show()
# print("Distance between p1 and p2:", p1.dist(p2))
# print("Distance between p1 and p3:", p2.dist(p3))

'''create a file and write  data into it 
file=open("student.txt","w") #Write mode (creates file)
file.write("Name:Abhishek kumar\n")
file.write("Course.Btech\n")
file.close()
print("File created and data written successfully!")

# #Read file data 
file= open("student.txt", "r") #Read mode(reads content insode file)
data=file.read()
print(data)
file.close()

#Append data (add new data without deleting old data)
file=open("student.txt","a")
file.write("City.Indore\n")
file.close()

#Read whole content of file also appended data
file=open("student.txt","r")
for line in file:
    print(line.strip()) #remove extra newline
file.close()

#Update specific content
file= open("student.txt","r")
data= file.read()
print(data)
file.close()

print("***********************")
data=data.replace("Abhishek kumar","Ashu")
file=open("student.txt","w")
file.write(data)
file.close()

print("***********************")
print("File updated successfully")
file=open("student.txt", "r")
updated_data=file.read()
print(updated_data)
file.close()'''

#Delete content inside file
# with open("student.txt","w") as file:
#     file.write(" ")
# print("File cleared successfully!")

# file=open("student.txt","r")
# data= file.read()
# print(data)
# file.close()

# Recursive Function
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# Palindrome using recurdion
# def is_palindrome(s):
#     if len(s) <=1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     # recursive call (remove 1st and last)
#     return is_palindrome(s[1:-1])

# step 1st: create and open
# write mode has 2 purpose 
# 1)If file exists, it removes old content of file and write the current content.
# 2)if file don't exists, if. creates a new file, them write current content.

# file=open("students_details.txt","w")
# file.write("101 , Abhi, 90\n")
# file.write("102, Ashu, 85\n")
# file.write("103, Nishant, 90\n")

# file.close()

# step2: search student
# search_id="102"
# found=False
# file=open("Student_details.txt","A")
# for line in file:
#     data=line.strip().split(",")
#     if data[0]==search_id:
#         print("Student Found:",line)
#         found=True
# file.close()
