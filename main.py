from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# we have 4 classes: Menu, MenuItem, CoffeeMaker, MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_ON = True
while machine_ON:
    order = input(f"What would you like? ({menu.get_items()}) \n").lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        machine_ON = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

