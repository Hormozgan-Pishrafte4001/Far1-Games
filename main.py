import random


class XOGame:
    _board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    def pretty_board(self):
        result = ""
        for row in self._board:
            for cell in row:
                if cell == "":
                    cell = "."
                result += cell
            result += "\n"
        return result

    def place(self, x, y, xo) -> None:
        if xo not in ("X", "O"):
            raise ValueError("xo must be X or O")
        if x not in range(2 + 1):
            raise ValueError("x must be from 0 to 2")
        if y not in range(2 + 1):
            raise ValueError("y must be from 0 to 2")
        if self._board[y][x] != "":
            raise ValueError("the selected cell is not empty")

        self._board[y][x] = xo

    def end_of_game(self) -> bool:
        b = ""
        for row in self._board:
            b += "".join(row)
        if len(b) == 9:
            return True

        if self.has_won("X") or self.has_won("O"):
            return True

        return False

    def has_won(self, xo) -> bool:
        if xo not in ("X", "O"):
            raise ValueError("xo must be X or O")
        xo *= 3
        for row in self._board:
            row = "".join(row)
            if row == xo:
                return True

        for x in range(2 + 1):
            column = ""
            for y in range(2 + 1):
                column += self._board[y][x]
            if column == xo:
                return True

        adj = ""
        for i in range(2 + 1):
            adj += self._board[i][i]
        if adj == xo:
            return True

        adj = "".join([
            self._board[0][2],
            self._board[1][1],
            self._board[2][0],
        ])
        if adj == xo:
            return True

        return False


if __name__ == "__main__":
    game = XOGame()
    turn = random.choice(("X", "O"))
    while not game.end_of_game():
        x, y = input(f"{turn}> ").strip().split()
        x, y = int(x), int(y)
        try:
            game.place(x, y, turn)
        except ValueError as e:
            print(e)
        print(game.pretty_board())
        turn = "X" if turn == "O" else "O"
        # ^ if turn is "O" it should become "X" and vice versa

    if game.has_won("X"):
        print("Player X has won")
    elif game.has_won("O"):
        print("Player O has won")
    else:
        print("Draw!")
