class GameBoard:
    def __init__(self):
        # 0 = field free
        # 1 = field occupied by player 1
        # 2 = field occupied by player 2
        self.playing_fields = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Checks if the field is still free and places the corresponding player on the field.
    def make_turn(self, position: int, player: int) -> bool:
        if self.playing_fields[position] == 0:
            self.playing_fields[position] = player
            return True
        else:
            return False

    # Checks if there are still empty spaces on the board
    def free_field(self) -> bool:
        for i in self.playing_fields:
            if i == 0:
                return True
        return False

    # The game status is checked
    def check_status(self) -> int:
        for i in range(3):
            # vertical
            if self.playing_fields[i] == self.playing_fields[i + 3] and self.playing_fields[i] == self.playing_fields[
                i + 6] and self.playing_fields[i] != 0:
                return self.playing_fields[i]
            # horizontal
            if self.playing_fields[i * 3] == self.playing_fields[i * 3 + 1] and self.playing_fields[i * 3] == \
                    self.playing_fields[i * 3 + 2] and self.playing_fields[i * 3] != 0:
                return self.playing_fields[i * 3]
            # diagonal
            # only position 0 and 2 is needed
            if i == 1:
                continue
            if self.playing_fields[i] == self.playing_fields[4] and self.playing_fields[i] == self.playing_fields[
                8 - i]:
                return self.playing_fields[i]
        if not self.free_field():
            return 3
        return 0

    # Builds the game board string, which can be printed.
    def print(self):
        string = ""
        for index, item in enumerate(self.playing_fields):
            if item == 0:
                string += "   "
            elif item == 1:
                string += " X "
            else:
                string += " O "
            if (index + 1) % 3 == 0:
                string += "\n"
            else:
                string += "|"
        print(string)

    def reset(self):
        self.playing_fields = [0, 0, 0, 0, 0, 0, 0, 0, 0]
