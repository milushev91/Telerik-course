class Employee:
    def __init__(self, full_name, salary, department):
        self.full_name = full_name
        self.salary = salary
        self.department = department
    
    def public_info(self):
        return f"{self.full_name}, Department: {self.department}"
    
    def internal_info(self):
        return f"{self.publi_info()}, Salary: {self.salary}"
