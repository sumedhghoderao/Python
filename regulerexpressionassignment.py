import re
string0 = "gaurav1234@gmail.com"
string1 = "pratik190900234@gmail.com"
string2 = "2009_rocking_person@yahoo.com"
string3 = "GodFather2022@yahoo.com"
string4 = "Brocklesner_89_WWE@yahoo.com"
string5 = "TheRock_WWE@yahoo.com"
string6 = "JohnCena_WWE@yahoo.com"
string7 = "Undertaker_Roman_reigns@outlook.com"
string8 = "6789764666@rediffmail.com"
string9 = "Kane#6789@gmail.com"

my_list = [string0,string1,string2,string3,string4,string5,string6,string7,string8,string9]
   
#1) provide me the list of emails that do have special characters of #~`!
for test_string in my_list:
    search_obj = re.search(r"[#~`!]", test_string)  
    if search_obj is not None :
     print(f"{test_string} resulted into {search_obj}")  
   

#2) provide me the list of emails that start with numbers
for test_string in my_list:
    search_obj = re.search(r"^[0-9]", test_string)  
    if search_obj is not None :
     print(f"{test_string} resulted into {search_obj}")


#3) provide me the list of emails that start with numbers followed by an underscore
for test_string in my_list:
   search_obj = re.search(r"^\d+_", test_string)  
   if search_obj is not None :
    print(f"{test_string} resulted into {search_obj}")

#4) provide me the list of emails that start with numbers followed by an underscore or small case characters
for test_string in my_list:
    search_obj = re.search(r"^[0-9]+[_a-z]", test_string)  
    if search_obj is not None :
      print(f"{test_string} resulted into {search_obj}")
        
#5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
for test_string in my_list:
   search_obj = re.search(r"^[0-9]+[_a-zA-Z]", test_string)  
   if search_obj is not None :
    print(f"{test_string} resulted into {search_obj}")
        
#6) Provide me list of emails with only numbers before the @
for test_string in my_list:
    search_obj = re.search(r"^[0-9]+@", test_string)  
    if search_obj is not None :
     print(f"{test_string} resulted into {search_obj}")
        
        
#7) Provide me list of emails with numbers anywhere before the @
for test_string in my_list:
    search_obj = re.search(r"^[0-9]+@.*", test_string)  
    if search_obj is not None :
     print(f"{test_string} resulted into {search_obj}")