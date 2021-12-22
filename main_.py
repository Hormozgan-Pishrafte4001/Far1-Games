from main import XOGame

BIG_X = """
X X
 X 
X X
"""

BIG_O = """
 O 
O O
 O 
"""

BIG_D = """
DD 
D D
DD 
"""

class SuperXOGame:
    _board = []

    def __init__(self):
        for i in range(3):
            row = list()
            for j in range(3):
                row.append(XOGame())
            self._board.append(row)

    def pretty_print(self) -> str:
        pretty_board = []
        for i, row in enumerate(self._board):
            pretty_board.append([])
            for subgame in row:
                if isinstance(subgame, str):
                    if subgame == "D":
                        pretty_board[i].append(BIG_D)
                    if subgame == "X":
                        pretty_board[i].append(BIG_X)
                    if subgame == "O":
                        pretty_board[i].append(BIG_O)
                else:
                    pretty_board[i].append(subgame.pretty_board())

        result = ""
        pretty_board = [[x.split("\n") for x in row] for row in pretty_board]
        print(pretty_board)

    def place(self, x0, y0, x1, y1, xo):
        if x0 not in range(2 + 1):
            raise ValueError("x0 must be from 0 to 2")
        if y0 not in range(2 + 1):
            raise ValueError("y0 must be from 0 to 2")
        
        subgame = self._board[y0][x0]
        if isinstance(subgame, XOGame):
            subgame.place(x1, y1, xo)
            if subgame.end_of_game():
                if subgame.has_won("X"):
                    self._board[y0][x0] = "X"
                elif subgame.has_won("O"):
                    self._board[y0][x0] = "O"
                else:
                    self._board[y0][x0] = "D"
        else:
            raise ValueError("The place is already taken")


    def end_of_game(self) -> bool:
        for row in self._board:
            for subgame in row:
                if isinstance(subgame, XOGame):
                    return False
        return True

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
    super_xo_game = SuperXOGame()
    turn = "X"

    print("Welcome to Super XO game")
    while not super_xo_game.end_of_game():
        try:
            coordiantes = input(f"{turn}> ")
            x0, y0, x1, y1 = (int(i) for i in coordiantes.split())
            super_xo_game.place(x0, y0, x1, y1, turn)
            turn = "O" if turn == "X" else "X"
            super_xo_game.pretty_print()
        except Exception as e:
            print(e)
