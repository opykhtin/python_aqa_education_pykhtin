"""Stage 6. Perfect Final"""


class CoffeeMachine:
    """Coffee Machine 2.0"""

    __MENU_TEXT = {"active": "Write action (buy, fill, take, remaining, exit):\n",
                   "select": "What do you want to buy? 1 - espresso, 2 - latte, "
                             "3 - cappuccino, back – to main menu: \n",
                   "water": "Write how many ml of water you want to add:",
                   "milk": "Write how many ml of milk you want to add:",
                   "c_beans": "Write how many grams of coffee beans you want to add:",
                   "cups": "Write how many disposable coffee cups you want to add:"}

    __ESPRESSO = {'water': 250, 'milk': 0, 'c_beans': 16, 'cups': 1, 'money': 4}
    __LATTE = {'water': 350, 'milk': 75, 'c_beans': 20, 'cups': 1, 'money': 7}
    __CAPPUCCINO = {'water': 200, 'milk': 100, 'c_beans': 12, 'cups': 1, 'money': 6}

    def __init__(self, water, milk, c_beans, cups, money):
        """all items in the machine"""
        self.water = water
        self.milk = milk
        self.c_beans = c_beans
        self.cups = cups
        self.money = money
        self.state = 'active'

    def buy_drink(self, user_input):
        """types of coffee in the machine"""
        if user_input in ['1', '2', '3', 'back']:
            if user_input == '1':
                self.available_ingredients(self.__ESPRESSO)
            elif user_input == '2':
                self.available_ingredients(self.__LATTE)
            elif user_input == '3':
                self.available_ingredients(self.__CAPPUCCINO)
            elif user_input == 'back':
                pass
        else:
            pass

    def available_ingredients(self, bought_drink):
        """check available ingredients"""
        if self.water - bought_drink['water'] < 0:
            print("Sorry, not enough water!")
        elif self.milk - bought_drink['milk'] < 0:
            print("Sorry, not enough milk!")
        elif self.c_beans - bought_drink['c_beans'] < 0:
            print("Sorry, not enough coffee beans!")
        elif self.cups - bought_drink['cups'] < 0:
            print("Sorry, not enough disposable cups!")
        else:
            self.water -= bought_drink['water']
            self.milk -= bought_drink['milk']
            self.c_beans -= bought_drink['c_beans']
            self.cups -= bought_drink['cups']
            self.money += bought_drink['money']
            print("I have enough resources, making you a coffee!")

    def fill_machine(self):
        """fill the items in the machine"""
        print(self.__MENU_TEXT['water'])
        self.water += int(input())
        print(self.__MENU_TEXT['milk'])
        self.milk += int(input())
        print(self.__MENU_TEXT['c_beans'])
        self.c_beans += int(input())
        print(self.__MENU_TEXT['cups'])
        self.cups += int(input())

    def take_money(self):
        """take money in the machine"""
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def machine_amount(self):
        """displays items in the machine"""
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.c_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def make_action(self, user_input):
        """check status when input"""
        if self.state == 'active':
            if user_input == 'buy':
                self.state = 'select'
                return self.__MENU_TEXT[self.state]
            elif user_input == 'fill':
                self.fill_machine()
                return self.__MENU_TEXT[self.state]
            elif user_input == 'take':
                self.take_money()
                return self.__MENU_TEXT[self.state]
            elif user_input == 'remaining':
                self.machine_amount()
                return self.__MENU_TEXT[self.state]
            elif user_input == 'exit':
                exit()
        elif self.state == 'select':
            self.buy_drink(user_input)
            self.state = 'active'
            return self.__MENU_TEXT[self.state]
        return self.__MENU_TEXT[self.state]


def main():
    """actions"""
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    """ingredients by default in coffee machine"""
    response = 'Write action (buy, fill, take, remaining, exit):\n'
    while True:
        machine_action = input(f'{response}')
        response = machine.make_action(machine_action)


if __name__ == '__main__':
    main()
