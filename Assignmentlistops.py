# Exercises 
# Topics covered : Modules,Functions,Looping,Conditional constructs,Input,Output,Collections :
# ---------------------------------------------------------------------------------------------------------
# 1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user 
# for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] is provided by the user 

# Operations supported by our program are :
#   1:  Display number of elements in the members list
#   2:  Add an element to the members collection like 'Sehwag' 
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection 
#   6:  Display third, fourth and fifth element from the collection 

# Keep asking the user for the operation in this store untill he chooses to exit from the program


# def list_display_members(members) :
# 	print(len(members))

# def list_add_element(members) :
#     a=input("Enter new member")
#     members.append(a)
#     print(members)

# def list_add_elements(members):
#     a=input('Enter new members seperated by comma\n').split(",")
#     members.extend(a)
#     print(members)

# def list_remove_element(members) :
#     a=int(input("Enter member index to remove"))
#     del members[a] 
#     print(members)

# def remove_last_element(members) :
# 	members.pop()
   
# def display_3_4_5_element(members):
# 	print(members[3:6])

# def my_list_store():
#     print("\n Welcome to Our List Store !!! ")
#     print("Please enter a list Comma seperated that you would want to perform Operation Upon")
#     members = input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n').split(",")

#     while(True):
#         print("\n*************** Menu **********************")
#         print("Operations supported by our program are :")
#         print("  1:  Display number of elements in the members list")
#         print("  2:  Add an element to the members collection like 'Sehwag' ")
#         print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
#         print("  4:  Remove a member from the collection at a given subscript")
#         print("  5:  Remove the last member from the collection ")
#         print("  6:  Display third, fourth and fifth element from the collection ")
#         print("  7: Exit the Program ")
#         choice = int(input("Please enter your choice "))
        
#         if choice   ==1:
#             list_display_members(members) 
#         elif choice ==2:
#             list_add_element(members) 
#         elif choice ==3:
#             list_add_elements(members)
#         elif choice ==4:
#             list_remove_element(members) 
#         elif choice ==5:
#             remove_last_element(members) 
#         elif choice ==6:
#             display_3_4_5_element(members) 
#         elif choice ==7:
#             break
#         else:
#             print("Invalid Input , Please Try Again !!!!  ")

# my_list_store()			

# #2) Create My tuple store with following operations
# def tuple_display_members(members) :
# 	print(members)

# def display_3_4_5_element(members) :
# 	print(members[3:6])

# def tuple_retrieve_element(members):
#     a=int(input("Enter member index to retrive"))
#     print(members[a])

# def tuple_retrieve_elements(members) :
#     start=int(input("Enter start index"))
#     stop=int(input("Enter start index"))
#     print(members[start:stop])

# def find_min_element(members) :
# 	print(min(members))

# def reverse_tuple(members):
# 	print(members[::-1])

			
# def my_tuple_store():
#     print("\n Welcome to Our tuple Store !!! ")
#     print("Please enter a tuple Comma seperated that you would want to perform Operation Upon")
#     members = tuple(input('for ex: Pratiksha,Kevin,Sachin,Yuvraj,Sania \n').split(","))

#     while(True):
#         print("\n*************** Menu **********************")
#         print("Operations supported by our program are :")
#         print("  1:  Display elements of the tuple")
#         print("  2:  Display third, fourth and fifth element from the collection ")
#         print("  3:  Retrieve element at a given subscript")
#         print("  4:  Retrieve elements from a given subscript and to a given subscript")
#         print("  5:	 Find minimum element in the tuple " )
#         print("  6:	 Reverse elements in the tuple " )
#         print("  7:  Exit the Program ")
#         choice = int(input("Please enter your choice "))
        
#         if choice   ==1:
#             tuple_display_members(members) 
#         elif choice ==2:
#             display_3_4_5_element(members) 
#         elif choice ==3:
#             tuple_retrieve_element(members)
#         elif choice ==4:
#             tuple_retrieve_elements(members) 
#         elif choice ==5:
#             find_min_element(members) 
#         elif choice ==6:
#             reverse_tuple(members) 
#         elif choice ==7:
#             break
#         else:
#             print("Invalid Input , Please Try Again !!!!  ")

# my_tuple_store()			

# #3) Create my string store with following operations

def string_display(string_input) :
    print(string_input) 

def display_3_4_5_element(string_input) :
    print(string_input[3:6])

def string_retrieve_element(string_input):
    a=int(input("Enter member index to retrive"))
    print(string_input[a]) 

def string_retrieve_elements(string_input) :
    start=int(input("Enter start index"))
    stop=int(input("Enter start index"))
    print(string_input[start:stop])

def find_min_element(string_input) :
    print(min(string_input))

def reverse_string(string_input) :
    print(string_input[::-1])

def  find_each_character_count(string_input):
    for i in string_input:
        cnt=string_input.count(i)
        print("Count of ",i, "is" ,cnt)
        cnt=0
     
def  find_character_count_greater_than_1(string_input):
     for i in string_input:
        cnt=string_input.count(i)
        if cnt>1:
            print("Count of ",i,"is",cnt)

def  check_palindrome(string_input):
     pali= string_input[::-1]
     if pali==string_input:
        print("Given String is Palidrom")
     else:
         print("Given string is not palidrom")
             
def my_string_store():
    print("\n Welcome to Our string Store !!! ")
    string_input = input("Please enter a string that you would want to perform Operation Upon").strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print( " 1:Display the string")
        print( " 2:Display third, fourth and fifth element from the string ")
        print( " 3:Retrieve element at a given subscript")
        print( " 4:Retrieve elements from a given subscript and to a given subscript")
        print( " 5:Find minimum character in the string " )
        print( " 6:Reverse the string " )
        print( " 7:Output list of tuple( character,count) for each characters of the string  " )
        print( " 8:Output list of characters of the string that appear more than once " )
        print( " 9:Check if the string is a palindrome and return output message accordingly")
        print( " 10: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            string_display(string_input) 
        elif choice ==2:
            display_3_4_5_element(string_input) 
        elif choice ==3:
            string_retrieve_element(string_input)
        elif choice ==4:
            string_retrieve_elements(string_input) 
        elif choice ==5:
            find_min_element(string_input) 
        elif choice ==6:
            reverse_string(string_input) 
        elif choice ==7:
             find_each_character_count(string_input)
        elif choice ==8:
             find_character_count_greater_than_1(string_input)
        elif choice ==9:
             check_palindrome(string_input)
        elif choice ==10:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_string_store()