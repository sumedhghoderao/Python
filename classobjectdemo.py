# class Student:
#     """ This is doc string for Student class """
#     # class variable
#     school_name = "CDAC"    
    
#     # initialiser
#     def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
#         # instance variable
#         self.student_name = rcv_name      # public instance variable 
#         self.student_rollno = rcv_rollno   # public instance variable 
#         self.student_pocket_money = rcv_pocket_money # public instance variable 
#         self.student_enrolled_coursename = rcv_course # public instance variable 
#         print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

#     # instance method
#     def get_enrolled_course(self):
#         return self.student_enrolled_coursename

#     # instance method
#     def get_student_pocket_money(self):
#         return self.student_pocket_money
    
#     # instance method
#     def enroll(self,rcv_course_name):
#         self.student_enrolled_coursename = rcv_course_name

#     # instance method
#     def unenroll(self):
#         self.student_enrolled_coursename = None

#     # class method
#     @classmethod
#     def change_schoolname(cls,rcv_schoolname):
#         cls.school_name = rcv_schoolname
    
#     # static method
#     @staticmethod
#     def display_facilities_available():
#         print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
       
# # main method which is outside the class 
# def main():
#     print("I am in main and I am not part of the class ")

#     # create a Student object referenced by gaurav
#     gaurav= Student("Gaurav",1,100,'Python')
#     duplicate_gaurav= Student("Gaurav",1,100,'Scala')
    
#     # access the public instance variable for gaurav referenced object directly 
#     print("Before setting the public variable : ",gaurav.student_pocket_money) 
#     # set the public variable outside the class 
#     gaurav.student_pocket_money = 9999999
#     print("After setting the public variable : ", gaurav.student_pocket_money) 
    
#     # invoke a instance method(getter) for gaurav referenced object to access an attribute of the class 
#     print(gaurav.get_student_pocket_money())
    
#     print("Before Unenroll call ", gaurav.get_enrolled_course())
#     # invoke a instance method(setter) for gaurav referenced object to set an attribute of the class 
#     gaurav.unenroll()
#     print("After Unenroll call ", gaurav.get_enrolled_course())
#     # invoke a instance method for gaurav referenced object 
#     gaurav.enroll("Scala")
#     print("After Enroll call ", gaurav.get_enrolled_course())

#     # create another Student object referenced by pratik
#     pratik= Student("Pratik",2,200,'Java')
 
#     # trying to change the class variable using the Class reference 
#     # print the class variable using each of the available references 
#     print("School name at Class level was",Student.school_name)
#     print("Gaurav School name was",gaurav.school_name)
#     print("Pratik School name was",pratik.school_name)
    
#     # invoke class method(setter) using Student class reference
#     Student.change_schoolname("Sunbeam")

#     # print the class variable 
#     print("School name at Class level is",Student.school_name)
#     print("Gaurav School name is",gaurav.school_name)
#     print("Pratik School name is",pratik.school_name)

#     # trying to change the class variable using the instance reference gaurav but via a class method
#     # print the class variable using each of the available references 
#     print("School name at Class level was",Student.school_name)
#     print("Gaurav School name was",gaurav.school_name)
#     print("Pratik School name was",pratik.school_name)

#     # invoke class method(setter) using gaurav instance variable reference
#     gaurav.change_schoolname("Sunbeam")

#     # print the class variable 
#     print("School name at Class level is",Student.school_name)
#     print("Gaurav School name is",gaurav.school_name)
#     print("Pratik School name is",pratik.school_name)

#     # trying to change the class variable using the instance reference gaurav's . notation
#     # print the class variable 
#     print("School name at Class level was",Student.school_name)
#     print("Gaurav School name was",gaurav.school_name)
#     print("Pratik School name was",pratik.school_name)
#     # invoke class method using gaurav reference 
    
#     gaurav.school_name = "Sunbeam" # this will create a new instance variable for gaurav instance 

