# Created by Tuong Bao Nguyen
# Created on 06/08/2023

#--------------------------------------------------------------
#Custom exceptions:
class MakeAIPlay(Exception):
    pass
class Information(Exception):
    pass
class EndGame(Exception):
    pass
#--------------------------------------------------------------



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
        print("AI")
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
    controls = "a move is made by selecting a piece and specifying a direction in which it should be move (up, down, left or right). The piece can be selected by specifying its position on the board. To do so, we use a tuple (row, column) where row and column are index values of the row and column on the board that contain a piece. To specify the direction we use a single lower case character as follows: 'u' is up, 'd' is down, 'l' is left and 'r' is right. When playing the game, to make a specific move, input the move in the format ((row, column), direction). For example to move the piece in the top left corner right, you would input the move ((0, 0), r). Now to eliminate a piece on the board, four pieces of the same colour may be eliminated from the board by moving them into a 2x2 square (This is the reason why it is not possible to have a game smaller than 2x2). This 2x2 square will subsequently be eliminated leaving behind a blank 2x2 square. This blank 2x2 square will be immediately filled back up as the pieces directly below will move up, leaving behind a blank square below which will also be filled up when the pieces to right of the newly blank square will fill up the space. This means that after elimination, the blank spaces will always be in the bottom right corner of the board."
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
print("                              Select your Difficulty:")

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