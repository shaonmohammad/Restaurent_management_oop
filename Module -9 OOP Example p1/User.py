from abc import ABC,abstractmethod
class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        super().__init__()
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name,money,phone,email,address) -> None:
        super().__init__(name)
        self.wallet = money
        self.__Order = None
        self.bill__due = 0
   
    @property
    def order(self):
       return self.__order
    
    @order.setter
    def order(self,order):
        self.__order = order


    def place_order(self,order):
        self.order = order
        self.bill__due += order.bill
        print(f'{self.name} placed an order with bill {order.bill}')

    def eat_food(self,order):
        print(f'{self.name} item food {self.items}')
    def pay_for_order(self,amount):
        pass
    def give_tips(self,tips_amount):
        pass



class Emplpoyee(User):
    def __init__(self, name, phone, email, address,salary,starting_date,department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_date= starting_date
        self.department = department
        self.due = salary

    def receive_salary(self):
        self.due= 0


class Chef(Emplpoyee):
    def __init__(self, name, phone, email, address, salary, starting_date, department,cocking_items) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.cocking_items = cocking_items

class Server(Emplpoyee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        self.tips_earing = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)
    
    def take_order(self,order):
        pass

    def raceive_tips(self,amount):
        self.tips_earing += amount

class Manager(Emplpoyee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)