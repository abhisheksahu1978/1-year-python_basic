        #   TUPLES IN PYTHON

# 0. create a tuple of 3 movies and print them.
# movies = ("3 Idiot", "Bahubali", "Saho")
# print(type(movies))

# 1. Create a tuple containing 5 numbers and print it.
# numbers = (2, 4, 5, 6, 7)
# print((numbers))

# 2. Create a tuple of student names and print the first letter.
# student = ("Abhishek", "Lucky", "Alok", "Vivek")
# print(student)
# for student in student:
#     print(student[0][0])

# 3. Create a tuple of 5 numbers and print the last element.
# number = (1, 4, 6, 7, 8)
# print(number)
# print(number[4])

# 4. Find the length of a tuple using len().
# my_name = ("Abhishek", "kumar")
# print(my_name)
# print(len(my_name))

# 5. Create a tuple and print all elements using a for loop.
# my_intro = ("Mr. Abhishek kumar ", "My Hobby is playing cricket", "age: 19")
# for my_intro in my_intro:
#     print(my_intro)

# 6. Create a tuple and print elements from index 1 to 3 using slicing.
# my_intro = ("Name: Abhishek kumar", "Age: 19", "Hobby: Playing cricket", "Aim: Software engineer", "Study: Graduation(B.tech)")
# print(my_intro[1:3])

# 7. Count how many times a number appears in a tuple using count().
# num = (2,4,5,6,6,7,8,8,8,9,96,5,7,8,9,9)
# print(num.count(9))

# 8. Find the index of a given element using index().
# num = (2, 4, 5, 6, 6, 7, 1, 6)
# print(num.index(5))

# 9. Create two tuples and concatenate them.
# a = ("My name: ")
# b = ("Abhishek kumar")
# c = ("Age: ")
# d = ("19")
# result = a+b,c+d
# print(result)

# 10. Repeat a tuple 3 times using the * operator.
# a = ("I am happy \n")
# result = a * 3
# print(result)

# 11. Check whether a given element exists in a tuple.
# whether = ("summer","winter","rainy","autumn")
# if "summer" in whether:
#     print("whether is exist in tupple")
# else:
#     print("not exist")

# 12. Find the maximum element in a tuple.
# fruits = ("apple", "mango", "guavava", "orange", "banana", "pine-apple", "zine")
# print(max(fruits))
# num = (3, 5, 6, 8, 9, 19, 29, 39, 49)
# print(max(num))

# 13. Find the minimum element in a tuple.
# months = ("january", "february", "march", "april", "june", "may")
# print(min(months))

# 14. Find the sum of all elements in a tuple.
# num = (2, 3, 4, 5, 6, 67, 78, 23)
# print(sum(num))
# result = 1
# for i in num:
#     result = result * i
# print(result)

# 15. Convert a list into a tuple.
# my_list = ["abhishek", "kumar", "age", "19"]
# my_tuple = tuple(my_list)
# print(my_tuple)

# 16. Convert a tuple into a list.
# my_tuple = ("my", "name", "is", "abhishek", "kumar")
# my_list = list(my_tuple)
# print(my_list)

# 17. Create a nested tuple and access an element from the inner tuple.
# number = (10, 20, (30, 40, 50), 60, 70)
# print(number[2][1])

# 18. Perform tuple unpacking and print the values.
# student = ("Abhishek", 19, "Bihar")
# name, age, state = student
# print("name", name) 
# print("age", age)
# print("state", state)

# 19. Create a tuple of 10 numbers and print only the even numbers.
# numbers = (2, 4, 5, 6, 7, 8, 9, 12, 13, 14)
# for numbers in numbers:
#     if numbers % 2 == 0:
#         print("even: ", numbers)

# 20. Create a tuple of 10 numbers and print only the odd numbers.
# numbers = (21, 22, 23, 24, 25, 26, 27, 28, 19, 30)
# for numbers in numbers:
#     if numbers % 2 != 0:
#      print("odd: ",numbers)