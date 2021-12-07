"""Brute Force"""
from bank import BankSystem
import itertools


def brute_card(generated_string, rep):
    numbers = '0123456789'
    y = generated_string
    for c in itertools.product(numbers, repeat=rep):
        number = y + ''.join(c)
        yield number


def main():
    bf = BankSystem()
    card_generate = brute_card('400000', 10)
    pin_generate = brute_card('', 4)
    while True:
        card_number = str(next(card_generate))
        while True:
            pin_number = str(next(pin_generate))
            print(f'Hacking card with number: {card_number}')
            print(f'Hacking card with pin: {pin_number}')
            if bf.login_account(card_number, pin_number):
                print("You are hacked!")
                quit()
            if pin_number == '9999':
                pin_generate = brute_card('', 4)
                break


if __name__ == '__main__':
    main()
