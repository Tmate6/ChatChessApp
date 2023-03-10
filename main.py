## Read Settings ##
import yaml

with open('config.yml', 'r') as file:
    config_file = yaml.safe_load(file)

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
        print(board.legal_moves)
        handlePlayerInput(input("Make a move: "))


def handleChatInput(inputMove):
    print(board.legal_moves)
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
    for i, move in enumerate(allMoves):
        if i % 2 == 0:
            moves += str(int(i / 2 + 1)) + ". " + move + " "
        else:
            moves += move + " "

    print(moves)

    prompt = f"Reply the next chess move. Only the move. {moves}"
    tokens = len(moves) + config_file["GPT_Settings"]["Tokens_added"]

    if tokens > config_file["GPT_Settings"]["Max_tokens"] != 0 or config_file["GPT_Settings"]["Tokens_added"] == -1:
        tokens = config_file["GPT_Settings"]["Max_tokens"]

    print(len(moves))

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=tokens,
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
    while True:
        printBoard()
        handlePlayerInput(input("Make a move: "))

        if board.is_checkmate():
            print("CHECKMATE! Player wins.")
            exit()

        printBoard()
        handleChatInput(get_gpt_response())

        if board.is_checkmate():
            print("CHECKMATE! ChatGPT wins.")
            exit()
