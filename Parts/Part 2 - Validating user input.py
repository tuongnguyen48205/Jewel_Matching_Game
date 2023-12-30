# Created by Tuong Bao Nguyen
# Started 04/04/2023

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

# For the sake of reability, I have split each point into its own chunk of code
# I could put it all into one for loop, but doing so will impact readability.

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
        if key != 'Z' and value % 4 != 0:
            return False
        else:
            continue
    
    # If all the conditions are met, it means that the input was valid and so
    # the function returns True.
    return True
