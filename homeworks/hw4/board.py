class Board:
    def __init__(self, n_row, n_column):
        self.c_board = []
        self.n_row = n_row
        self.n_column = n_column
        self.create_board()
        self.show_board()

    def create_board(self):
        for i in range(self.n_row):
            col = []
            for j in range(self.n_column):
                col.append(i * self.n_row + j)
            self.c_board.append(col)

    def show_board(self):
        s_board = "\n".join(" ".join(str(el) for el in row) for row in self.c_board)
        print(s_board)

    def change_board(self, selected_move, player_symbol):
        is_exist_in_board = False
        for i in range(self.n_row):
            for j in range(self.n_column):
                if self.c_board[i][j] == selected_move:
                    self.c_board[i][j] = player_symbol
                    is_exist_in_board = True
                    break
        return is_exist_in_board

    def create_list(self):
        obj = {}
        for i in range(0, self.n_row):
            obj[i] = []
        return obj

    def is_game_ended(self):
        liste1 = Board.create_list(self)
        liste2 = Board.create_list(self)
        for j in range(self.n_column):
            for i in range(self.n_row):
                if self.c_board[0][j] == 'X':
                    if self.c_board[i][j] == 'X':
                        liste1[j].append(self.c_board[i][j])

                        if len(liste1[j]) == self.n_row:
                            print('kazandın')
                            return False
                elif self.c_board[0][j] == 'O':
                    if self.c_board[i][j] == 'O':
                        liste1[j].append(self.c_board[i][j])
                        print(liste1[i])
                        if len(liste1[j]) == self.n_row:
                            print('kazandın')
                            return False
        for j in range(self.n_row):
            for i in range(self.n_column):
                if self.c_board[j][0] == 'X':
                    if self.c_board[j][i] == 'X':
                        liste2[j].append(self.c_board[j][i])
                        print(liste2[i])
                        if len(liste2[j]) == self.n_row:
                            print('kazandın')
                            return False
                if self.c_board[j][0] == '0':
                    if self.c_board[j][i] == '0':
                        liste2[j].append(self.c_board[j][i])
                        print(liste2[i])
                        if len(liste2[j]) == self.n_row:
                            print('kazandın')
                            return False