#     # print the class variable 
#     print("School name at Class level is",Student.school_name)
#     print("Gaurav School name is",gaurav.school_name)
#     print("Pratik School name is",pratik.school_name)    

    
#     # invoke the static method 
#     Student.display_facilities_available()
#     gaurav.display_facilities_available()
#     pratik.display_facilities_available()
#     #display_facilities_available() # doesnot work 
    
#     # # Deleting Attributes student_pocket_money
#     print(gaurav.student_pocket_money)
    
#     # AttributeError: 'Student' object has no attribute 'student_pocket_money'
#     del gaurav.student_pocket_money 
#     # print(gaurav.student_pocket_money)
#     print(pratik.student_pocket_money)
    
    
#     """  Deleting entire object gaurav
#     The destructor was called after the program ended or when all the references to object are #deleted i.e when the reference count becomes zero, not when object went out of scope.
#     """
#     # UnboundLocalError: local variable 'gaurav' referenced before assignment
#     del gaurav
#     print(gaurav.student_pocket_money)
      
#     # miscellnous functions for the class 
#     # list all that the Student Class contains 
#     print(dir(Student))
#     print(Student.__doc__)

# # invoke the main function 
# main()

#     # print("Before",Student.school_name)
#     # print("Before",gaurav.school_name)

#     # # del Student.school_name
#     # # print("after",Student.school_name)
#     # # print("After",gaurav.school_name)

#     # new_obj = Student("test",100,1000,"test")    
#     # print("after",new_obj.school_name)



# demo 2
class Student:
    """ This is doc string for Student class """
    # class variable
    school_name = "CDAC"    
    
    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
        # instance variable
        self.student_name = rcv_name      # public instance variable 
        self.student_rollno = rcv_rollno   # public instance variable 
        self.__student_pocket_money = rcv_pocket_money # private instance variable 
        self._student_enrolled_coursename = rcv_course # public instance variable 
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

    # instance method
    def get_enrolled_course(self):
        return self.student_enrolled_coursename

    # instance method
    def get_student_pocket_money(self):
        return self.student_pocket_money
    
    # instance method
    def enroll(self,rcv_course_name):
        self.student_enrolled_coursename = rcv_course_name

    # instance method
    def unenroll(self):
        self.student_enrolled_coursename = None

    # class method
    @classmethod
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname
    
    # static method
    @staticmethod
    def display_facilities_available():
        print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
     
     # Operator Overloading -- implemented this to support greater than operation for Student class 
    def __gt__(self,other_obj):
        return self.student_rollno > other_obj.student_rollno    
    
    # Operator Overloading -- implemented this to support Equal to operation for Student class 
    def __eq__(self,other_obj):
       return (self.student_name == other_obj.student_name  and 
               self.student_rollno == other_obj.student_rollno and
               self.__student_pocket_money == other_obj.__student_pocket_money and
               self._student_enrolled_coursename == other_obj._student_enrolled_coursename)
          
# main method which is outside the class 
def main():
    print("I am in main and I am not part of the class ")

    # create a Student object referenced by gaurav
    gaurav= Student("Gaurav",1,100,'Python')
    # create another Student object referenced by pratik
    pratik= Student("Pratik",2,200,'Java')
    
    # create a Student object referenced by gaurav_copy
    gaurav_copy= Student("Gaurav",1,100,'Python')
    
    
    # print("Private attribute :", gaurav.__student_pocket_money)
    print("Private attribute :", gaurav._Student__student_pocket_money)
    print("Protected attribute" , gaurav._student_enrolled_coursename)
    
    
    if gaurav > pratik:
        print("Gaurav rollno: {gaurav.student_rollno} is greater than that of Pratik")
    else:
        print(f"Pratik rollno: {pratik.student_rollno} is greater than that of Gaurav")    
    
    if gaurav == gaurav_copy:
        print("both objects have same contents ")

# invoke the main function 
main()