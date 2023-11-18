input_num = int(input("Enter number:"))

# #version 1
# if input_num%3 ==0 and input_num%5 ==0:
#     print("Fizz Buzz")
# elif input_num%3 ==0 :
#     print("Fizz")
# elif input_num%5 ==0:
#     print("Buzz")
# else:
#     print("Invalid Input")

# #version 2
# if input_num%3 ==0 :
#     if input_num%5 ==0:
#         print("Fizz Buzz")
#     else:    
#         print("Fizz")
# elif input_num%5 ==0:
#     print("Buzz")    
# else:
#     print("Invalid Input")

# #version 3
flag = None    
if input_num%3 ==0 :
        print("Fizz", end= " ")
        flag = 'Y'
if input_num%5 ==0:
    print("Buzz")
    flag = 'Y'    
if flag is None:
    print("Invalid Input")