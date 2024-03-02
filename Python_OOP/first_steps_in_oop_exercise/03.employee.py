class Employee:
    MONTHS = 12

    def __init__(self, _id, first_name, last_name, salary):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * Employee.MONTHS

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary
