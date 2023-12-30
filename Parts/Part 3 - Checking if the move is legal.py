# Created by Tuong Bao Nguyen
# Started 08/04/2023

DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"
BLANK_PIECE = "Z"

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
