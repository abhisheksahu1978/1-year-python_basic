# diamond shape
# n=10
# print()
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))

#STEP 1ST: Create and open file
#Creating a file and writing initial student data

# file=open("students_detailss.txt","w")
# file.write("101, Adil, 90\n")
# file.write("102, Ramu, 85\n")
# file.write("103, Jyotish, 92\n")
# file.close()
# '''
# #STEP 2: Search Student
# '''
# search_id="102"
# found=False
# file=open("students_detailss.txt","r")
# for line in file:
#     data=line.strip().split(",")    #strip():- removes leading and trailing whitespace unwanted line, split(",") splits the line into a list using comma as a delimiter
#     if data[0]==search_id:
#         print("Student Found:",line)
#         found=True
# file.close()

# #Step 3: Delete Operation
# delete_id = "101"
# file=open("students_detailss.txt","r")
# lines=file.readlines()
# file.close()

# file=open("students_detailss.txt","w")
# for line in lines:
#     data=line.strip().split(",")
#     if data[0]!=delete_id:
#         file.write(line)
# file.close()
# print("Student record deleted successfully!")

# #Step 4: Update Operation:
# update_id="103"
# new_data="103, Nishant, 99\n"
# file=open("students_detailss.txt","r")
# lines=file.readlines()
# file.close()

# file=open("students_detailss.txt","w")
# for line in lines:
#     data=line.strip().split(",")
#     if data[0]==update_id:
#         file.write(new_data)
#     else:
#         file.write(line)
# file.close()
# print("student record updated successfully!")

# read file line by line
# file=open("students_detailss.txt","r")
# print("\n Reading file line by line:")
# for line in file:
#     print(line.strip())
# file.close()

# remove line containing 'n'
# input_file=open("students_detailss.txt","r")
# output_file=open("filetered.txt","w")
# for line in input_file:
#     if 'n' not in line:
#         output_file.write(line)
# input_file.close()
# output_file.close()
# print("\n Filtered file created successfully! (no 'n' lines)")
# print("------------------------")

# file=open("students_detailss.txt","r")
# print("\n Reading file line by line:")
# for line in file:
#     print(line.strip())
# file.close() 