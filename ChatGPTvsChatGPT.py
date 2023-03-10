## Read Settings ##
import yaml

with open('config.yml', 'r') as file:
    config_file = yaml.safe_load(file)

## Chess ##
import chess
import chess.pgn

board = chess.Board()
allMoves = []


def handlePlayerInput(inputMove):
    move = inputMove
    if len(inputMove) > 2:
        move = inputMove[0].capitalize() + inputMove[1:]
    try:
        board.push_san(move)
        allMoves.append(str(move))
    except:
        if "x" in move and len(move) > 3:
            try:
                move = inputMove[0].lower() + inputMove[1:]
                board.push_san(move)
                allMoves.append(str(move))
                return
            except:
                pass

        printBoard()
        handlePlayerInput(input("Make a move: "))


def handleChatInput(inputMove):
    move = inputMove
    if len(move) > 2:
        move = move[0].capitalize() + move[1:]
    try:
        board.push_san(move)
        allMoves.append(str(move))
    except:
        if "x" in move and len(move) > 3:
            try:
                ModMove = move[0].lower() + move[1:]
                board.push_san(ModMove)
                allMoves.append(str(ModMove))
                return
            except:
                pass
        move = inputMove
        for chars in range(len(move), 0, -1):
            for i in range(len(move)):
                try:
                    board.push_san(move[i:i+chars])
                except:
                    pass

lettersToPeices = {"R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟︎"}

def printBoard():
    chessBoard = str(board)

    peices = "rnbkqpRNBKQP"
    print("  ---------------------------------")
    for no, i in enumerate(range(0, len(chessBoard), 16)):
        column = chessBoard[i:i + 16]
        print(8 - no, "|", end="")

        for field in column:
            if field == " ":
                pass
            elif field == ".":
                print(bcolors.OKBLUE, " ", bcolors.ENDC, end="|")
            elif field in peices:
                if field.capitalize() == field:
                    print(bcolors.OKCYAN, lettersToPeices[field], bcolors.ENDC, end="|")
                elif field.lower() == field:
                    print(bcolors.OKBLUE, lettersToPeices[field], bcolors.ENDC, end="|")
        print("")
    print("  ---------------------------------")
    print("    a   b   c   d   e   f   g   h")


## ChatGPT ###
import openai

openai.api_key = config_file["API_key"]

def get_gpt_response():
    moves = ""

    prompt = f"Reply the next chess move. Only the move. {chess.pgn.Game.from_board(board)}"
    print(len(moves))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=config_file["GPT_Settings"]["Max_tokens"],
        messages=[{"role": "system", "content": prompt}]
    )

    gptMove = response.choices[0]["message"]["content"].replace("\n", "").replace(".", "").replace(" ", "")

    for i in range(len(gptMove)):
        try:
            placeholder = int(gptMove[i])
        except:
            gptMove = gptMove[i:]
            break

    print(gptMove)
    return gptMove


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
    handlePlayerInput("e4")
    handlePlayerInput("e5")

    while True:
        printBoard()
        handleChatInput(get_gpt_response())

        print(chess.pgn.Game.from_board(board))

        if board.is_checkmate():
            print("CHECKMATE!")
            exit()