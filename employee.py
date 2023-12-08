class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."

class CommissionEmployee(Employee):
    def __init__(self, name, commission):
        super().__init__(name)
        self.commission = commission

    def get_pay(self):
        return self.commission

    def __str__(self):
        return f"{self.name} receives a commission of {self.commission}. Their total pay is {self.get_pay()}."
    
# Example usage:
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
# ... and so on for Renee, Jan, Robbie, Ariel with their respective classes and parameters.
