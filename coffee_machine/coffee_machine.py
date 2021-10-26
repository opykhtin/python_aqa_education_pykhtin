# Coffee Machine


# Stage 1

text = '''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!'''

print(text)


# Stage 2

print('Write how many cups of coffee you will need:')
cups_of_coffee = int(input())

cup_of_coffee_water = 200
cup_of_coffee_milk = 50
cup_of_coffee_beans = 15

water = cup_of_coffee_water * cups_of_coffee
milk = cup_of_coffee_milk * cups_of_coffee
beans = cup_of_coffee_beans * cups_of_coffee

print('For %s cups of coffee you will need:' % cups_of_coffee)
print('%d ml of water ' % water)
print('%d ml of milk ' % milk)
print('%d g of coffee beans' % beans)


# Stage 3

print('Write how many ml of water the coffee machine has:')
ml_water = int(input())
print('Write how many ml of milk the coffee machine has:')
ml_milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
gr_beans = int(input())

print('Write how many cups of coffee you will need:')
cups_of_coffee = int(input())

cup_of_coffee_water = 200
cup_of_coffee_milk = 50
cup_of_coffee_beans = 15

available_cups_of_coffee = min(ml_water // cup_of_coffee_water, ml_milk // cup_of_coffee_milk,
                               gr_beans // cup_of_coffee_beans)

if cups_of_coffee == available_cups_of_coffee:
    print('Yes, I can make that amount of coffee')
elif cups_of_coffee > available_cups_of_coffee:
    print(f'No, I can make only {available_cups_of_coffee} cups of coffee')
elif cups_of_coffee < available_cups_of_coffee:
    print(
        f"Yes, I can make that amount of coffee (and even {available_cups_of_coffee - cups_of_coffee} more than that)")


# Stage 4

machine_amount = {
    "water": 400,
    "milk": 540,
    "c_beans": 120,
    "cups": 9,
    "money": 550
}


def machine_display():
    # displays quantities in the machine
    print(f'The coffee machine has:')
    print(f"{machine_amount.get('water')} of water")
    print(f"{machine_amount.get('milk')} of milk")
    print(f"{machine_amount.get('c_beans')} of coffee beans")
    print(f"{machine_amount.get('cups')} of disposable cups")
    print(f"{machine_amount.get('money')} of money")


def machine_action():
    # actions in the machine
    machine_display()
    action = str(input('Write action (buy, fill, take): \n'))
    print()
    # choices in the coffee machine
    if action == 'buy':
        buy_drink()
    elif action == 'fill':
        fill_machine()
    elif action == 'take':
        take_money()


def buy_drink():
    # types of coffee in the machine
    type_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n')
    if type_of_coffee == '1':
        espresso = [250, 0, 16, 1, 4]
        balance_calculation(espresso)
    elif type_of_coffee == '2':
        latte = [350, 75, 20, 1, 7]
        balance_calculation(latte)
    elif type_of_coffee == '3':
        cappuccino = [200, 100, 12, 1, 6]
        balance_calculation(cappuccino)


def balance_calculation(bought_drink):
    # amount in the machine
    global machine_amount
    machine_amount['water'] -= bought_drink[0]
    machine_amount['milk'] -= bought_drink[1]
    machine_amount['c_beans'] -= bought_drink[2]
    machine_amount['cups'] -= bought_drink[3]
    machine_amount['money'] += bought_drink[4]
    machine_display()


def fill_machine():
    # fill in the machine
    global machine_amount
    machine_amount['water'] += int(input('Write how many ml of water you want to add:\n'))
    machine_amount['milk'] += int(input('Write how many ml of milk you want to add:\n'))
    machine_amount['c_beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
    machine_amount['cups'] += int(input('Write how many disposable coffee cups you want to add:\n'))
    machine_display()


def take_money():
    # take money in the machine
    print(f"I gave you {machine_amount.get('money')}")
    machine_amount['money'] -= machine_amount['money']
    print()
    machine_display()


machine_action()


# Stage 5

machine_amount = {
    "water": 400,
    "milk": 540,
    "coffee beans": 120,
    "cups": 9,
    "money": 550
}


def machine_display():
    # displays quantities in the machine
    string = f'''The coffee machine has: 
{machine_amount.get('water')} of water
{machine_amount.get("milk")} of milk
{machine_amount.get('coffee beans')} of coffee beans
{machine_amount.get('cups')} of disposable cups
{machine_amount.get('money')} of money'''
    return string


def machine_action():
    # actions in the machine
    action = str(input('\nWrite action (buy, fill, take, remaining, exit): \n'))
    if action == 'buy':
        buy_drink()
        machine_action()
    elif action == 'fill':
        fill_machine()
    elif action == 'take':
        take_money()
    elif action == 'remaining':
        print(machine_display())
        machine_action()
    elif action == 'exit':
        exit()
    return machine_display()


def balance_calculation(bought_drink):
    # amount in the machine
    global machine_amount
    machine_amount['water'] -= bought_drink[0]
    machine_amount['milk'] -= bought_drink[1]
    machine_amount['coffee beans'] -= bought_drink[2]
    machine_amount['cups'] -= bought_drink[3]
    machine_amount['money'] += bought_drink[4]
    for ingredients in machine_amount:
        if machine_amount.get(f'{ingredients}') < 0:
            print(f"Sorry, not enough {ingredients}!")
            machine_amount['water'] += bought_drink[0]
            machine_amount['milk'] += bought_drink[1]
            machine_amount['coffee beans'] += bought_drink[2]
            machine_amount['cups'] += bought_drink[3]
            machine_amount['money'] -= bought_drink[4]
            break
        else:
            print("I have enough resources, making you a coffee!")
            break

    return machine_amount


def buy_drink():
    # types of coffee in the machine
    type_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu: \n')
    if type_of_coffee == '1':
        espresso = [250, 0, 16, 1, 4]
        balance_calculation(espresso)
    elif type_of_coffee == '2':
        latte = [350, 75, 20, 1, 7]
        balance_calculation(latte)
    elif type_of_coffee == '3':
        cappuccino = [200, 100, 12, 1, 6]
        balance_calculation(cappuccino)
    elif type_of_coffee == 'back':
        machine_action()
    return machine_amount


def fill_machine():
    # fill in the machine
    global machine_amount
    machine_amount['water'] += int(input('Write how many ml of water you want to add:\n'))
    machine_amount['milk'] += int(input('Write how many ml of milk you want to add:\n'))
    machine_amount['coffee beans'] += int(input('Write how many grams of coffee beans you want to add:\n'))
    machine_amount['cups'] += int(input('Write how many disposable coffee cups you want to add:\n'))
    machine_action()


def take_money():
    # take money in the machine
    print(f"I gave you {machine_amount.get('money')}")
    machine_amount['money'] -= machine_amount['money']
    print()
    machine_action()


print(machine_display())
print(machine_action())
