class HiredEmployees:
    def __init__(self, salary_type):
        self.salary_type = salary_type
        pass

    def calculate_salary(self, fixed_amount, percentage, sale_amount):
        if self.salary_type == 'fixed':
            salary = fixed_amount
        elif self.salary_type == 'mixed':
            salary = sale_amount * percentage / 100 + fixed_amount
        else:
            salary = sale_amount * percentage / 100
        return salary
