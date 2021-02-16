from src.game_board import GameBoard


class Control:
    def __init__(self):
        self.game_board = GameBoard()
        print("Welcome to Tic Tac Toe! \nField Numbering:\n 1 | 2 | 3 \n 4 | 5 | 6\n 7 | 8 | 9")

        while True:
            if self.play(1):
                break
            if self.play(2):
                break

        print("Finish.")

    def play(self, player: int):
        self.choose_field(player, f"Player {player} choose field [1-9]: ")
        self.game_board.print()
        status = self.game_board.check_status()
        if status == 1:
            print(f"Player {status} win!")
            return True
        elif status == 2:
            print(f"Player {status} win!")
            return True
        elif status == 3:
            print(f"All Fields full!")
            return True

    def choose_field(self, player: int, text: str):
        value = input(text)
        # pos must be able to be converted to a number
        try:
            value = int(value)
        except ValueError:
            self.choose_field(player, f"Error: The input was not a number. Retry Player {player}: ")

        # position must be between 1 and 9
        if value < 1 or value > 9:
            self.choose_field(player, f"Error: The entered number is not between 1 and 9. Retry Player {player}: ")

        if not self.game_board.make_turn(value - 1, player):
            self.choose_field(player, f"Error: The field with the entered number is not free. Retry Player {player}: ")


if __name__ == '__main__':
    Control()
