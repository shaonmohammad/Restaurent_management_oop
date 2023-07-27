class Restaurent:
    def __init__(self,name,menu = []) -> None:
        self.name = name
        self.chef  = None
        self.manager = None
        self.server = None
        self.manu = []
        self.revenue = 0
        self.balance = 0
        self.profit = 0
        self.expense = 0

        def add_employee(self,employee_type,employee):
            if(employee_type == 'chef'):
                self.chef = employee

            elif(employee_type == 'server'):
                self.server = employee

            elif (employee_type == 'manager'):
                self.manager = employee

        def receive_payment(self,order,amount,cutomer):
            if order.bill > amount:
                self.reveneu += amount
                self.balance += amount
                cutomer.due_amount = 0
                return order.bill - amount
            
        def pay_expense(self,amount,description):
            if(amount < self.balance):
                self.expense += amount
                self.balance -= amount
                print(f'Expense {amount} for {description}')
            else:
                print('Not enough money')

        def pay_salary(self,employee):
            if employee.salary < self.balance:
                employee.receive_salary()
