# Jewel_Matching_Game
A game created by Tuong Bao Nguyen using the programming language of Python.

Information
Matching games are a popular class of games, with titles like Bejeweled and Candy Crush receiving great success over recent years. This game is inspired by games like the previously two mentioned, excepted coded by a solo programmer from the ground up. This is the Jewel Matching Game where your primary objective is to match the jewels in order to clear all of the jewels off the screen, leaving behind a completely blank board. The jewels themselves are denoted by any of the 26 characters in the English alphabet. For this game, you will be prompted to generate a game board ranging in any size from 2x2 to 100x100 where the difficulty increases as the size of the board increases. It is impossible to play a game where the board is less than 2x2, which will be explained later, and rather silly to attempt a game with over 1000 squares despite it being very much possible! 

Controls:
a move is made by selecting a piece and specifying a direction in which it should be move (up, down, left or right). The piece can be selected by specifying its position on the board. To do so, we use a tuple (row, column) where row and column are index values of the row and column on the board that contain a piece. To specify the direction we use a single lower case character as follows: 'u' is up, 'd' is down, 'l' is left and 'r' is right. When playing the game, to make a specific move, input the move in the format ((row, column), direction). For example to move the piece in the top left corner right, you would input the move ((0, 0), r). Now to eliminate a piece on the board, four pieces of the same colour may be eliminated from the board by moving them into a 2x2 square (This is the reason why it is not possible to have a game smaller than 2x2). This 2x2 square will subsequently be eliminated leaving behind a blank 2x2 square. This blank 2x2 square will be immediately filled back up as the pieces directly below will move up, leaving behind a blank square below which will also be filled up when the pieces to right of the newly blank square will fill up the space. This means that after elimination, the blank spaces will always be in the bottom right corner of the board. 

Rules:
The board must contain at least two rows and at least two columns where each row in the board is the same length and each column also the same length. Each jewel is denoted by an upper case letter and the position specified is withing the board and does not contain negative row or column values. The direction argument containes one of the four permitted direction values and cannot go outside of the board. For instance if your piece is in the top row, it cannot move up, if your piece is in the right column, it cannot move right, etc. For each piece present on the board, the number of pieces of that colour is a multiple of 4 for a solvable board where blanks are not included in this requirement. When you make a move, both pieces involved in the move are inside the board. The piece that you move will need to end up next to at least one piece of a similar symbol. That is, if you move a certain piece, a piece either to the right, left, above or below of where it is moved to must be of a similar symbol. Either that or the other piece involved in the move must end up adjacent to at least one other piece which shares a similar symbol. The blank pieces/areas may never be moved.

That is all! Have fun playing the Jewel Matching Game!
