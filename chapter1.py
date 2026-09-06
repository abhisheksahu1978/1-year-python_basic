# mylist = ["abhishek","lucky","atul","nitish"]
# item1 = mylist[0]
# item2 = mylist[1]
# item3 = mylist[2]
# print(item1,item2,item3)
# for y in mylist:
#     print(y)
# if "abhishek" in mylist:
#     print("yes")
# else:
#     print("no")
# print(len(mylist))
# mylist.append("lucky")     #lucky ko sabse piche bhi print karega
# print(mylist)
# mylist.remove("nitish")    #nitish ko remove kar deta hai
# print(mylist)
# mylist.insert(2,"khalu")   #2 index par khalu ko print karta hai
# print(mylist)
# mylist.clear()             #sab element ko hata deta hai
# print(mylist)
# mylist.reverse()           # ulta karke print karta hai
# print(mylist)
# mylist.sort()              # print in accending order
# print(mylist)
# new_list = sorted(mylist)  #accending order
# print(mylist)
# print(new_list)
# mylist = [0]*5             #0 five times print
# print(mylist)
# mylist2 = [1,2,3,4,5]
# new_list = mylist+mylist2
# print(new_list)
# mylist = [13,22,3,43,52,65,7,58,9]
# a = mylist[1:5]            #print index
# print(a)
# mylist=[61,62,63,64,65,66,67,68,69]
# a = mylist[1::2]             #jump by 2 from one index
# print(a)
# list_abhi = ["abhishek","lucky","atul","alok"]
# print(list_abhi)
# mylist = [1,2,3,4,5,6,7]
# a = [i*i for i in mylist]     #i*i means index ki sakhyan se multiply karna 
# print(mylist)
# print(a)

# mytuple = tuple(["music",23,"abhishek"])
# print(mytuple)
# item = mytuple[2]
# print(item)
# for a in mytuple:
#     print(a)
# if "abhishek" in mytuple:
#     print("yes")
# else:
#     print("no")
# mytuple = ('a','b','c','d')
# print(len(mytuple))
# print(mytuple.count('a'))
# print(mytuple.index('c'))
# a = (11,22,33,44,55,66,77,88,99,10)
# b = a[3:8]
# print(b)
# b = a[1::2]
# print(b)
# b = a[::-1]
# print(b)
# mytuple = "abhishek",20,"kumar"
# name,age,lastname = mytuple
# print(name)
# print(age)
# print(lastname)
# a = (0,1,2,3,4,5)
# i1,*i5,i3=a
# print(i1)
# print(i5)
# print(i3)

#Dictionary 
# mydict = {"name": "Abhishek","age":18,"present":"college"}
# gandu = mydict["name"]
# lodu = mydict["age"]
# chomu = mydict["present"]
# print(gandu)
# print(lodu)
# print(chomu)
# mydict = {"name":"abhishek","age":20,"lastname":"kumar","bhosdk":"kisko bola we laude"}
# print(mydict)
# mydict["email"] = "abhi@gmail.com"
# print(mydict)
# mydict["email"] = "abhishekkumar@gmail.com"
# print(mydict)
# if "name" in mydict:
#     print("yes")
# else:
#     print("no")
# del mydict["name"]        #delete item whose written
# print(mydict)
# mydict.pop("age")         #remove this item whose written
# print(mydict)
# mydict.popitem()          #remove last item
# print(mydict)
# try:                       #agar sahi likha item mil gaya upar se toh print hoga warna nahi
#     print(mydict["lalu"])
# except:                    #agar try loop nahi chala to except chalega
#     print("Bosdk sahi se likh, Lodu")
# for keys in mydict.keys():
#     print(keys)
# for value in mydict.values():
#     print(value)
# for keys, values in mydict.items():
#     print(keys,":",values)
# mydict_copy = mydict
# mydict_copy["email"]= "abhi@gmail.com"
# print(mydict_copy)
# mydict = {"name":"abhishek","age":20,"lastname":"kumar","bhosdk":"kisko bola we laude"}
# mydict2 = dict(name="abhishek",age=21,lastname="kumar")
# mydict.update(mydict2)
# print(mydict)
# numbers = [10,20,30,40]
# print(numbers.remove(10))
# print(numbers)
# print(numbers.pop(1))
# print(numbers)
# numbers=[4,5,2,1,3,6,9]
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(len(numbers))
# d={"name":"abhishek","age":20,"lastname":"kumar",}
# print(d["name"])
# d["age"]=21
# print(d)
# d["city"]="indore"
# print(d)
# del d["lastname"]
# print(d)
# print(d.pop("age"))
# print(d.keys())
# print(d.values())
# print(d.items())
# d={("name","roll"):("abhishek",21),"age":20}
# print(d)
# def pythonclass():
#     print("this is a function")

# pythonclass()
# def votingtest():
#     age=int(input("enter your age:"))

# function with parameter without return
# def function_name(parameter1, parameter2):
#     print("hello",parameter1,"and",parameter2)
# function_name("abhishek", "lucky")
# def add(a,b):
#     print("the first number is ",a,"and the second number is ",b)
#     return a+b
# result = add(10,20)
# print("the sum is",result)
# # using value returned by function
# print("*******")
# c=add(3,2)
# print(c)

# advanced function
# lambda arguments:expression
# add=lambda a,b:a+b
# print(add(4,5))
# square=lambda a:a*a
# square=lambda a:a**2
# print(square(5))

# creating a decorator

# def my_decorator(func):
#     def wrapper():
#         print("User login details")
#         func()
#         print("User login details end")
#     return wrapper
# # main function with decorator

# @my_decorator
# def says_hello():
#     print("hello")
# # Cslling main function with decorator
# says_hello()

# Advanced function:
# def demo(*args, **kwargs):
#     print("Args:",args)
#     print("Kwargs:",kwargs)
# demo(1,2,3,4,5,6, name="Abhishek", age=20, city="Indore")