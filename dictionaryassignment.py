# # 1) Create a program named "my_dict_store" which support following operations on 
# # dictionary named "capitals" which would have keys as their country and values as their capitals
# # respectively from the user
# # for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
# # is provided by the user 

# # Operations supported by our program are :
# #     1: Display all elements in the capitals collection
# #     2: Add an element to the capitals collection like --> Afghanistan: Kabul
# #     3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
# #     4: Remove an element from the collection 
# #     5: Take a key from the user and show value if it is present in the dictionary
# #     6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary 	

# # Keep asking the user for the operation in this store untill he chooses to exit from the program
# def dict_display_capitals(capitals): 
#        print(capitals.items())
     
# def dict_add_element(capitals):

#     for i in range(0,1):
#         key=input("Enter key")
#         value=input("Enter value")
#         capitals.update({key:value})
#         print(capitals.items())
        
# def dict_add_elements(capitals):
#     n=int(input("Enter no of values"))
#     for i in range(0,n):
#         key=input("Enter key")
#         value=input("Enter value")
#         capitals.update({key:value})
#         print(capitals.items()) 
        
# def dict_remove_element(capitals):
#      key=input("Enter the element you want to delete")
#      del capitals[key]
#      print(capitals.items())

# def dict_show_value_for_a_key(capitals):
#      key=input("Enter the key you want to search")
#      print(capitals[key])

# def dict_update_or_add_a_key(capitals):
#     key=input("Enter the key you want to search")
    
#     if(key in capitals):
#         print("Key Found")
#         print(capitals[key])
#     else:
#         print("Key not Found hence adding it")
#         value=input("Enter the value you want to add")
#         capitals.update({key:value})

# def my_dict_store():
#     print("\n Welcome to Our Dict Store !!! ")
	
#     capitals={}
#     n=int(input("Enter no of values"))
    
#     for i in range(0,n):
#         key=input("Enter key")
#         value=input("Enter value")
#         capitals.update({key:value})
        
#     """
#         # Write your code here to create the dictionary from the user and reference it with capitals
#     """
    
#     print(capitals)
    
#     while(True):
#         print("\n*************** Menu **********************")
#         print("Operations supported by our program are :")
#         print("    1: Display all elements in the capitals collection")
#         print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
#         print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
#         print("    4: Remove an element from the collection 	")
#         print("    5: Take a key from the user and show value if it is present in the dictionary")
#         print("    6: Take a key from the user update it if it is present in the dictionary or add the key to the dictionary")
#         print("    7: Exit the Program ")
#         choice = int(input("Please enter your choice "))
        
#         if choice   ==1:
#             dict_display_capitals(capitals) 
#         elif choice ==2:
#             dict_add_element(capitals)
#         elif choice ==3:
#             dict_add_elements(capitals)
#         elif choice ==4:
#             dict_remove_element(capitals) 
#         elif choice ==5:
#             dict_show_value_for_a_key(capitals)
#         elif choice ==6:
#             dict_update_or_add_a_key(capitals)
#         elif choice ==7:
#             break
#         else:
#             print("Invalid Input , Please Try Again !!!!  ")

# my_dict_store()

# Exercise 2 : Create a dictionary like this by taking values from the user:
# here the idea is to support a generic dictionary where the values could be of any datatype
# and the keys are strings

# {
# 'employee_id' : 1,
# 'employee_name' : 'Sarwesh'
# 'account_number' : 829389283982839,
# 'salary' : 1000.99999,
# 'address' : {'home_address' : 'Pune' , 'work_address' : 'mumbai'} ,
# 'awards': ['employeeOfTheYear','StarOfTheMonth']
# 'subjects_enrolled' : ('Physics','Chemistry')
# }
# """

def dict_add_integer(gen):
    n=int(input("Enter no of values"))
    for i in range(0,n):
        key=input("Enter key")
        value=int(input("Enter value"))
        gen.update({key:value})
       
def dict_add_string(gen):
    n=int(input("Enter no of values"))
    for i in range(0,n):
        key=input("Enter key")
        value=str(input("Enter value"))
        gen.update({key:value})
    
 
def dict_add_float(gen):
    n=int(input("Enter no of values"))
    for i in range(0,n):
        key=input("Enter key")
        value=float(input("Enter value"))
        gen.update({key:value})
        
def dict_add_dict(gen):
    key=input("Enter key")
    print("Enter new dictionary as a value of key")
    value=my_dict_store()
    gen.update({key:value})
        
def dict_add_list(gen):
    key=input("Enter key")
    value=list(input('Enter new members seperated by comma\n').split(","))
    gen.update({key:value})
    
def dict_add_tuple(gen):
    key=input("Enter key")
    value=tuple(input('Enter new members seperated by comma\n').split(","))
    gen.update({key:value})
 
def display(gen):
    print(gen)   

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")          

    gen = {}
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Add Integer")
        print('    2: Add string')
        print('    3: Add Float')
        print("    4: Add Dictionary")
        print("    5: Add List")
        print("    6: Add Tuple")
        print("    7: Diplay ")
        print("    8: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice ==1:
            dict_add_integer(gen)
        elif choice ==2:
            dict_add_string(gen)
        elif choice ==3:
            dict_add_float(gen)
        elif choice ==4:
            dict_add_dict(gen) 
        elif choice ==5:
            dict_add_list(gen)
        elif choice ==6:
            dict_add_tuple(gen)
        elif choice ==7:
            display(gen)
        elif choice ==8:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")
    return gen
my_dict_store()