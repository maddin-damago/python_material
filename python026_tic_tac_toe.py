from random import randrange
theBoard: list[list[str]] = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]

]


def display_board(board: list[list[str]]):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(f"""
            +-------+-------+-------+
            |       |       |       |
            |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
            |       |       |       |
            +-------+-------+-------+
            |       |       |       |
            |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
            |       |       |       |
            +-------+-------+-------+
          """)


def enter_move(board: list[list[str]]):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    freeFields = make_list_of_free_fields(board)
    print("Freefields:", freeFields)
    try:
        userMove = int(input("Enter your move:"))
    except ValueError:
        print("Enter valid field number!")
        enter_move(theBoard)
        return
    position = 0

    if userMove in (1, 4, 7):
        position = 0
    elif userMove in (2, 5, 8):
        position = 1
    elif userMove in (3, 6, 9):
        position = 2
    else:
        print("Chose field within the board!")
        enter_move(theBoard)

    if userMove in [1, 2, 3]:
        if (0, position) in freeFields:
            theBoard[0][position] = "O"
        else:
            print("Pick a free field!")
            enter_move(theBoard)
    elif userMove in [4, 5, 6]:
        if (1, position) in freeFields:
            theBoard[1][position] = "O"
        else:
            print("Pick a free field!")
            enter_move(theBoard)
    elif userMove in [7, 8, 9]:
        if (2, position) in freeFields:
            theBoard[2][position] = "O"
        else:
            print("Pick a free field!")
            enter_move(theBoard)


def make_list_of_free_fields(board: list[list[str]]):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeFields: list[tuple[int, int]] = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                freeFields.append((row, col))
    return freeFields


victory = False


def victory_for(board: list[list[str]], sign: str):
    global victory
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if theBoard[0][0] == sign and theBoard[0][1] == sign and theBoard[0][2] == sign:
        victory = True
    elif theBoard[1][0] == sign and theBoard[1][1] == sign and theBoard[1][2] == sign:
        victory = True
    elif theBoard[2][0] == sign and theBoard[2][1] == sign and theBoard[2][2] == sign:
        victory = True
    elif theBoard[0][0] == sign and theBoard[1][0] == sign and theBoard[2][0] == sign:
        victory = True
    elif theBoard[0][1] == sign and theBoard[1][1] == sign and theBoard[2][1] == sign:
        victory = True
    elif theBoard[0][2] == sign and theBoard[1][2] == sign and theBoard[2][2] == sign:
        victory = True
    elif theBoard[0][0] == sign and theBoard[1][1] == sign and theBoard[2][2] == sign:
        victory = True
    elif theBoard[2][0] == sign and theBoard[1][1] == sign and theBoard[0][2] == sign:
        victory = True

    if victory:
        print("Player won!" if sign == "O" else "Computer won!")


def draw_move(board: list[list[str]]):
    freeFields = make_list_of_free_fields(board)
    print("Freefields:", freeFields)
    compDraw = randrange(1, 10)
    print("Computer picked:", compDraw)

    position = 0
    if compDraw in (1, 4, 7):
        position = 0
    elif compDraw in (2, 5, 8):
        position = 1
    elif compDraw in (3, 6, 9):
        position = 2

    if compDraw in [1, 2, 3]:
        if (0, position) in freeFields:
            theBoard[0][position] = "X"
        else:
            draw_move(theBoard)
    elif compDraw in [4, 5, 6]:
        if (1, position) in freeFields:
            theBoard[1][position] = "X"
        else:
            draw_move(theBoard)
    elif compDraw in [7, 8, 9]:
        if (2, position) in freeFields:
            theBoard[2][position] = "X"
        else:
            draw_move(theBoard)


playerTurn = True

while victory == False:
    freeFields = make_list_of_free_fields(theBoard)
    if not freeFields:
        print("Draw!")
        break
    display_board(theBoard)
    if playerTurn:
        enter_move(theBoard)
        victory_for(theBoard, "O")
        playerTurn = False
        continue
    else:
        draw_move(theBoard)
        victory_for(theBoard, "X")
        playerTurn = True
        continue

display_board(theBoard)
