from menu import Pizza,Burger,Drinks,Menu
from User import Customer,Emplpoyee,Chef
from order import Order

def main():
    menu = Menu()
    pizza1 = Pizza('Shutiki Pizza',600,'large',['sutiki,onion'])
    menu.add_menu_item('pizza',pizza1)
    pizza2 = Pizza('alur pizza',400,'large',['poteto','onion','sos'])
    menu.add_menu_item('pizza',pizza2)
    pizza3 = Pizza('Dal pizza',400,'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza3)

    # add burger to the menu
    burger1 = Burger('Naga Burger',1000,'chicken')
    menu.add_menu_item('burger',burger1)
    burger2 = Burger('Beef Burger',1200,'Beef')
    menu.add_menu_item('burger',burger2)


    #add drinks to the menu
    cock = Drinks('cock',50,True)
    menu.add_menu_item('drinks',cock)
    Coffe = Drinks('coffe',50,False)
    menu.add_menu_item('drinks',Coffe)


    ## show menu
    menu.show_menu()

    #Customer 
    customer_1 = Customer('shakib khan',100,3239232432,'abc@gmail.com','feni')

    #Order
    Order1 = Order(customer_1,[pizza1,burger2,Coffe])
    customer_1.place_order(Order1)
    
    



#call the main
if __name__ == '__main__':
    main()