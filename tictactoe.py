from tictactoeclass import TicTacToe


class PlayGame(TicTacToe):

    def __init__(self, state_table):
        super().__init__(state_table)

    def easy_easy(self):
        """Method which represents the game between two AI. Returns result of the game."""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            first_comp = self.comp_makes_move()
            print('Making move level "easy"')
            print(first_comp)
            result = self.checker()
            if result:
                return result
            second_comp = self.comp_makes_move(is_X=False)
            print('Making move level "easy"')
            print(second_comp)
            result = self.checker()
            if result:
                return result

    def easy_user(self, is_comp_first=True):
        """Method which represents the game between AI and user."""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            if is_comp_first:
                comp_move = self.comp_makes_move()
                print('Making move level "easy"')
                print(comp_move)
                result = self.checker()
                if result:
                    return result
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=False)
                print(users_move)
                result = self.checker()
                if result:
                    return result
            else:
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=True)
                print(users_move)
                result = self.checker()
                if result:
                    return result
                comp_move = self.comp_makes_move(is_X=False)
                print('Making move level "easy"')
                print(comp_move)
                result = self.checker()
                if result:
                    return result

    def user_user(self):
        """Method which represents the game between user and user"""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            while True:
                coordinates = input('Enter the coordinates: ').split()
                is_right_coor = self.is_right_coordinates(coordinates)
                if is_right_coor:
                    print(is_right_coor)
                else:
                    break
            first_users_move = self.user_makes_move(coordinates)
            print(first_users_move)
            result = self.checker()
            if result:
                return result

            while True:
                coordinates = input('Enter the coordinates: ').split()
                is_right_coor = self.is_right_coordinates(coordinates)
                if is_right_coor:
                    print(is_right_coor)
                else:
                    break
            second_users_move = self.user_makes_move(coordinates, is_X=False)
            print(second_users_move)
            result = self.checker()
            if result:
                return result

    def rows_coor_medium(self):
        """Looking for the coordinates if there are two X or O in rows. Returns new coordinates or None"""
        for lines in range(len(self.state_table)):
            x_line = []
            o_line = []
            for el in range(len(self.state_table[lines])):
                if self.state_table[lines][el] == 'X':
                    x_line.append([lines, el + 1])
                elif self.state_table[lines][el] == 'O':
                    o_line.append([lines, el + 1])
            if len(x_line) == 2:
                if x_line[1][1] == 3:
                    new_coor = [x_line[0][0], (x_line[1][1] - x_line[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [x_line[0][0], (x_line[1][1] + x_line[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
            elif len(o_line) == 2:
                if o_line[1][1] == 3:
                    new_coor = [o_line[0][0], (o_line[1][1] - o_line[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [o_line[0][0], (o_line[1][1] + o_line[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor

    def columns_coor_medium(self):
        """Looking for the coordinates if there are two X or O in columns. Returns new coordinates or None"""
        columns = 0
        while columns < len(self.state_table[0]):
            x_column = []
            o_column = []
            for lines_ind in range(len(self.state_table)):
                if self.state_table[lines_ind][columns] == 'X':
                    x_column.append([lines_ind + 1, columns])
                elif self.state_table[lines_ind][columns] == 'O':
                    o_column.append([lines_ind + 1, columns])
            if len(x_column) == 2:
                if x_column[1][0] == 3:
                    new_coor = [(x_column[1][0] - x_column[0][0]) - 1, x_column[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [(x_column[1][0] + x_column[0][0]) - 1, x_column[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
            if len(o_column) == 2:
                if o_column[1][0] == 3:
                    new_coor = [(o_column[1][0] - o_column[0][0]) - 1, o_column[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [(o_column[1][0] + o_column[0][0]) - 1, o_column[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
            columns += 1

    def diag_coor_medium(self):
        """Looking for the coordinates if there are two X or O in diagonals. Returns new coordinates or None"""
        main_diag = 0
        alter_diag = -1
        x_main = []
        x_alter = []
        o_main = []
        o_alter = []

        for lines in range(len(self.state_table)):
            if self.state_table[lines][main_diag] == 'X':
                x_main.append([main_diag + 1, main_diag + 1])

            elif self.state_table[lines][main_diag] == 'O':
                o_main.append([main_diag + 1, main_diag + 1])
            # print(f'x_main {x_main}')
            if len(x_main) == 2:
                if x_main[1][1] == 3:
                    new_coor = [(x_main[1][0] - x_main[0][0]) - 1, (x_main[1][1] - x_main[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [x_main[1][0] + x_main[0][0] - 1, (x_main[1][1] + x_main[0][1]) - 1]
                    # print(f'this is{new_coor}')
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
            elif len(o_main) == 2:
                if o_main[1][1] == 3:
                    new_coor = [(o_main[1][0] - o_main[0][0]) - 1, (o_main[1][1] - o_main[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [o_main[1][0] + o_main[0][0] - 1, (o_main[1][1] + o_main[0][1]) - 1]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor

            if self.state_table[lines][alter_diag] == 'X':
                x_alter.append([lines + 1, alter_diag])
            elif self.state_table[lines][alter_diag] == 'O':
                o_alter.append([lines + 1, alter_diag])

            if len(x_alter) == 2:
                if x_alter[1][1] == -3:
                    new_coor = [x_alter[1][0] - x_alter[0][0] - 1, x_alter[1][1] - x_alter[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [x_alter[1][0] + x_alter[0][0] - 1, x_alter[1][1] + x_alter[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor

            elif len(o_alter) == 2:
                if o_alter[1][1] == -3:
                    new_coor = [o_alter[1][0] - o_alter[0][0] - 1, o_alter[1][1] - o_alter[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
                else:
                    new_coor = [o_alter[1][0] + o_alter[0][0] - 1, o_alter[1][1] + o_alter[0][1]]
                    if self.state_table[new_coor[0]][new_coor[1]] == '_':
                        return new_coor
            main_diag += 1
            alter_diag -= 1

    def coor_for_medium(self):
        """Look for the coordinates for level medium of AI: if the game table already has two in row/diagonal/column
        it returns these coordinates else: None"""
        medium_coor_lines = self.rows_coor_medium()
        if medium_coor_lines:
            return medium_coor_lines
        medium_coor_columns = self.columns_coor_medium()
        if medium_coor_columns:
            return medium_coor_columns
        medium_coor_diagonals = self.diag_coor_medium()
        if medium_coor_diagonals:
            return medium_coor_diagonals

    def medium_medium(self):
        """Method which represents the game between two AI(level is medium)"""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            coor = self.coor_for_medium()
            if coor:
                first_comp_move = self.comp_makes_move(medium_coor=coor)
            else:
                first_comp_move = self.comp_makes_move()
            print('Making move level medium')
            print(first_comp_move)
            result = self.checker()
            if result:
                return result

            coor = self.coor_for_medium()
            if coor:
                second_comp_move = self.comp_makes_move(is_X=False, medium_coor=coor)
            else:
                second_comp_move = self.comp_makes_move(is_X=False)
            print('Making move level medium')
            print(second_comp_move)
            result = self.checker()
            if result:
                return result

    def medium_user(self, is_comp_first=True):
        """Method which represents the game between AI(medium) and user"""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            if is_comp_first:
                coor = self.coor_for_medium()
                if coor:
                    first_comp_move = self.comp_makes_move(medium_coor=coor)
                else:
                    first_comp_move = self.comp_makes_move(is_X=True)
                print('Making move level medium')
                print(first_comp_move)
                result = self.checker()
                if result:
                    return result
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=False)
                print(users_move)
                result = self.checker()
                if result:
                    return result

            else:
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=True)
                print(users_move)
                result = self.checker()
                if result:
                    return result

                coor = self.coor_for_medium()
                # print(coor)
                if coor:
                    second_comp_move = self.comp_makes_move(medium_coor=coor, is_X=False)
                else:
                    second_comp_move = self.comp_makes_move(is_X=False)
                print('Making move level medium')
                print(second_comp_move)
                result = self.checker()
                if result:
                    return result

    def minimax(self, player):
        """Method which represents minimax algorithm for TicTacToe. Looking for the best move.
        Returns score and coordinates for the move"""
        maxv = -2
        minv = 2

        px = None
        py = None
        qx = None
        qy = None

        result = self.checker()

        if result:
            if result[0] == 'X':
                return (-1, 0, 0)
            elif result[0] == 'O':
                return (1, 0, 0)
            elif result[0] == 'D':
                return (0, 0, 0)

        if player == 'X':
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.state_table[i][j] == '_':
                        self.state_table[i][j] = 'X'
                        (m, max_i, max_j) = self.minimax('O')
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        self.state_table[i][j] = '_'
            return (minv, qx, qy)

        elif player == 'O':
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.state_table[i][j] == '_':
                        self.state_table[i][j] = 'O'
                        (m, min_i, min_j) = self.minimax('X')
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        self.state_table[i][j] = '_'
            return (maxv, px, py)

    def hard_user(self, is_comp_first=True):
        """Method which represents the game between AI level hard and user"""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            if is_comp_first:
                (m, px, py) = self.minimax('X')
                self.state_table[px][py] = 'X'
                print('Making move level "hard"')
                print(TicTacToe(self.state_table, is_str=False))
                result = self.checker()
                if result:
                    return result
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=False)
                print(users_move)
                result = self.checker()
                if result:
                    return result

            else:
                while True:
                    coordinates = input('Enter the coordinates: ').split()
                    is_right_coor = self.is_right_coordinates(coordinates)
                    if is_right_coor:
                        print(is_right_coor)
                    else:
                        break
                users_move = self.user_makes_move(coordinates, is_X=True)
                print(users_move)
                result = self.checker()
                if result:
                    return result

                (m, px, py) = self.minimax('O')
                self.state_table[px][py] = 'O'
                print('Making move level "hard"')
                print(TicTacToe(self.state_table, is_str=False))
                result = self.checker()
                if result:
                    return result

    def hard_hard(self):
        """Method which represents the game between two AI level hard"""
        self.state_table = self.make_state_table('_________', str_type=True)
        print(TicTacToe(self.state_table, is_str=False))
        while True:
            (m, px, py) = self.minimax('X')
            self.state_table[px][py] = 'X'
            print('Making move level "hard"')
            print(TicTacToe(self.state_table, is_str=False))
            result = self.checker()
            if result:
                return result
            (m, px, py) = self.minimax('O')
            self.state_table[px][py] = 'O'
            print('Making move level "hard"')
            print(TicTacToe(self.state_table, is_str=False))
            result = self.checker()
            if result:
                return result
    def main(self):
        res_user = None
        res_comp = None
        is_right_coor = None
        while True:
            command = input('Input command: ').split()
            if command[0] == 'exit':
                break
            elif len(command) < 3 or len(command) > 3:
                print('Bad parameters!')
            else:
                if command[1] == 'easy':
                    if command[2] == 'easy':
                        print(self.easy_easy())
                    else:
                        print(self.easy_user())
                elif command[1] == 'medium':
                    if command[2] == 'medium':
                        print(self.medium_medium())
                    else:
                        print(self.medium_user())
                elif command[1] == 'hard':
                    if command[2] == 'hard':
                        print(self.hard_hard())
                    else:
                        print(self.hard_user())
                elif command[1] == 'user':
                    if command[2] == 'user':
                        print(self.user_user())
                    elif command[2] == 'easy':
                        print(self.easy_user(is_comp_first=False))
                    elif command[2] == 'medium':
                        print(self.medium_user(is_comp_first=False))
                    elif command[2] == 'hard':
                        print(self.hard_user(is_comp_first=False))


easy_tic = PlayGame('_________')
easy_tic.main()
