# # 1) Write a program that creates a dictionary like this 
# # {
# #     1: "red" , 2: "Blue" , 3: "Orange"
# # }
# # Now take the key as input from the user and print its corresponding colour 
# # (Exception handle the code to terminate gracefully by printing 
# # Colour not found if the key doesnot exists )

# gen = {}
# n=int(input("Enter no of values"))
# for i in range(0,n):
#     key=input("Enter key")
#     value=(input("Enter value"))
#     gen.update({key:value})

# while True:
    
#     k=input("Enter key to search")
    
#     try:
#         print("Colour Found",gen[k])
#         break
        
#     except:
#         print("Colour not found")
#         break
        
        
# # 2) Write a program that creates a list of 5 elements of your choice 
# # Now take the index that the user want the data of and print the value at that 
# # location 
# # Exception handle the code to  terminate gracefully by printing 
# # Value not found if the index doesnot exists 

# gen=[]
# gen=list(input('Enter elements seperated by comma\n').split(","))

# while True:
#     i=int(input("Enter Index to search"))
#     try:
#         print("Value found",gen[i])
#         break
        
#     except:
#         print("Value not Found")
#         break
    


# # 3) Create program that takes age of the user as input 
# # and prints number of days that user has lived for 
# # Exception handle the code such that if the user has lived for more than 
# # 100001 days then user should get the message
# # , you lived for so long , may be you will die soon:)

# class my_exception(Exception):
#     pass

# a=int(input("Enter your age"))
# days=a*365

# try:
#     if days>100001:
#         raise my_exception
    
#     else:
#         print("You have lived for",days,"days")
        
# except my_exception:
#     print("you lived for so long , may be you will die soon:")

# 4)Create the following program named "my_exception_store" with the menu below :

# Welcome User , What would you like to do today ?
#     1) Create a postive numbered list 
#     Note : raise an exception if the users inserts a negative number OR user creates an empty list 
#     2) Create a negative  numbered list 
#     Note : raise an exception if the users inserts a positive number/Zero OR user creates an empty list
#     3) Create a heterogenous list 
#     Note : raise an exception if the users creates a homogenous list (all elements of same datatype)
#     4) Refresh the program to start with blank lists
#     5) Exit

# Handle exceptions in the script for all operations 
# and let the user continue till he chooses to exit from the program 

    

class positive_number_error(Exception):
    pass

class negative_number_error(Exception):
    pass

class homogenous_number_error(Exception):
    pass

def input_val():
    print("choose data type of element you want to enter")
    print("1.for intger data type")
    print("2.for float data type")
    print("3.for string data type")
    print("4.for tuple data type")
    
    ch = int(input("Enter your choice:"))
    if ch==1:
        return int(input("Enter integer value:"))
    elif ch==2:
        return float(input("Enter float value:"))
    elif ch==3:
        return str(input("Enter string value:"))
    elif ch==4:
        return tuple(input("Enter tuple value seperated by comma:").split(","))
    else:
        print("Invalid Input")
    



def create_postive_numbered_list(my_int_list1):
    n=int(input('Enter no of elements \n'))
    for i in range(0,n):
        a=int(input('Enter Integers \n'))
        if a<0:
            raise negative_number_error
        else:
            my_int_list1.append(a)
        print(my_int_list1)
        

def create_negative_numbered_list(my_int_list2):
    n=int(input('Enter no of elements \n'))
    for i in range(0,n):
        a=int(input('Enter no of elements \n'))
        if a>0:
            raise positive_number_error
        else:
            my_int_list2.append(a)
        print(my_int_list2)
            
def create_hetrogenous_numbered_list(my_het_list3):
    n=int(input('Enter no of elements \n'))
    for i in range(0,n):
        flag=True
        a=input_val()
        for i in range(0,len(my_het_list3)):
            if type(a) == type(my_het_list3):
                flag=False
        
        if flag==False:
            raise homogenous_number_error
        else:
            my_het_list3.append(a)
        print(my_het_list3)
        
            
        
def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]
    
    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_postive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_hetrogenous_numbered_list(my_het_list3)
            elif choice ==4:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==5:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_number_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()   