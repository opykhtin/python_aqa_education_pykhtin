"""Tic Tac Toe Game"""
import logging
import sys
import time
from pathlib import Path


Path("logs").mkdir(parents=True, exist_ok=True)
FILENAME = 'logs/game_log.log'


def configure_logger():
    """Configure logger for terminal"""
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(FILENAME)
    file_handler.setLevel(logging.WARNING)
    file_format = logging.Formatter('%(asctime)s %(message)s', "%d-%m-%Y %H:%M:%S")
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)

    stream_handler.setLevel(logging.WARNING)
    console_format = logging.Formatter('%(message)s')
    stream_handler.setFormatter(console_format)
    logger.addHandler(stream_handler)
    return logger


log = configure_logger()


def timer(func):
    """Decorator used for counting time games and displays time games in logs"""
    def wrapper(*args_for_function):
        start = time.time()
        func(*args_for_function)
        end = time.time()
        total_time = (end - start)
        log.warning(f'Game duration time was: {total_time.__round__(2)}')

    return wrapper


class PlayGame:

    def __init__(self):
        self.playing_game = True
        """Check if game is still going"""
        self.winner = None
        self.name_X = None
        self.name_O = None
        self.current_player = "X"
        self.current_player_name = self.name_X
        self.field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def main_menu(self):
        """Main menu method"""
        try:
            print('''1. Play game
2. Show Logs
3. Clear Logs
0. Exit''')
            user_input = input('> ')
            if user_input == '1':
                self.set_name()
            elif user_input == '2':
                self.show_logs()
                self.main_menu()
            elif user_input == '3':
                self.clear_logs()
                self.main_menu()
            elif user_input == '0':
                quit()
        except KeyError:
            print("This option does not exist.\nPlease try again")

    def board_display(self):
        """Display the board"""
        print("\n")
        print(" |-1-+-2-+-3-|")
        print(" | " + self.field[0] + " | " + self.field[1] + " | " + self.field[2] + " | ")
        print(" |-4-+-5-+-6-|")
        print(" | " + self.field[3] + " | " + self.field[4] + " | " + self.field[5] + " | ")
        print(" |-4-+-5-+-6-|")
        print(" | " + self.field[6] + " | " + self.field[7] + " | " + self.field[8] + " | ")
        print(" |-7-+-8-+-9-|")
        print("\n")

    def winner_check(self, mark):
        """Checking winner"""
        winner_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for i in range(0, len(winner_list)):
            result = all(self.field[element] == mark for element in winner_list[i])
            if result:
                self.playing_game = False
                self.winner = mark

    def draw_check(self):
        """Draw checking"""
        if " " not in self.field:
            self.playing_game = False
            return True

        else:
            return False

    def set_name(self):
        """Set names"""
        print('Х player, please, enter your name:')
        self.name_X = str(input('> '))
        self.current_player_name = self.name_X

        print('O player, please, enter your name:')
        self.name_O = str(input('> '))
        self.start_play()

    @timer
    def start_play(self):
        """Start the game"""
        while self.playing_game:
            self.board_display()
            self.position_input(self.current_player)
            self.end_game_check()

            self.change_player()
        if self.winner == "X" or self.winner == "O":
            self.change_player()
            self.board_display()
            log.warning(f'{self.current_player_name} won!')
            print(self.current_player_name + " won!")

        elif self.winner is None:
            print("Draw")
            log.warning('Draw between players')
        if self.ask_play_again():
            self.field = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.winner = None
            self.playing_game = True
            self.start_play()

        return

    def ask_play_again(self):
        """Ask player to play again"""
        print("Do you want to play again? 1 - yes, 2 - no):")
        play_again = input('> ')
        if play_again == '1':
            return True
        elif play_again == '2':
            quit()
        else:
            self.ask_play_again()

    def position_input(self, player):
        """Prints whose turn it is to enter the input"""
        print(f"{self.current_player_name} - your turn")
        position = input("Enter the field from 1 to 9:\n > ")

        valid = False
        while not valid:

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Enter the field from 1 to 9:\n")

            position = int(position) - 1

            if self.field[position] == " ":
                valid = True
            else:
                print("This field is already taken! Try again.")

        self.field[position] = player

    def end_game_check(self):
        """Check end the game"""
        self.winner_check(self.current_player)
        self.draw_check()

    def change_player(self):
        """Changing players"""
        if self.current_player == "X":
            self.current_player_name = self.name_O
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player_name = self.name_X
            self.current_player = "X"

    @staticmethod
    def show_logs():
        try:
            with open(FILENAME, "r") as log_file:
                print(log_file.read())
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()

    @staticmethod
    def clear_logs():
        try:
            with open(FILENAME, "w") as log_file:
                log_file.truncate()
        except OSError:
            log.critical('File not found')
        else:
            log_file.close()


def main():
    game = PlayGame()
    game.main_menu()


if __name__ == '__main__':
    main()
