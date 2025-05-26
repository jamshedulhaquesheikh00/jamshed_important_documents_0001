class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to an Employee

    def get_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

# Example usage
emp = Employee("Alice", 101)
dept = Department("HR", emp)

print(dept.get_department_info())
