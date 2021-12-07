"""Bank system"""

from random import randrange
import secrets
import sqlite3
import time


class BankSystem:
    """Bank System"""

    TEXT = {
        "main_menu": '''\n1. Create an account 
2. Log into account
0. Exit''',
        "login_card": "Enter your card number:",
        "login_pin": "Enter your PIN:",
        "login_error": "Wrong card number or PIN!",
        "login_menu": '''\n1. Balance
2. Add Income
3. Do Transfer
4. Close Account
5. Log out
0. Exit''',
        "enter_income": "Enter income:",
        "do_transfer": '''Transfer
Enter card number:''',
        "close_account": "The account has been closed!"
    }

    def __init__(self):
        """Main characteristics, Creating table"""
        self.card_numbers = []
        self.pin_numbers = []
        self.user = None
        self.balance = None
        self.pinn = 400000
        self.state = 'main_menu'
        self.attempt = 0
        self.connection = sqlite3.connect('card.s3db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BANK_USER(
        ID INTEGER PRIMARY KEY, 
        CARD TEXT,
        PIN TEXT,
        BALANCE INTEGER DEFAULT 0)''')
        self.connection.commit()

    def menu_state(self):
        """Menu states"""
        if self.state == 'main_menu':
            entered_value = self.display_text(self.state)
            self.main_input(entered_value)
            return True
        elif self.state == "login_card":
            login_card = self.display_text(self.state)
            login_pin = self.display_text("login_pin")
            self.login_account(login_card, login_pin)
            return True
        elif self.state == "login_menu":
            entered_value = self.display_text(self.state)
            self.login_input(entered_value)
            return True
        elif self.state == "enter_income":
            entered_value = self.display_text(self.state)
            self.enter_income(entered_value)
            return True
        elif self.state == "do_transfer":
            entered_value = self.display_text(self.state)
            self.do_transfer(entered_value)
            return True
        elif self.state == "close_account":
            self.display_text(self.state)
            return True

    def display_text(self, state):
        """Input with text"""
        print(self.TEXT[state])
        entered_value = input("> ")
        return entered_value

    def main_input(self, entered_value):
        """Main menu actions"""
        if entered_value == "1":
            self.create_account()
        elif entered_value == "2":
            self.state = "login_card"
            self.dev_only_get_exists_credentials()
        elif entered_value == "0":
            print("\nBye!")
            self.connection.close()
            self.state = "off"
        else:
            print(self.TEXT["login_error"])
            self.state = "main_menu"

    def login_input(self, entered_value):
        """User menu actions"""
        balance = self.balance_account()
        if entered_value == "1":
            print(f"\nBalance: {balance}\n")
        elif entered_value == "2":
            self.dev_only_get_exists_credentials()
            self.state = "enter_income"
        elif entered_value == "3":
            self.state = "do_transfer"
        elif entered_value == "4":
            self.close_account()
            self.state = "main_menu"
        elif entered_value == "5":
            self.state = "main_menu"
        elif entered_value == "0":
            print("\nBye!")
            self.state = "off"

    def balance_account(self):
        """Get balance"""
        balance = self.cursor.execute(f'''SELECT BALANCE FROM BANK_USER WHERE CARD = {self.user}''')
        self.balance = balance.fetchone()[0]
        return self.balance

    def create_account(self):
        """Create account. Card, PIN"""
        create_card_numbers = "400000" + format(randrange(0000000000, 9999999999), '010d')
        create_pin_numbers = format(secrets.randbelow(9999), '04d')

        self.card_numbers.append(create_card_numbers)
        self.pin_numbers.append(create_pin_numbers)

        self.cursor.execute(f'''INSERT INTO BANK_USER (CARD, PIN) VALUES 
        ("{create_card_numbers}", "{create_pin_numbers}")''')
        self.connection.commit()

        print(f"\nYour card has been created\nYour card number: \n{create_card_numbers}\n"
              f"Your card PIN: \n{create_pin_numbers}\n")
        self.state = 'main_menu'

    def login_account(self, account_card, account_pin):
        """Login into account"""
        self.cursor.execute(f'''SELECT * FROM BANK_USER WHERE CARD = {account_card} AND PIN = {account_pin}''')
        account = self.cursor.fetchone()
        if account:
            self.attempt = 0
            self.user = account_card
            print("\nYou have successfully logged in!\n")
            self.state = "login_menu"
        else:
            self.attempt += 1
            if self.attempt >= 3:
                print("\nBrute Force detected. Please wait 60 seconds.\n")
                time.sleep(60)
            else:
                print("\nWrong Card or PIN!\n")
            self.state = "main_menu"

    def check_card_created(self):
        """Check the card in DB"""
        created_card = self.cursor.execute(f'''SELECT CARD FROM BANK_USER WHERE CARD = {self.card_numbers}''')
        if len(created_card.fetchall()) == 0:
            return False
        else:
            return True

    def enter_income(self, amount):
        """Add money to the card"""
        amount = int(amount) + self.balance_account()
        self.cursor.execute(f"UPDATE BANK_USER SET BALANCE = {amount} WHERE CARD = {self.user}")
        self.connection.commit()
        print("Income was added!")
        self.state = "login_menu"

    def do_transfer(self, entered_value):
        """Transfer money to the card"""
        print("Enter how much money you want to transfer:")
        card_amount = input("> ")
        if self.check_card(entered_value, card_amount):
            card_amount = int(card_amount)
            self.balance -= card_amount
            self.cursor.execute(f'UPDATE BANK_USER SET BALANCE = BALANCE - '
                                f'({card_amount}) WHERE CARD = {self.user}')
            self.cursor.execute(f'UPDATE BANK_USER SET BALANCE = BALANCE + '
                                f'({card_amount}) WHERE CARD = {entered_value}')
            self.connection.commit()
            print("\nSuccess!")
        else:
            print("\nSuch a card does not exist!")
        self.state = "login_menu"

    def check_card(self, card_numbers, card_amount):
        if self.check_card_numbers(card_numbers):
            if self.check_card_amount(card_amount):
                self.cursor.execute(f'''SELECT * FROM BANK_USER WHERE CARD = {card_numbers}''')
                other_account = self.cursor.fetchone()
                if other_account:
                    return True

    def check_card_numbers(self, card_numbers):
        if len(card_numbers) == 16 and card_numbers.isdigit() is False:
            print("\nProbably you made mistake in the card number. Please try again!")
        elif card_numbers == self.user:
            print("\nYou can't transfer money to the same account!")
        else:
            return True

    def check_card_amount(self, card_amount):
        if card_amount.isdigit() is False and int(card_amount) > 0:
            print("\nIncorrect amount!")
        elif int(card_amount) > self.balance:
            print("\nNot enough money!")
        else:
            return True

    def close_account(self):
        """Close the account"""
        self.cursor.execute(f"DELETE FROM BANK_USER WHERE CARD = {self.user}")
        self.connection.commit()
        self.user = None
        print("The account has been closed!")

    def dev_only_get_exists_credentials(self):
        # dev only part to know what credentials could be used
        self.cursor.execute('''SELECT * FROM BANK_USER''')
        result = self.cursor.fetchall()
        print(result)


def main():
    bank = BankSystem()

    while True:
        if not bank.menu_state():
            break
        elif bank.state == "off":
            break


if __name__ == '__main__':
    main()
