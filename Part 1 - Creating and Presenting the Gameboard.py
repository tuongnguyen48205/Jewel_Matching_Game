# The following chunk of code will ask the player for how many columns they
# want and ensure that they input a valid value.
columns_number = 0
while columns_number < 2 or columns_number > 99:
    try:
        columns_number = int(input('How many columns would you like? '))
        if columns_number < 2 or columns_number > 99:
            print('You need to input a number between 2 and 99!')
            continue
    except Exception:
        print('You need to input an integer!')
        continue
        
# The following chunk of code will ask the player for how many rows they want
# and ensure that they input a valid value.
row_number = 0
while row_number < 2 or row_number > 99:
    try:
        row_number = int(input('How many rows would you like? '))
        if row_number < 2 or columns_number > 99:
            print('You need to input a number between 2 and 99!')
            continue
    except Exception:
        print('You need to input an integer!')
        continue

# The following chunk of code will ask the player to put in what type of jewel
# they want (letter) and ensure that it is valid.
jewel = 'Placeholder'
while jewel == 'Placeholder':
    jewel = input('Please input a letter between A-Y: ')
    if len(jewel) != 1 or not jewel.isalpha():
        jewel = 'Placeholder'
 
# The following line of code will create what gets put into the board argument 
# for the pretty_print(function)
board = [[jewel.upper()] * columns_number] * row_number


def pretty_print(board):
    '''
    This function prints out a neat game board for the player. The function
    takes one argument (board) which takes the values that the player was 
    previously prompted to input, creating a board based on these values.
    Otherwise, it can also be accessed directly by putting in an argument in
    the following format ([['jewel']*number_of_columns]*number_of_rows]). For
    example pretty_print([['B']*3]*5).
    '''
    
    gamelist = []  # This will store the lists that make up the game board
    
    # The following code is for generating the title and the first two rows
    # of the board (Column number and hyphen border)
    toprow_list = [' ', ' ', ' ']
    for i in range(len(board[0])):
        if i < 10:
            toprow_list.append(str(i))
            toprow_list += 2 * ' '
        elif i >= 10:
            toprow_list.append(str(i))
            toprow_list.append(' ')
            
    toprow = ''.join(toprow_list)
    empty_space = round((len(toprow) - len("JEWEL MATCHING GAME")) / 2)
    print(f'\n{empty_space * " "}--JEWEL MATCHING GAME--{empty_space * " "}')
    print(toprow)
    print('   ' + '-' * (len(toprow) - 3))
 
    # The following code is for generating the rest of the board including
    # the row labels on the left hand side
    counter = 0
    for row in board:
        row2 = row.copy()
        row2.append("")
        if counter < 10:
            row2.insert(0, f' {counter}|')
        elif counter >= 10:
            row2.insert(0, f'{counter}|')
        gamelist.append(row2)
        counter += 1
         
    # Finally, we print out the board in a nice and readable fashion
    for gameline in gamelist:
        print('  '.join(gameline[0:1]) + '  '.join(gameline[1:]))
    print("")

    pass
    
print(pretty_print(board))
