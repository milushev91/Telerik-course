class Employee:
    def __init__(self, full_name, department, salary):
        self.full_name = full_name
        self.department = department
        self.salary = salary

    @property 
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Employee's salary must be a postive number")
            
        self._salary = value
    
    def public_info(self):
        return f"{self.full_name}, Department: {self.department}"
    
    def internal_info(self):
        return f"{self.public_info()}, Salary: {self.salary}"
