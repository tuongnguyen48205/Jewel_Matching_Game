# Created by Tuong Bao Nguyen
# Created on 06/08/2023

import random

#--------------------------------------------------------------
#Custom exceptions:
class MakeAIPlay(Exception):
    pass
class Information(Exception):
    pass
class EndGame(Exception):
    pass
class EndMove(Exception):
    pass
#--------------------------------------------------------------
#Functions:
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

    return "Outstanding move!"
def validate_input(board, position, direction):
    '''
    This function aims to validate the player's input (making sure that the
    board, the position the player selected and the direction the player wishes
    to move are valid). This function takes three arguments. The first argument
    is the board which is a nested list of lists. The second argument is the 
    position that the player selects in the form of an (x, y) coordinate and
    the third argument is the direction argument (the direction the player
    wishes to move their selected piece).
    '''
    
    # The following code between line 26-31 addresses the first point, making
    # sure that the board contains at least two rows and two columns.
    if len(board) < 2:
        return False
    
    for row in board:
        if len(row) < 2:
            return False
    
    # The following code between line 35-37 addresses the second point, making
    # sure that each row in the board has the same length.
    for row2 in board:
        if len(row2) != len(board[0]):
            return False
        
    # The following code between line 41-44 addresses the third point, making
    # sure that each board value is an upper case character.
    for row3 in board:
        for jewel in row3:
            if not jewel.isupper() or len(jewel) != 1:
                return False
            
    # The following code between line 50-55 addresses the fourth point, making
    # sure that the position specified is within the board and does not contain
    # negative row or column values and is an integer value
    if type(position[0]) != int or type(position[1]) != int:
        return False
    elif position[0] > len(board) or position[1] > len(board[0]):
        return False
    elif position[0] < 0 or position[1] < 0:
        return False

    # The following code between line 60-61 addresses the fifth point, making
    # sure that the direction argument containes one of the four permitted 
    # direction values as outlines in lines 5-8 of the code
    if direction not in ("u", "d", "l", "r"):
        return False
    
    # The following code between line 67-77 addresses the sixth point, making
    # sure that for each piece colour present on the board, the number of 
    # pieces of that colour is a multiple of four, where blanks are not
    # considered.
    mydict = {}
    for row4 in board:
        for jewel2 in row4:
            if jewel2 in mydict:
                mydict[jewel2] += 1
            else:
                mydict[jewel2] = 1
    
    for (key, value) in mydict.items():
        if key != ' ' and value % 4 != 0:
            return False
        else:
            continue
    
    # If all the conditions are met, it means that the input was valid and so
    # the function returns True.
    return True
