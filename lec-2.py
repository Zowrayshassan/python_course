# #Arithmetic operation / comparison & logical operators
# #1-Arithmetic operators are +,-,*,/
# #2-boolean  >,<,==.!=
# #boolean expresssion return true or false i.e, 5==5, 5!=5, 3>5,3<5


# #logical operators

# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) #decimal 3.333
# #--------------------------
# print(a // b) #gives as an integer 3
# print(a % b)  #reminder 3/10 = 1
# print(a ** b) #10power3 1000






# #i want u to calculate the area of circle | and take radius from the user ====> (pie*radius*radius)
# import math
# radius = float(input("Entre the radius:"))

# #logic
# area = math.pi*pow(radius,2)
# print(area)


#relaional operators 


# x=5
# y=6
# print(x==y)  #they give us the boolean results 
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)





# #assignment aperators 
# x=5
# x+=5  #x=x+5 x*=5

# print(x)



# Create a variable score = 50
# Increase score by 20
# # Then divide it by 2
# # Then raise it to the power of 3




# #conditional statements as well:

# #1- if
# #2- if-else
# #3- if-elif-else


# #if ur face is washed 
# #u can eat food 

# #if ur face is washed
#   #if ur hands are washed 
# #then u can eat food



# #check the user , he is eligible for vote or not (ask age and id)
# age = 19
# has_id = True

# if age>18 and has_id:
#     print("Yes,Eligible")   
# else:
#     print("No,Not eligible")
    
    
# #Indentation is very important (spaces)

# #mulitple conditions 
# #of grading a student 

# #1-mulitple conditons
# marks = int(input("Entre your marks:"))
# if marks>90:
#   print("A grade")
# elif marks>80:
#   print("B grade")
# elif marks>70:
#   print("C grade")
# elif marks>60:
#   print("D grade")
# else:
#   print("Fail")
  
# #logical operators
# print("hello world")


# #logical operators
# marks = int(input("Enter your marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade: A")
# elif marks >= 75 and marks < 90:
#     print("Grade: B")
# elif marks >= 50 and marks < 75:
#     print("Grade: C")
# else:
#     print("Fail")
    
    
# #i want u to check that the number user enterd is even or odd 

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


# # 1 2 3 all are integers
# #0.5 0.10 these are floats
# #a,b,c all are strings




# #we have 2 ways to take a value in a variable 

# #1st assigning values 
# name = 'zowrays hassan'
# x=10
# salary = 0.5


# #2nd way taking values from the user 
# name = input("Entre your name: ")
# age = int(input("Entre your age: "))
# salary = float(input("Entre your salary: "))


    
    
# num_1 = int(input("Entre First Number: "))
# num_2 = int(input("Entre Second Number: "))
# num_3 = int(input("Entre Third Number: "))

# if num_1>num_2:
#   if num_1>num_3:
#     print("The largest number is: ", num_1)
#   else:
#     print("The largest number is: ", num_3)
# else:
#   if num_2>num_3:
#     print("The largest number is: ", num_2)
#   else:
#     print("The largest number is: ", num_3)

  


    
grade = input("Entre your grade: ")
attendance = int(input("Entre your attendance ratio % "))

if grade == "A" and attendance >= 90:
    print("You are eligible for the big toy.")
elif grade == "B" and attendance >= 80:
    print("You are eligible for the small toy.")
else:
    print("You are not eligible for any toy.")



