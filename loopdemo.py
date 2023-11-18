# Version 1
ch="Y"
while True:
    input_num = int(input("Enter number:"))
    if input_num%3 ==0 :
        if input_num%5 ==0:
            print("Fizz Buzz")
        else:    
            print("Fizz")
    elif input_num%5 ==0:
        print("Buzz")    
    else:
        print("Invalid Input")
    ch=input("Play Again y/n?")
    if ch=="y" or ch=="Y":
        continue
    elif ch=="n" or ch=="N":
        break
    else:
        print("Enter valid coice")
        continue


# # Version 2
# def my_fizz_buzz():
#    input_num = int(input("Enter number:"))
#    flag = None    
#    if input_num%3 ==0 :
#          print("Fizz", end= " ")
#          flag = 'Y'
#    if input_num%5 ==0:
#       print("Buzz")
#       flag = 'Y'    
#    if flag is None:
#       print("Invalid Input")

# while True:
#    my_fizz_buzz()
#    skip_char= input("\nPlease press ~ to skip ")
#    if skip_char == '~':
#       break