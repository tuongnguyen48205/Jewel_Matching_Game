# Created by Tuong Bao Nguyen
# Started 08/04/2023

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

def make_move(board, position, direction):
    '''
    This function takes three arguments. The first argument is a board which
    is a nested list of lists (same from previous tasks). The second is a 
    position in the form of an (x, y) coordinate point where (0, 0) is the top
    left point and the final argument is a direction as specified in lines 5-8 
    of the code. This function will return a board (nested list of lists) after 
    the move has been completed.
    '''
    
    # The following code is the piece that the player has selected based on
    # the position that they player inputted
    selected_piece = board[position[0]].pop(position[1])

    # The following chunk of code moves the piece, essentially swapping the 
    # piece that the player chose with the piece next to it, depending on which
    # direction the player chose to move.
    if direction == "u":
        swapping_piece = board[position[0] - 1].pop(position[1])
        board[position[0] - 1].insert(position[1], selected_piece)
        board[position[0]].insert(position[1], swapping_piece)           
    elif direction == "d":
        swapping_piece = board[position[0] + 1].pop(position[1])
        board[position[0] + 1].insert(position[1], selected_piece)
        board[position[0]].insert(position[1], swapping_piece)      
    elif direction == "l":
        swapping_piece = board[position[0]].pop(position[1] - 1)
        board[position[0]].insert(position[1] - 1, selected_piece)
        board[position[0]].insert(position[1], swapping_piece)       
    elif direction == "r":
        swapping_piece = board[position[0]].pop(position[1])
        board[position[0]].insert(position[1] + 1, selected_piece)
        board[position[0]].insert(position[1], swapping_piece)
    
    # The following block of code does the final rearrangement of the board. A
    # while loop was chosen as it allows for the iteration to continue even 
    # after the board has been iterated through. This means that if a new 2 x 2
    # square is formed after another 2 x 2 was formed and removed, the while
    # loop would allow for the new 2 x 2 square that formed to be removed also.
    # There will be further details for each individual section.
    i = 0
    while i != len(board[0]) * len(board):
        row_number = -1 
        for row in board:
            column_number = -1
            row_number += 1
            checker = 0
            for jewel in row:
                column_number += 1
                # If the jewel is a gap, represented by 'Z', it cannot be moved
                # so it is skipped using the following if statement.
                if jewel == "Z":
                    pass
                # Below are a series of if and elif statements. Each of these statements
                # play a vital role in determining if a square is formed. They check if the
                # jewel to the left, the jewel directly below, and the jewel directly below
                # and one to the left is the same as the jewel currently being iterated over.
                # If all the if statements are satisfied, it means that a 2 x 2 square has
                # been formed.
                elif jewel == checker:
                    # A few index errors may occur due to trying to index outside the list and
                    # so a try except statement is used. If the jewel chosen is outside the list,
                    # it is impossible for a 2 x 2 square to form and so it will be ignored and 
                    # the loop will continue.
                    try:
                        if board[row_number + 1][column_number] == checker:
                            if board[row_number + 1][column_number - 1] == checker:
                                # The following chunks of code replaces the 2 x 2 square formed with the 'Z' character.
                                # >= 4 was chosen as this means that there are at least 2 rows below where the square
                                # was formed. Now if there are at least 2 rows below where the 2 x 2 square is formed, 
                                # the empty space left behind by the removal of the square can be replaced immediately
                                # by the four jewels directly below where the square was removed
                                if len(board) - row_number >= 4:
                                    board[row_number][column_number] = board[row_number + 2][column_number]
                                    board[row_number + 2][column_number] = "Z"
                                    board[row_number][column_number - 1] = board[row_number + 2][column_number - 1]
                                    board[row_number + 2][column_number - 1] = "Z"
                                    board[row_number + 1][column_number] = board[row_number + 3][column_number]
                                    board[row_number + 3][column_number] = "Z"
                                    board[row_number + 1][column_number - 1] = board[row_number + 3][column_number - 1]
                                    board[row_number + 3][column_number - 1] = "Z"
                                # The 3 means that there is only one row below where the 2 x 2 square was. This means
                                # that only the top half of the square can be replaced immediately by the jewels
                                # directly below. The bottom half is instead replaced by the character "Z".
                                elif len(board) - row_number == 3:
                                    board[row_number][column_number] = board[row_number + 2][column_number]
                                    board[row_number + 2][column_number] = "Z"
                                    board[row_number][column_number - 1] = board[row_number + 2][column_number - 1]
                                    board[row_number + 2][column_number - 1] = "Z"
                                    board[row_number + 1][column_number] = "Z"
                                    board[row_number + 1][column_number - 1] = "Z"
                                # Now if it is less than 3, this means that there are no rows below where the 2 x 2
                                # square was, and so the whole square is replaced by the character "Z"
                                elif len(board) - row_number < 3:
                                    board[row_number][column_number] = "Z"
                                    board[row_number][column_number - 1] = "Z"
                                    board[row_number + 1][column_number] = "Z"
                                    board[row_number + 1][column_number - 1] = "Z"                             
                            else: 
                                pass
                    except Exception:
                        continue
                
                # When the 2 x 2 square is removed, the jewels directly underneath fill in the gaps left
                # behind by the removal of the square. However, this in itself leaves behind an empty
                # square of "Z" characters and if there are even more jewels in the row below where the
                # empty square is, they will need to move up to fill the empty square. This is what the
                # following code does to ensure that the "Z" characters always end up in the bottom of 
                # the board
                row_number2 = -1
                for row2 in board:
                    row_number2 += 1
                    column_number2 = -1
                    for jewel2 in row2:
                        column_number2 += 1
                        try: 
                            if jewel2 == "Z":
                                if board[row_number2 + 1][column_number2] != "Z":
                                    board[row_number2][column_number2] = board[row_number2 + 1][column_number2]
                                    board[row_number2 + 1][column_number2] = "Z"
                        except IndexError:
                            continue
               
                # The following line just checks if the previous jewel iterated over is the
                # same as the one currently being iterated over.
                checker = jewel 

            # Lastly, if an empty square forms in the middle bottom of the board,
            # this final block of code ensures that all the "Z" characters end up
            # in the bottom right corner of the square.
            for row3 in board:
                z_counter = 0
                for jewel3 in row3:
                    if jewel3 == "Z":
                        z_counter += 1
                        row3.remove(jewel3)
                        row3.append("Z")
                        
        i += 1
        
    return board