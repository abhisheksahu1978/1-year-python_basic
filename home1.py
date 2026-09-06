                # LISTS IN PYTHON

# 1.) Write a Python program to create a list of 3 movies and print them.
# movies = []

# movies1 = input("enter 1st movie name: ")
# movies2 = input("enter 2nd movie name: ")
# movies3 = input("enter 3rd movie name: ")

# movies.append(movies1)
# movies.append(movies2)
# movies.append(movies3)

# print("the movies you entered are: ",movies)

# 2.) Write a Python program to create a list of numbers and print the sum of the numbers.

# numbers = []
# num1 = int(input("enter 1st number: "))
# num2 = int(input("enter 2nd number: "))
# num3 = int(input("enter 3rd number: "))
# sum = num1 + num2 + num3

# numbers.append(num1)
# numbers.append(num2)
# numbers.append(num3)

# print("the numbers you entered are: ", numbers , "and the sum of the numbers is: ", sum)

# 3.) Write a Python program to create a list of 5 fruits and print the fruits in reverse order.

# fruits = []

# fruits1 = input("enter 1st fruit name: ")
# fruits2 = input("enter 2nd fruit name: ")
# fruits3 = input("enter 3rd fruit name: ")
# fruits4 = input("enter 4th fruit name: ")
# fruits5 = input("enter 5th fruit name: ")

# fruits.append(fruits1)
# fruits.append(fruits2)
# fruits.append(fruits3)
# fruits.append(fruits4)
# fruits.append(fruits5)

# print("the fruits you entered are: ", fruits)
# print("the fruits in reverse order are: ", fruits[::-1])

# 4.) Write a Python program to create a list of 4 cities and print the cities in uppercase.

# cities = []

# cities.append(input("enter 1st city name: "))
# cities.append(input("enter 2nd city name: "))
# cities.append(input("enter 3rd city name: "))
# cities.append(input("enter 4th city name: "))

# print(cities)
# print("the cities in uppercase are: ", [city.upper() for city in cities]) 

# 5.) Write a Python program to create a list of 3 animals and print the animals that start with the letter 'a'.
# animals = []

# animals.append(input("enter 1st animal name: "))
# animals.append(input("enter 2nd animal name: "))
# animals.append(input("enter 3rd animal name: "))

# print(animals)
# for animals in animals:
#    if (animals[0].startswith('a') or animals[1].startswith('a') or animals[2].startswith('a')):
#     print("the animals that start with the letter 'a' are: ",animals)
#    else:
#     print("there are no animals that start with the letter 'a'")

# 6.) Write a Python program to create a list of 5 numbers and print the largest number in the list.  
# numbers = []

# numbers.append(int(input("enter 1st number: ")))
# numbers.append(int(input("enter 2nd number: ")))
# numbers.append(int(input("enter 3rd number: ")))
# numbers.append(int(input("enter 4th number: ")))
# numbers.append(int(input("enter 5th number: ")))
 
# print("list of five number is: ",numbers)
# print("the largest number is: ", max(numbers))
# print("minimum number is: ", min(numbers))

# 7.) Write a Python program to create a list of 5 numbers and print the even numbers in the list.
# num = []

# num.append(int(input("enter 1st num: ")))
# num.append(int(input("enter 2nd num: ")))
# num.append(int(input("enter 3rd num: ")))
# num.append(int(input("enter 4th num: ")))
# num.append(int(input("enter 5th num: ")))

# print("the list of five num is : ", num)
# # print("the even numbers in the list are: ", [n for n in num if n % 2 == 0])
# for num in num:
#     if (num % 2 == 0):
#         print("even number is: ",num)

# 8.) Write a Python program to create a list of 5 numbers and print the odd numbers in the list.
# num = []

# num.append(int(input("enter 1st number: ")))
# num.append(int(input("enter 2nd number: ")))
# num.append(int(input("enter 3nd number: ")))
# num.append(int(input("enter 4nd number: ")))
# num.append(int(input("enter 5nd number: ")))

# print("the list of 5 numbers are: ", num)
# for num in num:
#     if (num % 2 != 0 ):
#         print("odd number: ",num)

# 9.) Write a Python program to create a list of 5 numbers and print the numbers that are greater than 10.
# number = [23, 24, 25, 26, 27, 1]
# for number in number:
#     if (number > 10):
#      print(number)

# 10.) Print the last element of a list.
# number = [12, 13, 24, 35, 45]
# print(number[-1])

# 11.) Check whether a given element exists in a list.
# whether = ["winter", "summer", "rainy", "autumn"]
# if "summer" in whether:
#         print("exist in whether")
# else:
#         print("not exist")

# 12.) Add an element to the end of a list.
# student = ["Name: Abhishek"]
# student.append("kumar")
# print(student)

# 13.) Insert an element at a specific position in a list.
# fruits = ["apple", "banana", "mango", "lichi"]
# fruits.insert(2,"graps")
# print(fruits)

# 14.) Create a list of numbers [10, 20, 40, 50] and insert 30 at index 2.
# number = [10, 20, 40, 50]
# number.insert(2, "30")
# print(number)

# 15.) Create a list of student name and insert your name in this list.
# student = ["Lucky", "Atul", "Alok", "Nitish"]
# student.insert(1, "Abhishek")
# print(student)

# 16). Remove an element from a list using remove().
# month = ["january", "february", "march", "april", "may"]
# month.remove("may")
# print(month)

# 17.) Remove the last element using pop().
# fruits = ["apple", "banana", "lichi", "mango", "graps"]
# print(fruits)
# fruits.pop(4)
# print("after pop use", fruits)

# 18.) Clear all elements from a list.
# fruits = ["apple", "banana", "lichi", "mango", "graps"]
# fruits.clear()
# print(fruits)

# Intermediate Level

# 19.) Print all elements of a list using a for loop.
# fruits = ["apple", "banana", "lichi", "mango", "graps"]
# for fruits in fruits:
#     print(fruits)

# 12. Find the maximum element in a list.
# fruits = ["apple", "banana", "lichi", "mango", "graps"]
# print(max(fruits))

# 13. Find the minimum element in a list.
# fruits = ["apple", "banana", "lichi", "mango", "graps"]
# print(min(fruits))

# 14. Find the sum of all elements in a list.
# number = [2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(number))

# 15. Count how many times a given element appears in a list.
# number = [1, 1, 1, 1, 1, 1, 3, 4, 5, 6]
# print(number.count(1))

# 16. Sort a list in ascending order.
# number = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# number.sort()
# print(number)

# 17. Sort a list in descending order.
# number = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# number.sort()
# print(number)
# number.reverse()
# print(number)

# 18. Reverse a list.
# number = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# number.reverse()
# print(number)

# 19. Copy one list into another list.
# number1 = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# number2 = number1.copy()

# print("number1: ",number1)
# print("number2: ", number2)

# 20. Concatenate two lists and print the result.
# number1 = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# number2 = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# result = number1 + number2
# print(result)

# Bonus Practice Questions

# 21. Find the average of all numbers in a list.
# number = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# average = sum(number) / len(number)
# print(average)

# 22. Print only the even numbers from a list.
# number = [3, 2, 5, 4, 6, 9, 7, 8, 1]
# for number in number:
#     if (number % 2 == 0 ):
#         print("even: ",number)

# 23. Print only the odd numbers from a list.
# number = [2, 3, 4, 5, 6, 7, 8, 9]
# for number in number:
#     if (number % 2 != 0):
#         print("odd : ", number)

# 24. Find the second largest element in a list.
# number = [2, 3, 4, 5, 6, 7, 8, 9]
# number.sort()
# print(number[6])

# 25. Remove duplicate elements from a list.
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 4, 4, 5, 6, 6]
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# 26. Convert a tuple into a list.
# numbers = (2, 3, 4, 5, 6, 7, 8, 9, 4, 4, 5, 6, 6)
# print(list(numbers))

# 27. Convert a string into a list of characters.

# 28. Find the index of a given element.
# 29. Replace an element in a list with another value.
# 30. Create a nested list and access an element from the inner list.