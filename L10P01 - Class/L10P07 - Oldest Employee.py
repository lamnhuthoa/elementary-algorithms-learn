# Bai 7
# Oldest Employee
class Employee:
    def __init__(self, emp_id, name, birth_year):
        self.emp_id = emp_id
        self.name = name
        self.birth_year = birth_year
        
class EmployeeRegistry:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
    def find_oldest_employee(self):
        oldest_employee = None
        for employee in self.employees:
            if  (
                    oldest_employee is None
                ) or (
                    employee.birth_year < oldest_employee.birth_year or (
                        employee.birth_year == oldest_employee.birth_year and employee.emp_id < oldest_employee.emp_id
                    )
                ):
                oldest_employee = employee
            
        return oldest_employee
    
num_of_employees = int(input())
registry = EmployeeRegistry()

for _ in range(num_of_employees):
    emp_id, name, birth_year = input().split()
    employee = Employee(emp_id, name, int(birth_year))
    registry.add_employee(employee)
    
oldest_employee = registry.find_oldest_employee()
print(f"{oldest_employee.emp_id} {oldest_employee.name} {oldest_employee.birth_year}")