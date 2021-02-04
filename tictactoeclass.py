import random
class TicTacToe:
    """Class that represents the game Tic-Tac-Toe 3x3"""

    def __init__(self, state_table, is_str=True):
        self.state_table = self.make_state_table(state_table, str_type=is_str)
        # self.X_size = int(sum([1 for i in state_table if i == 'X']))
        # self.O_size = int(sum([1 for i in state_table if i == 'O']))
        self.out = '-' * 9

    def __str__(self):
        """Outputs user's friendly game table."""
        for lines in self.state_table:
            self.out += '\n|'
            for el in lines:
                if el == '_':
                    el = ''
                self.out += f'{el:>2}'
            self.out += ' |'
        self.out += '\n' + '-' * 9
        return self.out

    def check_game(self):
        """Check state table for draw or for continue"""
        dummies = 0
        X_line = 0
        O_line = 0
        for lines in self.state_table:
            for el in lines:
                if el == '_':
                    dummies += 1
                elif el == 'X':
                    X_line += 1
                elif el == 'O':
                    O_line += 1
        if X_line + O_line == 9:
            return 'Draw'
        else:
            return False

    def check_rows(self):
        """Check rows in the table for winners and returns X or O are winners"""
        for lines in self.state_table:
            x_line = 0
            o_line = 0
            for el in lines:
                if el == 'X':
                    x_line += 1
                elif el == 'O':
                    o_line += 1
            if x_line == 3:
                return f'X wins'
            elif o_line == 3:
                return f'O wins'

    def check_columns(self):
        """Check columns for winner"""
        columns = 0
        while columns < len(self.state_table[0]):
            x_line = 0
            o_line = 0
            for lines_ind in range(len(self.state_table)):
                if self.state_table[lines_ind][columns] == 'X':
                    x_line += 1
                elif self.state_table[lines_ind][columns] == 'O':
                    o_line += 1
            if x_line == 3:
                return 'X wins'
            elif o_line == 3:
                return 'O wins'
            columns += 1

    def check_diagonals(self):
        """Check diagonals for winner"""
        main_diag = 0
        alter_diag = -1
        x_main = 0
        x_alter = 0
        o_main = 0
        o_alter = 0
        for lines in self.state_table:
            if lines[main_diag] == 'X':
                x_main += 1
            elif lines[main_diag] == 'O':
                o_main += 1

            if x_main == 3:
                return 'X wins'
            elif o_main == 3:
                return 'O wins'

            if lines[alter_diag] == 'X':
                x_alter += 1
            elif lines[alter_diag] == 'O':
                o_alter += 1

            if x_alter == 3:
                return 'X wins'
            elif o_alter == 3:
                return 'O wins'
            main_diag += 1
            alter_diag -= 1

    def make_state_table(self, inp_state, str_type=True):
        """Receive state of table at the current moment if form of string if type_s=True and return the list(matrix),
        else receive state of table in form of list, so returns the list(matrix)"""
        if str_type:
            result = []
            counter = 0
            temp_list = []
            while counter < len(inp_state):
                temp_list.append(inp_state[counter])
                if (counter + 1) % 3 == 0:
                    result.append(temp_list)
                    temp_list = []
                counter += 1
            return result
        else:
            return inp_state

    def user_makes_move(self, coordinates, is_X=True):
        """Receive coordinates of game table to make a move."""
        first, second = int(coordinates[0]) - 1, int(coordinates[1]) - 1
        if is_X:
            self.state_table[first][second] = 'X'
            return TicTacToe(self.state_table, is_str=False)
        else:
            self.state_table[first][second] = 'O'
            return TicTacToe(self.state_table, is_str=False)

    def is_right_coordinates(self, coordinates):
        """Check coordinates for their type and range: int and 0 < coordinates < 4.
        Returns game table after the move or exception about incorrect coordinates"""
        try:
            first, second = int(coordinates[0]) - 1, int(coordinates[1]) - 1
        except ValueError:
            return 'You should enter numbers!'
        if -1 < first < 3 and -1 < second < 3:
            if self.state_table[first][second] == '_':
                return False
            else:
                return 'This cell is occupied! Choose another one!'
        else:
            return 'Coordinates should be from 1 to 3!'

    def comp_makes_move(self, is_X=True, medium_coor=None):
        """Returns new state table with the move of the computer"""
        if not medium_coor:
            # first_coor, second_coor = 0, 0
            first_coor, second_coor = random.randint(0, 2), random.randint(0, 2)
            while self.state_table[first_coor][second_coor] != '_':
                first_coor, second_coor = random.randint(0, 2), random.randint(0, 2)
        else:
            first_coor, second_coor = medium_coor[0], medium_coor[1]
        # print(first_coor, second_coor)
        if is_X:
            self.state_table[first_coor][second_coor] = 'X'
            return TicTacToe(self.state_table, is_str=False)
        else:
            self.state_table[first_coor][second_coor] = 'O'
            return TicTacToe(self.state_table, is_str=False)

    def checker(self):
        """United function for checkers. Returns winner, draw or None"""
        rows_winner = self.check_rows()
        columns_winner = self.check_columns()
        diagonals_winner = self.check_diagonals()
        is_draw = self.check_game()
        if rows_winner:
            return rows_winner
        elif columns_winner:
            return columns_winner
        elif diagonals_winner:
            return diagonals_winner
        elif is_draw:
            return is_draw
