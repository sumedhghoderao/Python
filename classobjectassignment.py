# ##Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# main
# 1) create an object employee(100,1000,1)  
# 2) do the following for the created object
# // direct access using .notation
# empid
# emp_salary
# mgr_id
# 3) print the department name 
# 4) display the expertise for the employees 
# 5) Deleting Attributes and Objects

# class Employee:
    
    
#     def __init__(self,emp_id,emp_salary,mgr_id):
#         self.emp_id=emp_id
#         self.__emp_salary=emp_salary
#         self.mgr_id =mgr_id
        
#     def get_emp_salary(self):
#         return self.__emp_salary
#     def set_emp_salary(self,sal):
#         self.__emp_salary=sal
    
    
#     department_name = "Production"
    
#     @classmethod
#     def get_department_name(cls):
#         return cls.department_name
    
#     @staticmethod
#     def field_expertise():
#         print("employees are expert in their field")
        
# def main():
#     Akshay=Employee(1,10000,100)
#     print(Akshay.emp_id)
#     print(Akshay.get_emp_salary())
#     print(Akshay.mgr_id)
    

#     while True:
#         choice = int(input("\n\nEnter your choice \n1-Print Department Name \n2-Display Expertise of Employees \n3-Delete attribute and object \n4-Exit \n"))

#         if choice==1:
#             print(Employee.get_department_name())
      
#         elif choice==2:
#             Employee.field_expertise()
       
#         elif choice==3:
#             del Akshay.emp_id
#             print("Employee Attribute has been deleted")
#             del Akshay
            
#         else:
#             break
# main()        

            
            
# #     Exercise 02 : Classes and objects -- try creating this in oops world
# -------------------------------------------
 
# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details        
        
class Airline_ticket:
    
    
    def __init__(self,departure,arrival,flight_num,seat_assign):
        self.departure=departure
        self.arrival=arrival
        self.flight_num=flight_num
        self.seat=seat_assign
        
    def display(self):
        print("Flight number : ",self.flight_num)
        print("Departure location : ",self.departure)
        print("Arrival Location : ",self.arrival)
        print("Seat Allocated : ",self.seat)
        
def main():
    while True:
        flight_num={23434,45345,49877,12323,56575}
        seat={"10E","45A","30B","15C","32D"}
        print("1.Enter new ticket : ")
        print("2.Display bookings : ")
        print("3.Exit : ")
        ch=int(input("Enter Your Choice :\n"))
        if ch==1:
            print("Enter First ticket: ")
            dep=input("Enter Departure Location: \n")
            arr=input("Enter Arrival Location: \n")
            obj1=Airline_ticket(dep,arr,flight_num.pop(),seat.pop())
            print("Enter Second ticket: \n")
            dep=input("Enter Departure Location: \n")
            arr=input("Enter Arrival Location: \n")
            obj2=Airline_ticket(dep,arr,flight_num.pop(),seat.pop())
        elif ch==2:
            print("\n")
            try:
                obj1.display()
                print("\n")
                obj2.display()
            except:
                print("Ticket Not Booked")
        else:
            break
main()
    
    
        
        