def addition(first_num, second_num):
    return first_num+second_num

def multiplication(first_num, second_num):
    return first_num*second_num


# addition_lambda = lambda first_num, second_num : first_num+second_num
# multiplication_lambda = lambda first_num, second_num : first_num*second_num

# print(addition(1,2))
# print(addition_lambda(1,2))

# print(multiplication(1,2))
# print(multiplication_lambda(1,2))


# -------------------------
def my_calculator():
    
    print("1: Addition \n 2: Multiplication")
    choice = int(input("Please enter choice"))
    
    num1= int(input("Number1:"))
    num2= int(input("Number2:"))

    if choice ==1 :
        print("addition:",addition(num1,num2))
    else:
        print("multiplication",multiplication(num1,num2))

# my_calculator()        

#-----
def my_hof(function_to_execute,parameter1,parameter2):
    return function_to_execute(parameter1,parameter2)
    
def my_calculator_lamdba():
    print("1: Addition \n 2: Multiplication")
    choice = int(input("Please enter choice"))
    
    num1= int(input("Number1:"))
    num2= int(input("Number2:"))

    if choice ==1 :
        print("addition:",my_hof(lambda rcv_num1,rcv_num2 : rcv_num1+rcv_num2 , num1,num2))
    else:
        print("multiplication",my_hof(lambda rcv_num1,rcv_num2 : rcv_num1*rcv_num2 , num1,num2))

# my_calculator_lamdba()       


# *****************
def addition_nargs(*args):
    sum=0
    for val in args:
        sum += val
    return sum

# print(addition_nargs(1,2,3))

# addition_nargs_lamdba =   lambda *args:  sum(args)
# print(addition_nargs_lamdba(1,2,3))

def addition_nkeyword_args(**kwargs):
    sum=0
    for val in kwargs.values():
        sum += val
    return sum
print(addition_nkeyword_args(first_num = 1,second_num= 2,third_num= 3))    