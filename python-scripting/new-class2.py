# class to demonstrate inheritance in python 
# Main Class - Employee 

class Employee:

    def __init__(name, self):

        self.name = name

    
    def emp_name(self):
        return f"Employee Name: {self.name}"
    
class EmployeeDetails(Employee):
    
    def __init__(code, name, self):
        # calls the parent class

        super.__init__(name)
        self.code = code

    def emp_details():
        pass

    