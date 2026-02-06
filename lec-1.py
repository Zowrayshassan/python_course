#human do communicate in thier native language for that they have grammer rules 


#likewise programming also have some rules



# #1-variables
# #anything that can store value in a memory block (RAM)


# a=10
# #here a is a variable which is storing value 10


# #print is used in python to display something on the screen
# print(a)


# #sum of 2 variables
# # a=10
# # b=20
# # print(a+b)
# # c = a+b
# # print(c)





# #========day 2========
# #comments

# #add 2 number

# #multicomments
# """
# age = 10
# print(age)
# print(age+10)
# """


# #variables and thier datatype 

# a=10 #integer type data
# b =10.5 #float type data
# name = "hassan" #string
# is_married = True #boolean   either true or false 


# #take a name in a variable and age in a variable and print a message hi name your age is this 

# #strings shows the character and exact charcater  and u can decalre anything as a string
# a = "10"
# b = "20"
# print(a+b)




# #There is a rule to declare variables

# #1-always use meaning full words
# #2- always use underscore or never give spaces 
# student_marks = 10
# #3-never start your variable with the capital letter
# name=10
# #4-never start your variable with the number 
# #1_name throw an error


# #3 different format 
# #1-underscore    full_name
# #2-camel case    fullName,  studentMarks
# #3-pascal case   FullName, StudentMarks





# #INPUTS

# #i wanna ask a name from user in which he/she live 
# city  = input("what is your city? ")

    
# #sum via input

# #input function by default reutrn us strings to convert we need to define
# first_number = int(input("Entre First Number: "))
# second_number = int(input("Entre Second Number: "))
# sum = first_number + second_number
# print('The sum is: ', sum)

# #string concatination is basically we can add  strings
# first_name="10"
# last_name = '20'
# print("My name is " + first_name + last_name)









#i am solving problem no.3 
#hey salou i am gonna teach u inputs in python 



number = int(input("Entre a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")

else:
    print("The number is zero")