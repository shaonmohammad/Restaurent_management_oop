class food:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
       
            
    
class Burger(food):
    def __init__(self, name, price,meat) -> None:
        super().__init__(name, price)
        self.meat = meat

class Pizza(food):
    def __init__(self, name, price ,size,toopings) -> None:
        super().__init__(name, price)
        self.size = size
        self.ingredients = toopings

class Drinks(food):
    def __init__(self, name, price,isCold=True) -> None:
        super().__init__(name, price)
        self.isCold = isCold


class Menu:
    def __init__(self) -> None:
        self.pizzas = []
        self.Burgers = []
        self.Drinks = []

    def add_menu_item(self,item_type,item):
        if( item_type == 'pizza'):
            self.pizzas.append(item)
        elif(item_type == 'burger'):
            self.Burgers.append(item)
        elif( item_type == 'drinks'):
            self.Drinks.append(item)

    def remove_pizza(self,pizza):
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)

    def show_menu(self):
        for pizza in self.pizzas:
            print(f'name: {pizza.name} price:{pizza.price} size:{pizza.size}')
        for burger in self.Burgers:
            print(f'name: {burger.name} price:{burger.price}')
        for drinks in self.Drinks:
            print(f'name: {drinks.name} price:{drinks.price}')
