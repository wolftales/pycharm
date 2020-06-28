# write your code here
def print_board():
    # Display is setup:
    '''
    (x: row, y: column)
    (0, 0) (0, 1) (0, 2)
    (1, 0) (1, 1) (1, 2)
    (2, 0) (2, 1) (2, 2)
    '''
    print(f'''---------
| {cells[0][0]} {cells[0][1]} {cells[0][2]} |
| {cells[1][0]} {cells[1][1]} {cells[1][2]} |
| {cells[2][0]} {cells[2][1]} {cells[2][2]} |
---------''')

    # Invert cell Map to match this:
    ''' Check based on GRID pattern: 
        (x: column, y: row)
        (1, 3) (2, 3) (3, 3)
        (1, 2) (2, 2) (3, 2)
        (1, 1) (2, 1) (3, 1)
        '''
    ''' 'Reduced by 1' GRID pattern: 
        (x: column, y: row)
        (0, 2) (1, 2) (2, 2)
        (0, 1) (1, 1) (2, 1)
        (0, 0) (1, 0) (2, 0)'''

def check_valid_move(string):
    move = string.split()
    # print(f'Initial "move": {move}')

    # Validate input
    j = 0
    for i in move:
        if 1 < int(i) > 3:
            return 'Coordinates should be from 1 to 3!'
        if not i.isdigit():
            return 'You should enter numbers!'

        # Display is setup:
        ''' Original matrix
            (x: row, y: column)
            (0, 0) (0, 1) (0, 2)
            (1, 0) (1, 1) (1, 2)
            (2, 0) (2, 1) (2, 2)
            '''
        # Invert cell Map to match this:
        ''' Check based on GRID pattern: 
            (x: column, y: row)
            (1, 3) (2, 3) (3, 3)
            (1, 2) (2, 2) (3, 2)
            (1, 1) (2, 1) (3, 1)
            '''

        # Setting values in list:
        move[j] = int(i)

        j += 1

    # Check if position is free
    # List position = (x - 1) + (9 - (3 * y))
    index = (move[0] - 1) + (9 - (3 * move[1]))
    # print(f'Post loop": {move} type({type(move)}) index = {index}')

    # Convert cartesian coordinates(x, y) to multidimensional list coordinates(i, j)
    # use this formula:
    # i = 3 - y
    # j = x - 1
    # Create a copy of the list
    matrix_coords = list()
    for i in move:
        matrix_coords.append(i)
    # matrix_coords = move  # Bad - Don't 'Pass By Reference'
    # print(f'Before: matrix_coords(i, j) ({matrix_coords}) cartesian_coords(x, y) move({move})')
    matrix_coords[0] = 3 - move[1]
    matrix_coords[1] = move[0] - 1
    # print(f'matrix_coords(i, j) ({matrix_coords}) move = cartesian_coords(x, y) ({move})')
    # print(f'After: matrix_coords: {matrix_coords} = ({matrix_coords[0]}, {matrix_coords[1]}) index = {index}')
    #
    # print(f'Post conversion "move": {move} move[0] = {move[0]} move[1] = {move[1]}')
    # print(f'Convert cartesian coordinates(x, y): {move} to multidimensional list coordinates(i, j): {matrix_coords}')

    global cells

    if cells[matrix_coords[0]][matrix_coords[1]] == 'X' or cells[matrix_coords[0]][matrix_coords[1]] == 'O':
        return 'This cell is occupied! Choose another one!'

    return True

def set_coordinates(string, char):
    if char % 2 == 0:
        player_symbol = 'X'
    else:
        player_symbol = 'O'

    move = string.split()
    # print(f'Initial "move": {move}')

    # Validate input
    j = 0
    for i in move:
        if 1 < int(i) > 3:
            return 'Coordinates should be from 1 to 3!'
        if not i.isdigit():
            return 'You should enter numbers!'

        # Setting values in list:
        move[j] = int(i)

        j += 1

    # Conversion Territory - mapping Carteasian vs matrix
    # Display is setup:
    ''' Original matrix
        (x: row, y: column)
        (0, 0) (0, 1) (0, 2)
        (1, 0) (1, 1) (1, 2)
        (2, 0) (2, 1) (2, 2)
        '''
    # Invert cell Map to match this:
    ''' Check based on GRID pattern: 
        (x: column, y: row)
        (1, 3) (2, 3) (3, 3)
        (1, 2) (2, 2) (3, 2)
        (1, 1) (2, 1) (3, 1)
        '''

    # List position = (x - 1) + (9 - (3 * y))
    index = (move[0] - 1) + (9 - (3 * move[1]))
    # print(f'Post loop": {move} type({type(move)}) index = {index}')

    # Convert cartesian coordinates(x, y) to multidimensional list coordinates(i, j)
    # use this formula:
    # i = 3 - y
    # j = x - 1
    # Create a copy of the list
    matrix_coords = list()
    for i in move:
        matrix_coords.append(i)
    # matrix_coords = move  # Bad - Don't 'Pass by Reference'
    # print(f'Before: matrix_coords(i, j) ({matrix_coords}) cartesian_coords(x, y) move({move})')
    matrix_coords[0] = 3 - move[1]
    matrix_coords[1] = move[0] - 1
    # print(f'matrix_coords(i, j) ({matrix_coords}) move = cartesian_coords(x, y) ({move})')
    # print(f'After: matrix_coords: {matrix_coords} = ({matrix_coords[0]}, {matrix_coords[1]}) index = {index}')
    #
    # print(f'Post conversion "move": {move} move[0] = {move[0]} move[1] = {move[1]}')
    # print(f'Convert cartesian coordinates(x, y): {move} to multidimensional list coordinates(i, j): {matrix_coords}')

    global cells
    cells[matrix_coords[0]][matrix_coords[1]] = player_symbol

    return True


