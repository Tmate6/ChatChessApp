## Chess ##
import chess

board = chess.Board()
allMoves = []

def handlePlayerInput(inputMove):
    move = inputMove
    if len(inputMove) > 2:
        move = inputMove[0].capitalize() + inputMove[1:]
    try:
        board.push_san(move)
        allMoves.append(move)
    except:
        print("\n", board, "\n")
        print(board.legal_moves)
        handlePlayerInput(input("Make a move: "))

def handleChatInput(input):
    moves = input.split(" ")
    for move in moves:
        if len(move) > 2:
            move = move[0].capitalize() + move[1:]
        try:
            board.push_san(move)
            allMoves.append(move)
            break
        except:
            pass

def printBoard():
    chessBoard = str(board)

    peices = "rnbkqpRNBKQP"
    print("  ---------------------------------")
    for no, i in enumerate(range(0,len(chessBoard),16)):
        column = chessBoard[i:i+16]
        print(8-no, "|", end="")

        for field in column:
            if field == " ":
                pass
            elif field == ".":
                print(bcolors.OKBLUE, " ", bcolors.ENDC, end="|")
            elif field in peices:
                if field.capitalize() == field:
                    print(bcolors.OKBLUE, field, bcolors.ENDC, end="|")
                else:
                    print(bcolors.OKCYAN, field, bcolors.ENDC , end="|")
        print("")
    print("  ---------------------------------")
    print("    a   b   c   d   e   f   g   h")

## ChatGPT ###
import openai

openai.api_key = "" # Paste API key here

def get_gpt_response():
    moves = ""
    for i, move in enumerate(allMoves):
        if i%2 == 0:
            moves += str(int(i/2+1)) + ". " +  move + " "
        else:
            moves += move + " "
        print(move)

    print(moves)

    prompt = f"Respond chess. {moves}"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.2,
    )
    print(response.choices[0].text.strip())
    gpt_move = response.choices[0].text.strip()
    return gpt_move

## Mainloop ##

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":
    print(bcolors.OKBLUE, "ChatChess", bcolors.ENDC)
    while True:
        printBoard()
        handlePlayerInput(input("Make a move: "))
        printBoard()
        handleChatInput(get_gpt_response())
