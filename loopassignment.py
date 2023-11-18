# # Assignment 1
# def my_calculator(num1,num2):
#     ch=str(input("Enter your opperation: "))
#     if ch=="+":
#         print("addition =",num1+num2)
#     elif ch=="*":    
#         print("square of first no is",num1*num1)
#     elif ch=="**":
#         print("the first power to second number",num1**num2)
#     else:
#         print("Enter Valid Choice")
    
# while True:
#     num1,num2= int(input("enter the first no")),int(input("enter the second no"))
#     (my_calculator(num1,num2))
#     skip = input("\npress ~ to skip ")
#     if skip == '~':
#        break

# Assignment 2
def my_addition(num):
    print("The addition upto first number is: ",end= "")
    sum=0
    while num>0:
        sum=sum+num
        num=num-1
    print(sum)

def my_odd(num):
    i=0
    print("The odd numbers upto number is: ")
    while i<=num:
        if i%2 != 0:
            print(i)    
        i=i+1

def my_even(num):
    i=0
    print("The even numbers upto number is: ")
    while i<=num:
        if i%2 == 0:
            print(i)    
        i=i+1
    
num = int(input("Please enter number:")) 
while True:
            ch=str(input("Enter your choice \n1.Addition \n2.Odd numbers \n3.Even numbers \n4.exit "))
                
            if ch=="1":       
                my_addition(num)
                continue
            elif ch=="2":
                my_odd(num)
                continue
            elif ch=="3":
                my_even(num)
                continue
            else:
                break