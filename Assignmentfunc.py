# # Assignment 1
# def my_function(num1,num2):
#     print("addition =",num1+num2)
#     print("square of first no is",num1*num1)
#     print("the first power to second number",num1**num2)
#     return num1**num2
# num1,num2= int(input("enter the first no")),int(input("enter the second no"))
# (my_function(num1,num2))

# Assignment 2
# def upper_function(str1):
#     print(str1.upper())
#     return str1.upper()
# str1=str(input("Enter your string"))
# upper_function(str1)

# # Assignment 3
# raise_salary_percentage=int(input("Enter salary percentage"))
# name = "gaurav"
# existing_salary=900
# def salary_fuction(existing_salary,raise_salary_percentage):
#     incremented_salary=(existing_salary)+(existing_salary*raise_salary_percentage/100)
#     return incremented_salary
# print(salary_fuction(existing_salary,raise_salary_percentage))

# # Assignment 4
# height=(int(input("Enter height in cms")))
# def calc_height(height):
#     feet=height*1/30.48
#     inch=height*1/2.54
#     print("height in feet = ", feet,"Height in inch = ",inch)
# calc_height(height)

# # Assignment 5
# dollar=(int(input("Enter dollars")))
# def calc_dollar(dollar):
#     rupees=dollar*82
#     return rupees
# rupees=calc_dollar(dollar)
# print(rupees)

# # Assignment 6
# source = input("Pleased enter the source ")
# destination = input("Pleased enter the destination ")
# fare = float(input("Pleased enter the fare "))
# discount_rate = float(input("Pleased enter the discount_rate in percentage "))
# def calc_ride(source,destination,fare,discount_rate):
#     print("Fare from" , source ," to " , destination , " is " , fare- (fare*discount_rate/100)  , " INR with has a applied discount of " , discount_rate, "%")
# calc_ride(source,destination,fare,discount_rate)