def check_winner():
    global cells
    # Winning Scenarios
    row0 = [cells[0][0], cells[0][1], cells[0][2]]
    row1 = [cells[1][0], cells[1][1], cells[1][2]]
    row2 = [cells[2][0], cells[2][1], cells[2][2]]

    col0 = [cells[0][0], cells[1][0], cells[2][0]]
    col1 = [cells[0][1], cells[1][1], cells[2][1]]
    col2 = [cells[0][2], cells[1][2], cells[2][2]]

    dia0 = [cells[0][0], cells[1][1], cells[2][2]]
    dia1 = [cells[2][0], cells[1][1], cells[0][2]]

    combinations = [row0, row1, row2, col0, col1, col2, dia0, dia1]

    win_count_x = 0
    win_count_o = 0
    blanks_count = 0
    x_count = 0
    o_count = 0

    # Log cell membership
    for cell in cells:
        for i in cell:
            if i == "X":
                x_count += 1
            elif i == "O":
                o_count += 1
            elif i == "_" or i == " ":
                blanks_count += 1
    # print(f'Win X/O: {win_count_x}/{win_count_o} X\'s: {x_count} O\'s: {o_count} blanks: {blanks_count}')

    # Loop to check for win counts - series of 3 somewhere in combinations
    for combination in combinations:
        if combination[0] == combination[1] == combination[2] == "X":
            win_count_x += 1
        elif combination[0] == combination[1] == combination[2] == "O":
            win_count_o += 1

    # if cells[0][0] == 'X' and (win_count_x == 0 and win_count_o == 0) and (
    #         blanks_count > 1 and x_count > 3 and o_count > 3):
    #     return 'Game not finished'
    # elif cells[0][0] == 'X' and (win_count_x == win_count_o == blanks_count == 0):
    #     return 'Draw'
    # elif cells[0][0] == 'X' and (win_count_x == 1 and win_count_o == 0):
    #     return 'X wins'
    # elif cells[0][0] == 'X' and (win_count_o == 1 and win_count_x == 0):
    #     return 'O wins'
    # elif ((x_count - o_count) >= 2 or (o_count - x_count) >= 2) or (win_count_x == 1 and win_count_o == 1):
    #     print(f'{(x_count - o_count) >= 2} or {(o_count - x_count) >= 2} or {win_count_x == 1} and {win_count_o == 1}')
    #     return 'Impossible'
#     print(f'''win_count_x = {win_count_x}
# win_count_o = {win_count_o}
# blanks_count = {blanks_count}
# x_count = {x_count}
# o_count = {o_count}
# ''')
    if win_count_x == 0 and win_count_o == 0 and blanks_count > 0:
        return 'Game not finished'
    elif win_count_x == win_count_o == blanks_count == 0:
        return 'Draw'
    elif win_count_x == 1 and win_count_o == 0:
        return 'X wins'
    elif win_count_o == 1 and win_count_x == 0:
        return 'O wins'
    # elif ((x_count - o_count) >= 2 or (o_count - x_count) >= 2) or (win_count_x == 1 and win_count_o == 1):
    #     print(f'{(x_count - o_count) >= 2} or {(o_count - x_count) >= 2} or {win_count_x == 1} and {win_count_o == 1}')
    #     return 'Impossible'

    return False


# Intial player input

# player_actions = input('Enter cells: ')
# # player_actions = 'XOXOXOXXO'
# # player_actions = 'XXXOO__O_'
# # player_actions = '_X_O_____'
# # player_actions = '_XXOO_OX_'
player_actions = '         '
# '''
# ---------
# |   X X |
# | O O   |
# | O X   |
# ---------
# '''
#
# # print('String Entered:', player_actions)
#
# # Populate cells with player moves
cells = list()
cells = [[i for i in player_actions[x:x + 3]] for x in range(0, len(player_actions), 3)]
# print('Before loop:', [i for i in cells])

print_board()

player_x_or_o = 0  # even = 'X' AND odd = 'O'
rounds = 0

# Loop to verify input
while True:
    player_move = input('Enter the coordinates: ')  # Get player entry
    # player_move = input(f'Enter the coordinates player {"X" if player_x_or_o % 2 == 0 else "O"}: ')  # Get player entry

    # value = 'Test' if 1 == 1 else 'NoTest'

    # result = player_move if check_valid_move(player_move) != False else 'invalid' # Check valid: open, proper entry
    is_valid = check_valid_move(player_move)  # Check valid: open, proper entry

    if is_valid == True:
        # print('Success')
        pass
    else:
        print(f'{is_valid}')
        continue

    set_coordinates(player_move, player_x_or_o)  # Set move

    print_board()  # Display board

    result = check_winner()
    # print(f'result = check_winner(): {result}')

    if result == 'Game not finished':
        # print(f'pop')
        pass
    else:
        print(f'{result}')
        # print(f'poop')
        break

    player_x_or_o += 1  # Alternate players
    rounds += 1

    if rounds > 9:
        print('Draw')
        break

# Output
# print('After loop:', cells)
