class Employee:
    existing_ids = set()  

    def __init__(self, employee_id, name, department):
        if employee_id in Employee.existing_ids:
            raise ValueError("Employee ID must be unique!")
        
        self.employee_id = employee_id
        self.name = name
        self.department = department
        Employee.existing_ids.add(employee_id)

    def display_employee(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"
