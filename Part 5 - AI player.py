# Created by Tuong Bao Nguyen
# Started 12/04/2023

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

def ai_player(board):
    '''
    This function uses an 'AI' to solve a board that the player inputs. The 
    function takes one argumment 'board', in the form of a nested list of 
    lists. The function returns a list of positions and moves that should
    (hopefully) solve the puzzle.
    '''
    
    ai_move = []  # This is the list of moves and positions that the ai returns
    
    # The following while loop makes it so that the ai will continue until the 
    # board has been solved. Otherwise, after many iterations, if the ai is 
    # unable to solve the board, it could possibly mean that the board is 
    # unsolvable so no sequence exists that would solve the board, returning 
    # None
    counter = 0
    while True:
        counter += 1
        end_count = 0
        if counter == len(board) * len(board[0]):
            return None
        for row in board:
            for jewel in row:
                if jewel == "Z":
                    end_count += 1
        if end_count == len(board) * len(board[0]):
            break
  
        # Firstly, we list out every single possible move that can be made.
        # However, if there is an empty gap represented by the "Z" character,
        # obviously, it cannot be moved and so it is passed.
        # Admittedly, this is far from being the most efficient AI.
        movelist = []
        row_counter = -1
        for row2 in board:
            row_counter += 1
            column_counter = -1
            for jewel2 in row2:
                column_counter += 1
                position = (row_counter, column_counter)
                if jewel2 == "Z":
                    pass
                elif position[0] == 0 and position[1] == 0:
                    movelist.append((position, 'r'))
                    movelist.append((position, 'd'))
                elif position[0] == 0 and position[1] == len(row2) - 1:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'd'))
                elif position[1] == 0 and position[0] == len(board) - 1:
                    movelist.append((position, 'r'))
                    movelist.append((position, 'u'))
                elif position[1] == len(row2) - 1 and position[0] == len(board) - 1:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'u'))       
                elif position[0] == 0:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'r'))
                    movelist.append((position, 'd'))
                elif position[1] == 0:
                    movelist.append((position, 'r'))
                    movelist.append((position, 'd'))
                    movelist.append((position, 'u'))
                elif position[1] == len(row2) - 1:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'd'))
                    movelist.append((position, 'u'))
                elif position[0] == len(board) - 1:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'r'))
                    movelist.append((position, 'u'))
                else:
                    movelist.append((position, 'l'))
                    movelist.append((position, 'r'))
                    movelist.append((position, 'u'))
                    movelist.append((position, 'd'))
                 
        # To make the AI more efficient, each move in the list of every single
        # possible move is ran through the legal_move function which removes
        # all illegal moves, leaving behind only the moves that are valid, 
        # which makes the AI more efficient by only testing the possible moves
        # rather than every single combination.
        for position, direction in movelist:
            possible_move = legal_move(board, position, direction)
            if possible_move is False:
                movelist.remove((position, direction))
    
        # Every single possible move is then ran through the make_move function
        # which returns a new board based on the move that was made. Each board 
        # will be different and unique depending on the move made. A tally is
        # used to keep track of all the unique moves and corresponding board.
        # This AI uses a point system to determine which move is the best move
        # to make. The way that this point system works is by counting the 
        # number of empty gaps ("Z") present in each new board that results 
        # from every single move being made. This new board and its 
        # corresponding number of points is also placed into the tally. 
        tally = []
        for new_position, new_direction in movelist:
            board2 = []
            for row in board:
                board2.append(row.copy())  
            newboard = make_move(board2, new_position, new_direction)
            z_counter = 0
            for row in newboard:
                for jewel in row:
                    if jewel == "Z":
                        z_counter += 1
            tally.append((z_counter, newboard, (new_position, new_direction)))
        
        # Now that we have the all moves, its board and corresponding number of 
        # points tallied, the ai determines the best move to make based on 
        # which move would result in the greatest number of points (the 
        # greatest number of empty gaps). The AI then uses the board produced
        # by doing this 'best move' and the whole function starts all over 
        # again using the new board until the entire board is empty.
        sorted_tally = sorted(tally, reverse = True)
        ai_move.append(sorted_tally[0][2])
        board = sorted_tally[0][1]
    
    return ai_move

    
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
    # tries selected an empty space ("Z")
    selected_piece = board[position[0]][position[1]]
    if selected_piece == "Z":
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
        if swapping_piece == "Z":
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
        if swapping_piece == "Z":
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
        if swapping_piece == "Z":
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
        if swapping_piece == "Z":
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
        
    
def make_move(board2, position, direction):
    '''
    This function takes three arguments. The first argument is a board which
    is a nested list of lists (same from previous tasks). The second is a 
    position in the form of an (x, y) coordinate point and the final argument
    is a direction as specified in lines 5-8 of the code. 
    This function will return a board (nested list of lists) after the move
    has been completed.
    '''
    # The following code is the piece that the player has selected based on
    # the position that they player inputted
    selected_piece = board2[position[0]].pop(position[1])

    # The following chunk of code moves the piece, essentially swapping the 
    # piece that the player chose with the piece next to it, depending on which
    # direction the player chose to move.
    if direction == "u":
        swapping_piece = board2[position[0] - 1].pop(position[1])
        board2[position[0] - 1].insert(position[1], selected_piece)
        board2[position[0]].insert(position[1], swapping_piece)           
    elif direction == "d":
        swapping_piece = board2[position[0] + 1].pop(position[1])
        board2[position[0] + 1].insert(position[1], selected_piece)
        board2[position[0]].insert(position[1], swapping_piece)      
    elif direction == "l":
        swapping_piece = board2[position[0]].pop(position[1] - 1)
        board2[position[0]].insert(position[1] - 1, selected_piece)
        board2[position[0]].insert(position[1], swapping_piece)       
    elif direction == "r":
        swapping_piece = board2[position[0]].pop(position[1])
        board2[position[0]].insert(position[1] + 1, selected_piece)
        board2[position[0]].insert(position[1], swapping_piece)
    
    # The following block of code does the final rearrangement of the board. A
    # while loop was chosen as it allows for the iteration to continue even 
    # after the board has been iterated through. This means that if a new 2 x 2
    # square is formed after another 2 x 2 was formed and removed, the while
    # loop would allow for the new 2 x 2 square that formed to be removed also.
    # There will be further details for each individual section.
    i = 0
    while i != len(board2[0]) * len(board2):
        row_number = -1 # This variable is -1 as the first row has index 0
        for row in board2:
            column_number = -1 # This variable is -1 as the first column has index 0
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
                        if board2[row_number + 1][column_number] == checker:
                            if board2[row_number + 1][column_number - 1] == checker:
                                # The following chunks of code replaces the 2 x 2 square formed with the 'Z' character.
                                # >= 4 was chosen as this means that there are at least 2 rows below where the square
                                # was formed. Now if there are at least 2 rows below where the 2 x 2 square is formed, 
                                # the empty space left behind by the removal of the square can be replaced immediately
                                # by the four jewels directly below where the square was removed
                                if len(board2) - row_number >= 4:
                                    board2[row_number][column_number] = board2[row_number + 2][column_number]
                                    board2[row_number + 2][column_number] = "Z"
                                    board2[row_number][column_number - 1] = board2[row_number + 2][column_number - 1]
                                    board2[row_number + 2][column_number - 1] = "Z"
                                    board2[row_number + 1][column_number] = board2[row_number + 3][column_number]
                                    board2[row_number + 3][column_number] = "Z"
                                    board2[row_number + 1][column_number - 1] = board2[row_number + 3][column_number - 1]
                                    board2[row_number + 3][column_number - 1] = "Z"
                                # The 3 means that there is only one row below where the 2 x 2 square was. This means
                                # that only the top half of the square can be replaced immediately by the jewels
                                # directly below. The bottom half is instead replaced by the character "Z".
                                elif len(board2) - row_number == 3:
                                    board2[row_number][column_number] = board2[row_number + 2][column_number]
                                    board2[row_number + 2][column_number] = "Z"
                                    board2[row_number][column_number - 1] = board2[row_number + 2][column_number - 1]
                                    board2[row_number + 2][column_number - 1] = "Z"
                                    board2[row_number + 1][column_number] = "Z"
                                    board2[row_number + 1][column_number - 1] = "Z"
                                # Now if it is less than 3, this means that there are no rows below where the 2 x 2
                                # square was, and so the whole square is replaced by the character "Z"
                                elif len(board2) - row_number < 3:
                                    board2[row_number][column_number] = "Z"
                                    board2[row_number][column_number - 1] = "Z"
                                    board2[row_number + 1][column_number] = "Z"
                                    board2[row_number + 1][column_number - 1] = "Z"                             
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
                for row2 in board2:
                    row_number2 += 1
                    column_number2 = -1
                    for jewel2 in row2:
                        column_number2 += 1
                        try: 
                            if jewel2 == "Z":
                                if board2[row_number2 + 1][column_number2] != "Z":
                                    board2[row_number2][column_number2] = board2[row_number2 + 1][column_number2]
                                    board2[row_number2 + 1][column_number2] = "Z"
                        except IndexError:
                            continue
               
                # The following line just checks if the previous jewel iterated over is the
                # same as the one currently being iterated over.
                checker = jewel 

            # Lastly, if an empty square forms in the middle bottom of the board,
            # this final block of code ensures that all the "Z" characters end up
            # in the bottom right corner of the square.
            for row3 in board2:
                z_counter = 0
                for jewel3 in row3:
                    if jewel3 == "Z":
                        z_counter += 1
                        row3.remove(jewel3)
                        row3.append("Z")
                        
        i += 1
        
    return board2