def legal_move(board, position, direction):
    '''
    This function takes three arguments. The first is the board, represented
    as a nested list of lists. The second argument is the position of the 
    player's selected piece in the form of an (x, y) coordinate point where
    (0, 0) is the top left piece. The final argument is the direction of the 
    movement as specified in lines 5-8 of the code. 
    This function aims to validate the movement and will return True if the 
    move is legal (if at least one of the pieces involved in the movement ends
    up adjacent to a piece of the same nature.) Otherwise, it will return 
    False.
    '''
    
    # Note: I will only commennt in depth for the up and left direction as the 
    # down and right direction are essentially the same process, only reversed.
    
    # The following line is the piece that the player chose based on the 
    # position that the player inputted. Also, for the case that the player
    # tries selected an empty space (" ")
    selected_piece = board[position[0]][position[1]]
    if selected_piece == " ":
        return False
    
    # The following block of code tests the up movement
    if direction == "u":
        # If the piece is in the first row, it is impossible for the piece to
        # move up so the function will return False.
        if position[0] == 0:
            return False
        # The following line is the other piece involved in the movement. In
        # this case, the piece directly above.
        swapping_piece = board[position[0] - 1][position[1]]
        # The following line is if a player tries to move a piece into an 
        # empty slot.
        if swapping_piece == " ":
            return False
        try:
            # The following if statement checks if the piece to the left of
            # where the selected piece ends up is the same as the selected
            # piece. 
            if board[position[0] - 1][position[1] - 1] == selected_piece:
                # The rationale behind the following if statement is that if
                # position[1] - 1 is less than 0, it will start indexing from
                # the right hand side of the list. In the case that said piece
                # is the same as the selected piece, it will return True when
                # in reality, it should return False. 
                if position[1] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece to the right of
            # where the selected piece ends up is the same as the selected
            # piece
            if board[position[0] - 1][position[1] + 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece selected by the 
            # player is the same as the other piece involved in the move as if
            # they are both the same piece, then after the move, obviously they 
            # will be next to a piece of the same nature.
            if board[position[0]][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece directly above of
            # where the selected piece ends up is the same as the selected
            # piece.
            if board[position[0] - 2][position[1]] == selected_piece:
                if position[0] - 2 < 0:
                    pass
                else: 
                    return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece to the left
            # of where the other piece involved in the move ends up is the same
            # as the other piece involved in the movement.
            if board[position[0]][position[1] - 1] == swapping_piece:
                # Once again, the reason for the following if statement is 
                # because if position[1] - 1 is less than 0, it will start 
                # indexing from the right hand side of the list, leading to a 
                # possibility of returning True when it should not.
                if position[1] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece to the right of 
            # where the other piece involved in the move ends up is the same as
            # the other piece involved in the movement.
            if board[position[0]][position[1] + 1] == swapping_piece:
                return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece directly below
            # of where the other piece involved in the move ends up is the same
            # as the other piece involved in the movement.
            if board[position[0] + 1][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
        
        # If none of the above conditions are met, it means that the move was
        # illegal and therefore returns False.
        return False
        
    # I have copied and pasted the code above for the down direction but
    # altered it to the fit the down direction
    if direction == "d":
        # If the piece is in the last row, it is impossible for that piece to 
        # move down and so it returns False.
        if position[0] >= len(board) - 1:
            return False
        swapping_piece = board[position[0] + 1][position[1]]    
        if swapping_piece == " ":
            return False
        try:
            if board[position[0] + 1][position[1] - 1] == selected_piece:
                if position[1] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            if board[position[0] + 1][position[1] + 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0]][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0] + 2][position[1]] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0]][position[1] - 1] == swapping_piece:
                if position[1] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            if board[position[0]][position[1] + 1] == swapping_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0] - 1][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
  
        return False

    # The following code is for the left direction
    if direction == "l":
        # If the player selected a piece that is in the left column, it is 
        # impossible for the piece to move to the left and so the function
        # returns False.
        if position[1] == 0:
            return False
        # The following piece of code is for the other piece involved in the 
        # movement, in this case the piece directly to the left of the selected
        # piece
        swapping_piece = board[position[0]][position[1] - 1]
        # The following line is for if the player tries to move a piece into
        # an empty slot.
        if swapping_piece == " ":
            return False
        try:
            # The following if statement checks if the piece directly to the 
            # left of where the selected piece ends up is the same as the 
            # piece selected.
            if board[position[0]][position[1] - 2] == selected_piece:
                # The following if statement is to prevent the possibility of 
                # wrongly returning True due to negative indexing. 
                if position[1] -2 < 0:
                    pass
                else: 
                    return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the two pieces involved in 
            # the movement (the piece to the left of the selected piece) are 
            # the same type of piece. Obviously if they are, the selected piece
            # would end up next to a piece of the same type after movement.
            if board[position[0]][position[1] - 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece directly above
            # of where the selected piece ends up is the same as the piece 
            # selected.
            if board[position[0] - 1][position[1] - 1] == selected_piece:
                # Once again, the following if statemennt is to prevent the
                # possibility of returning True due to negative indexing
                if position[0] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            # The following if statemennt checks if the piece directly below
            # of where the selected piece ends up is the same as the piece
            # selected.
            if board[position[0] + 1][position[1] - 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            # The following if statement checks if the piece directly to the
            # right of where the other piece involved in the movement after the
            # move is the same as the other piece involved in the move.
            if board[position[0]][position[1] + 1] == swapping_piece:
                return True
        except IndexError:
            pass
        try:
            # The following code checks if the piece directly above of where 
            # the other piece involved in the movement after the move is the 
            # same as the other piece involved in the movement.
            if board[position[0] - 1][position[1]] == swapping_piece:
                if position[0] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            # The following code checks if the piece directly below of where
            # the other piece innvolved in the movement after the move is the
            # same as the other piece innvolved in the movement.
            if board[position[0] + 1][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
        
        # If none of the above conditions are met, it means that the move was
        # illegal and so it returns False.
        return False
    
    # I have copied and pasted the code above for the right direction but 
    # altered it to fit the right direction.
    if direction == "r":
        # If the selected piece is in the last column, it is impossible for 
        # that piece to move to the right, and so it returns False.
        if position[1] >= len(board[0]) - 1:
            return False
        swapping_piece = board[position[0]][position[1] + 1]
        if swapping_piece == " ":
            return False
        try:
            if board[position[0]][position[1] + 2] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0]][position[1] + 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0] - 1][position[1] + 1] == selected_piece:
                if position[0] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            if board[position[0] + 1][position[1] + 1] == selected_piece:
                return True
        except IndexError:
            pass
        try:
            if board[position[0]][position[1] - 1] == swapping_piece:
                if position[1] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            if board[position[0] - 1][position[1]] == swapping_piece:
                if position[0] - 1 < 0:
                    pass
                else:
                    return True
        except IndexError:
            pass
        try:
            if board[position[0] + 1][position[1]] == swapping_piece:
                return True
        except IndexError:
            pass
  
        return False

#--------------------------------------------------------------



DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = " "

print("\n------------------------------------------------------------------------------------")
print("                        Welcome to the JEWEL MATCHING GAME!")
print("------------------------------------------------------------------------------------\n")

# The following chunks of code will allow the player to select a variety of
# options including playing the game, exiting the game, making an AI play a
# game or information regarding how to play the game.
valid_option = ("play", "quit", "AI", "info")
play = input('Please type "play" to begin the game or type "AI" to watch an AI play a game\nor type "info" to learn how to play or type "quit" to exit the game: ')
while play not in valid_option:
    play = input("You did not input a valid option. Please choose one of the options above, thank you: ")

try:
    if play == "quit":
        raise EndGame
    elif play == "info":
        raise Information
    elif play == "play":
        pass
    elif play == "AI":
        raise MakeAIPlay
    else:
        print("Error detected, closing game.")
        exit()

# The following code is for if the player wishes to exit the game.
except EndGame:
    print("\n------------------------------------------------------------------------------------")
    print("\nThank you for playing!")
    print("\n------------------------------------------------------------------------------------")
    exit()

# The following is for if the player wishes to read information related to the game   
except Information:
    inform = "Matching games are a popular class of games, with titles like Bejeweled and Candy Crush receiving great success over recent years. This game is inspired by games like the previously two mentioned, excepted coded by a solo programmer from the ground up. This is the Jewel Matching Game where your primary objective is to match the jewels in order to clear all of the jewels off the screen, leaving behind a completely blank board. The jewels themselves are denoted by any of the 26 characters in the English alphabet. For this game, you will be prompted to generate a game board ranging in any size from 2x2 to 100x100 where the difficulty increases as the size of the board increases. It is impossible to play a game where the board is less than 2x2, which will be explained later, and rather silly to attempt a game with over 1000 squares despite it being very much possible!"
    controls = "A move is made by selecting a piece and specifying a direction in which it should be move (up, down, left or right). The piece can be selected by specifying its position on the board. To do so, we use a tuple (row, column) where row and column are index values of the row and column on the board that contain a piece. To specify the direction we use a single lower case character as follows: 'u' is up, 'd' is down, 'l' is left and 'r' is right. When playing the game, to make a specific move, input the move in the format ((row, column), direction). For example to move the piece in the top left corner right, you would input the move ((0, 0), r). Now to eliminate a piece on the board, four pieces of the same colour may be eliminated from the board by moving them into a 2x2 square (This is the reason why it is not possible to have a game smaller than 2x2). This 2x2 square will subsequently be eliminated leaving behind a blank 2x2 square. This blank 2x2 square will be immediately filled back up as the pieces directly below will move up, leaving behind a blank square below which will also be filled up when the pieces to right of the newly blank square will fill up the space. This means that after elimination, the blank spaces will always be in the bottom right corner of the board. You can quit the game at any time by typing 'quit' or reset the board and restart the game by typing 'reset'. You can also get all the information regarding this game at any time by typing 'info'."
    rules = "The board must contain at least two rows and at least two columns where each row in the board is the same length and each column also the same length. Each jewel is denoted by an upper case letter and the position specified is withing the board and does not contain negative row or column values. The direction argument containes one of the four permitted direction values and cannot go outside of the board. For instance if your piece is in the top row, it cannot move up, if your piece is in the right column, it cannot move right, etc. For each piece present on the board, the number of pieces of that colour is a multiple of 4 for a solvable board where blanks are not included in this requirement. When you make a move, both pieces involved in the move are inside the board. The piece that you move will need to end up next to at least one piece of a similar symbol. That is, if you move a certain piece, a piece either to the right, left, above or below of where it is moved to must be of a similar symbol. Either that or the other piece involved in the move must end up adjacent to at least one other piece which shares a similar symbol. The blank pieces/areas may never be moved."
    line_list = []
    print("\n------------------------------------------------------------------------------------\n")
    print("                                   How To Play:")
    print("\nA game created by Tuong Bao Nguyen using the programming language of Python")
    
    print("\nInformation:")
    for word in inform.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nControls:")
    for word in controls.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nRules:")
    for word in rules.split():
        if len(line_list) > 13:
            print(' '.join(line_list))
            line_list = []
        line_list.append(word)
    print(' '.join(line_list))
    line_list = []
    print("\nThat is all! Have fun playing the Jewel Matching Game!")

    print("\n------------------------------------------------------------------------------------") 
    print("\nWould you like to now try a game or exit the program?")
    while True:
        leave_info = input('Type "play" to play a game or type "quit" to exit: ')
        if leave_info == "play":
            break
        elif leave_info == "quit":
            print("\n------------------------------------------------------------------------------------")
            print("\nThank you for playing!")
            print("\n------------------------------------------------------------------------------------")
            exit()
        else:
            continue 


print("\n------------------------------------------------------------------------------------\n")
print("You have chosen to play the game! Now you will need to select your difficulty.")
print("The game is played best if the number of rows equal the number of columns.")
print("Additionally, even though you can make a board of any size, only some sizes can result")
print("in a possible win (if the area of the board is divisible by 4).")
print("\n------------------------------------------------------------------------------------\n")
print("                              Select your Difficulty:\n")

# The following chunk of code will ask the player for how many columns they
# want and ensure that they input a valid value.
columns_number = 0
while columns_number < 2 or columns_number > 100:
    try:
        columns_number = int(input('How many columns would you like? '))
        if columns_number < 2 or columns_number > 100:
            print('You need to input a number between 2 and 100!')
            continue
    except Exception:
        print('You need to input an integer!')
        continue
        
# The following chunk of code will ask the player for how many rows they want
# and ensure that they input a valid value.
row_number = 0
while row_number < 2 or row_number > 100:
    try:
        row_number = int(input('How many rows would you like? '))
        if row_number < 2 or row_number > 100:
            print('You need to input a number between 2 and 100!')
            continue
    except Exception:
        print('You need to input an integer!')
        continue

# The following will detect whether or not the board the player chose is possible
# and whether or not they wish to continue or reselect a difficulty.
while True:
    possible_board = columns_number * row_number
    if possible_board % 4 != 0:
        print("\nIt seems like this board will have no possible solution.\nWould you like to choose a different difficulty?")
        reselect = input('Type "yes" to choose a different difficulty or type "no" to continue anyways. ')
        if reselect == "no":
            break
        elif reselect == "yes":
            columns_number = 0
            while columns_number < 2 or columns_number > 99:
                try:
                    columns_number = int(input('\nHow many columns would you like? '))
                    if columns_number < 2 or columns_number > 99:
                        print('You need to input a number between 2 and 99!')
                        continue
                except Exception:
                    print('You need to input an integer!')
                    continue      
            row_number = 0
            while row_number < 2 or row_number > 99:
                try:
                    row_number = int(input('How many rows would you like? '))
                    if row_number < 2 or row_number > 99:
                        print('You need to input a number between 2 and 99!')
                        continue
                except Exception:
                    print('You need to input an integer!')
                    continue
        else:
            continue      
    else:
        print("\nThis board has a possible solution. Let's begin the game!")
        break
    
print("\n------------------------------------------------------------------------------------")

possible_jewel = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# The following line gets the general layout of the board but used the placeholder character '_'
board_template = [['_'] * columns_number] * row_number 

# The following code will just make a list of possible number of individual jewels
# Step size 4 is chosen because for the game to be possible the number of individual jewels
# must be a multiple of 4. Obvisouly, it would not make sense to generate more than the total
# number of spaces on the board
if possible_board % 4 == 0:
    no_of_jewels = []
    maxnum = int(possible_board / 2)
    for i in range(4, maxnum, 4):
        no_of_jewels.append(i)
    space_counter = 0
    space_list = []

    while True:
        space_choice = random.choice(no_of_jewels)
        space_counter += space_choice
        space_list.append(space_choice)
        if space_counter > possible_board:
            space_counter = 0
            space_list = []
        elif space_counter == possible_board:
            break
        else:
            continue
    # The following code will actually choose the specific jewels
    chosen_jewel = []
    for i  in range(len(space_list)):
        chosen_jewel.append(random.choice(possible_jewel))

    all_jewels_list = []
    index_tracker = -1
    for i in space_list:
        index_tracker += 1
        for j in range(i):
            all_jewels_list.append(chosen_jewel[index_tracker])

    board = []
    board_row = []
    for row in board_template:
        for column in row:
            board_row.append(column)
        board.append(board_row)
        board_row = []
    for row in board:
        for i in range(len(row)):
            selected_jewel = random.choice(all_jewels_list)
            row[i] = selected_jewel
            all_jewels_list.remove(selected_jewel)

# The  following code will place all the randomly selected jewels into the actual board
else:
    board = []
    board_row = []
    for row in board_template:
        for column in row:
            board_row.append(column)
        board.append(board_row)
        board_row = []
    for row in board:
        for i in range(len(row)):
            row[i] = random.choice(possible_jewel)

# Now we print the game board.
original_board = board.copy() 
print(pretty_print(board))

# The following chunk of code is responsible for the actualy game component of the game.
# The while loop is responsible for the game to be carried out and will terminate when 
# the board has been solved.
print("\n------------------------------------------------------------------------------------\n")
print('You can exit the game at any time by typing "quit". For instance, you may get stuck or')
print("there may be no possible solutions. You can also reset the board and restart the game")    
print('at any time by typing "reset". If you are unsure at any point, you may type "info" to')
print("receive all the info regarding this game.\n")

blank_counter = 0

while True:
    try:
        # The following line is if all the jewels have been eliminated leaving behind a blank
        # board, which means that the player has won.
        if blank_counter == possible_board:
            break

        move = input("Make your move in the format ((x-position, y-position), direction): ")
        if move == "quit":
            print("\n------------------------------------------------------------------------------------")
            print("\nThank you for playing!")
            print("\n------------------------------------------------------------------------------------")
            exit()
        elif move == "info":
            inform = "Matching games are a popular class of games, with titles like Bejeweled and Candy Crush receiving great success over recent years. This game is inspired by games like the previously two mentioned, excepted coded by a solo programmer from the ground up. This is the Jewel Matching Game where your primary objective is to match the jewels in order to clear all of the jewels off the screen, leaving behind a completely blank board. The jewels themselves are denoted by any of the 26 characters in the English alphabet. For this game, you will be prompted to generate a game board ranging in any size from 2x2 to 100x100 where the difficulty increases as the size of the board increases. It is impossible to play a game where the board is less than 2x2, which will be explained later, and rather silly to attempt a game with over 1000 squares despite it being very much possible!"
            controls = "A move is made by selecting a piece and specifying a direction in which it should be move (up, down, left or right). The piece can be selected by specifying its position on the board. To do so, we use a tuple (row, column) where row and column are index values of the row and column on the board that contain a piece. To specify the direction we use a single lower case character as follows: 'u' is up, 'd' is down, 'l' is left and 'r' is right. When playing the game, to make a specific move, input the move in the format ((row, column), direction). For example to move the piece in the top left corner right, you would input the move ((0, 0), r). Now to eliminate a piece on the board, four pieces of the same colour may be eliminated from the board by moving them into a 2x2 square (This is the reason why it is not possible to have a game smaller than 2x2). This 2x2 square will subsequently be eliminated leaving behind a blank 2x2 square. This blank 2x2 square will be immediately filled back up as the pieces directly below will move up, leaving behind a blank square below which will also be filled up when the pieces to right of the newly blank square will fill up the space. This means that after elimination, the blank spaces will always be in the bottom right corner of the board. You can quit the game at any time by typing 'quit' or reset the board and restart the game by typing 'reset'. You can also get all the information regarding this game at any time by typing 'info'."
            rules = "The board must contain at least two rows and at least two columns where each row in the board is the same length and each column also the same length. Each jewel is denoted by an upper case letter and the position specified is withing the board and does not contain negative row or column values. The direction argument containes one of the four permitted direction values and cannot go outside of the board. For instance if your piece is in the top row, it cannot move up, if your piece is in the right column, it cannot move right, etc. For each piece present on the board, the number of pieces of that colour is a multiple of 4 for a solvable board where blanks are not included in this requirement. When you make a move, both pieces involved in the move are inside the board. The piece that you move will need to end up next to at least one piece of a similar symbol. That is, if you move a certain piece, a piece either to the right, left, above or below of where it is moved to must be of a similar symbol. Either that or the other piece involved in the move must end up adjacent to at least one other piece which shares a similar symbol. The blank pieces/areas may never be moved."
            line_list = []
            print("\n------------------------------------------------------------------------------------\n")
            print("                                   How To Play:")
            print("\nA game created by Tuong Bao Nguyen using the programming language of Python")
        
            print("\nInformation:")
            for word in inform.split():
                if len(line_list) > 13:
                    print(' '.join(line_list))
                    line_list = []
                line_list.append(word)
            print(' '.join(line_list))
            line_list = []
            print("\nControls:")
            for word in controls.split():
                if len(line_list) > 13:
                    print(' '.join(line_list))
                    line_list = []
                line_list.append(word)
            print(' '.join(line_list))
            line_list = []
            print("\nRules:")
            for word in rules.split():
                if len(line_list) > 13:
                    print(' '.join(line_list))
                    line_list = []
                line_list.append(word)
            print(' '.join(line_list))
            line_list = []
            print("\nThat is all! Have fun playing the Jewel Matching Game!")

            print("\n------------------------------------------------------------------------------------\n") 
        elif move == "reset":
            board = original_board.copy()
            blank_counter = 0
        else:
            # First we interpret the move into a position and direction
            setup = []
            x_position = ''
            y_position = ''
            pos_index = 5
            for char in move:
                if char.isdigit():
                    setup.append(char)
                elif char == ',':
                    setup.append(char)
                elif char == ')':
                    break
            
            for num in setup:
                pos_index += 1
                if num == ',':
                    pos_index = 0
                else:
                    if pos_index >= 5:
                        x_position += num
                    elif pos_index < 5:
                        y_position += num
            position = [int(x_position), int(y_position)]

            for char in move:
                if char.isalpha():
                    direction = char
            
            # Next we check if the player's move was valid or not
            valid = validate_input(board, position, direction)
            if valid == False:
                raise EndMove
            elif valid == True:
                pass

            # Now that we know that the move is valid, we have to check if it is legal
            legal = legal_move(board, position, direction)
            if legal == False:
                raise EndMove
            else:
                pass
    
    
    except EndMove:
        print("That input was not valid. Please try again.")
        pass
    except Exception:
        print("That input was not valid. Please try again.")
        pass



except MakeAIPlay:
