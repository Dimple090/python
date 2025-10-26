
        # Initialize the attributes of the parent class
#         super().__init__(building, floor, room)
#         # Initialize additional attributes for College2
#         self.teachers = teachers
#         self.students = students
#         self.fees = fees

#     def full_info(self):
#         # Call show_info method from the College class to print building, floor, and room
#         self.show_info()
#         # Print additional information
#         print(f"Number of Teachers: {self.teachers}")
#         print(f"Number of Students: {self.students}")
#         print(f"Fees: ${self.fees}")


# # # Example
# # college= college2("Main Building", 1,6, 50, 500, 100000)

# # # Printing all information
# # college.full_info()






# # #overriding
# # class A:
# #     def show(self):
# #         print("class A")

# # class B:
# #     def show(self):
# #         super().show()
# #         print("class B")


# #in python oop, an instance is a specific realization of a class ,representing a unique object created from that class .
# #A constructor ,defined  

# #create a database using list and tuple
# # data=[ 
# #     (1,"komal",25,"maths"),
# #     (2,"shubam",23,"english"),
# #     (3,"preety",20,"IT"),
# #     (4,"dimple",21,"science")
 

# # ]

# # def display_data(database):
# #     print("ID   | Name    | Age    Sunject")
# #     print("_______________________________")
# #     for i in database: 
# #         print(f"{i[0]:<3} |{i[1]:<5} |{i[2]:<3} | {i[3]}")


# #to create and a write lines in the file
# #mode = "w" that means write
# # file=open("new_A3","w")
# # file.write("1. This is the file handling in python ")
# # file.close() 
# # #to add new lines in the files
# # file=open("new_A3","a")
# # file.write("2. we are using a mode a so that we can add more lines in the file ")
# # file.write("3.do not forget to add a line separator at the end of the line")
# # file.close()


# # #return those words that start with t,a 
# # file=open("new_A3","r")
# # for i in file.readlines():
# #     for j in startswith("a") or j.startswith("t"): # type: ignore
       

# # #return those words that start with t or a but their length is more than 3
# # file=open("exam","w")
# # file.write("1 this is the Ist line of the file\n")
# # file.close()


# # file=open("exam","r")
# # print(file.read())
# # file.close()

# # file=open("exam","a")
# # file.write("2 this is the 2nd line of the file\n")
# # file.write("3 this is the 3rd line of the file\n")
# # file.close()

# # file=open("exam","r")
# # print(file.read())
# # file.close()

# # file=open("exam","r")
# # print(file.readline()[2])   
# # print(file.readline()[3])
# # file.close()



# # return ist and 2nd line of the file

# file = open ("exam" , "r")
# print(file.readline())
# print(file.readline())
# file.close()

# #return ist and 2nd line of the file
# file=open("test","r")
# f=file.readlines()
# print(f[1])
# print(f[3])
# file.close()



#write a program to convert temperature to and from crlsius to fahrenheit





# file.open("file.csv","w")
# file.write("1,25000,6\n")
# file.write("2,27000,3\n")
# file.write("3,55000,7\n")
# file.write("4,44000,6\n")
# file.close()
# file=open("file.csv","r")
# f=csv.reader(file,delimeters=',')
# l=list(f)
# print(l) 








#update any line,delete any line,update any word,delete any word,replace any word

# file=open("exam","r")
# f=file.readlines()
# f[0]=f[0].replace("handling","handling in the python")
# file=open("exam","w")
# for i in f:
#     file.write(i)
# file.close()
# file=open("exam","r")
# print(file.read())
# file.close()

# #convert first line in uppercase
# # file=open("exam","r")
# # f=file.readlines()
# # f[0]=f[0].upper()
# # file=open("exam","w")
# # for i in f:
# #     file.write(i)
# # file.close()
# # file=open("exam","r")
# # f=file.read()
# # print(f)
# # file.close()



# #convert first word

# file=open("exam","r")
# f=file.readlines()
# file=open("exam","w")
# for i in f:
#     i=i[0:2]+i[2].upper()+i[3:]
#     file.write(i)
# file.close()

# file=open("exam","r")
# print(file.read())
# file.close()


#remove all line no, from the file

# file=open("exam","r")
# f=file.readlines()
# file=open("exam","w")
# for i in f:
#     i=i[2:]
#     file.write(i)
# file.close()

# file=open("exam","r")
# print(file.read())
# file.close()


#add line no
# file=open("exam","r")
# f=file.readlines()
# j=[]
# for i in range(len(f)):
#     file.write(str(i+1)+" "+f[i])
# file.close()

# file=open("exam","r")
# print(file.read())
# file.close()


# #update any word in the line
# file=open("exam","r")
# f=file.readlines()
# for i in f:
#     i=i.replace("file","FILE")
#     print(i)
# file.close()



#delete all file from the next

# file=open("exam","r")
# f=file.readlines()
# for i in f:
#     i=i.replace("file","  ")
#     print(i)
# file.close()



#create a file name it "ds" and write all these statements in that file 

# file=open("ds","r")
# f=file.readlines()
# print(f[3])
# print(f[5])
# file.close()

#print nth row of the file
# file=open("file.csv","r")
# f=csv.reader(file,delimeter=',')
# l=list(f)
# for i in range(len(l)):
#     if i!=1:
#         print(l[i]) 
#file.close()

#remove any row from the files


#add new column where multiply 2nd and 3rd column


# file=open("new_A3","w")


file=open("file.csv","r")
f=csv.reader(file,delimter=',')
l=list(f)
file=open("file1.csv","w")
for i in l:
        q=",".john(l)+"\n"
        file.write(q)
file.close()

file=open("file.csv","r")
f=csv.reader(file,delimter=',')
l=list(f)
print(l)
  