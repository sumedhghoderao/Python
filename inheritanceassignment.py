# # -------------------------
# # Exercise on Inheritance:
# # -------------------------
# # Create a base class named Employee as follows:
# # Employee (
# # -- class variables and methods
# # 	organisation_name, 
# # 	get_organisation_name(),
# # 	set_organisation_name(org_name)

# # -- instance variables and methods()
# # emp_id,
# # name,
# # base_location,
# # deployed_location,
# # designation,
# # salary ,
# # get_employee_details() 	


# # Create a subclass of Employee named Manager as follows:
# # Manager(
	
# # 	-- instance variables and methods()
# # 	managed_employees[],
# # 	perform_appraisal_for_an_employee(emp_id,percent_raise),
# # 	get_manager_details(mgr_id)
# # )

# # Write a main method that does the following:
# # create 3 objects of Employee 
# # create an object of Manager_class and add the above 3 employee objects created as managed employees 
# # display get_manager_details()
# # for an employee do perform_appraisal_for_an_employee()

# class Employee:
#     organization_name='cdac'
#     @classmethod
#     def get_organization_name(cls):
#         return cls.organisation_name
    
#     def set_organization_name(cls, val):
#       cls.organization_name=val
      
#     def __init__(self,emp_id,name,base_location,deployed_location,destination,salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.base_location = base_location
#         self.deployed_location = deployed_location
#         self.designation = destination
#         self.salary = salary
    
#     def get_employee_details(self):
#         print("Employee ID : ",self.emp_id,"\nName :",self.name,"\nBase Location :",self.base_location,"deployed location : ",self.deployed_location,"Employee salary : ",self.salary,)
        
# class manager(Employee):
#     def __init__(self,emp_id,name,base_location,deployed_location,destination,salary,managed_emp):
#         super().__init__(emp_id,name,base_location,deployed_location,destination,salary)
#         self.managed_employees=managed_emp
        
    
#     def get_manager_details(self):
#         self.get_employee_details()
#         print("Managed employees : \n")
#         for emp in self.managed_employees:
#             emp.get_employee_details()
#             print("\n")
        
        
#     def perform_appraisal_for_an_employee(self,emp_id,percent_raise):
#         for emp in self.managed_employees:
#             if emp.emp_id == emp_id:
#                emp.salary = emp.salary + (emp.salary * (percent_raise /100))
                
            
            
# def main():
#     emp1 = Employee(1,'akshay', 'nagpur', 'mumbai', 'developer', 50)
#     emp2 = Employee(2,'sumedh', 'pune', 'Paris', 'web developer', 70)
#     emp3 = Employee(3,'vikas', 'Delhi', 'Banglore', 'Tester',10)
#     mgr = manager(4,'avinash', 'hadapsar', 'cdac', 'manager',1077,[emp1,emp2,emp3])
    
    
    
#     mgr.get_manager_details()
#     mgr.perform_appraisal_for_an_employee(2,50)
#     mgr.get_manager_details()
    
# main()

    
# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 

# class person:
#     def __init__(self,name,place_of_residence):
#         self.name=name
#         self.place_of_residence=place_of_residence
        
#     def display_attributes(self):
#         print ("Name is ", self.name,"\nPlace of residence is", self.place_of_residence)
        
# class sister(person):
#     def __init__(self,name,place_of_residence,exam_subjects):
#         super().__init__(name,place_of_residence)
#         self.exam_subjects=exam_subjects
        
#     def display_attributes(self):
#         super().display_attributes()
#         print("Exams subjects are :",self.exam_subjects)
        
# class uncle(person):
#     def __init__(self,name,place_of_residence,business):
#         super().__init__(name,place_of_residence)
#         self.business=business
        
#     def display_attributes(self):
#         super().display_attributes()
#         print("Business is :",self.business)
        
# def main():
#     sis = sister('sister','Pune','math')
#     unc = uncle('uncle','mumbai','')
#     sis.display_attributes()
#     unc.display_attributes()
    
# main()