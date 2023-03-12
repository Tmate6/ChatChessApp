## Read Settings ##
import yaml

with open('config.yml', 'r') as file:
    config_file = yaml.safe_load(file)

## Chess ##
import chess
import chess.pgn

board = chess.Board()

noOfFails = 0


def handleChatInput(inputMove):
    global noOfFails
    move = inputMove
    if len(move) > 2:
        move = move[0].capitalize() + move[1:]

    try:
        board.push_san(move)
        printDebug("move_normal")
        noOfFails = 0
        return
    except:
        pass

    try:
        ModMove = move[0].lower() + move[1:]
        board.push_san(ModMove)
        printDebug("move_lower")
        noOfFails = 0
        return
    except:
        pass

    move = inputMove
    for chars in range(len(move), 0, -1):
        for i in range(len(move)):
            try:
                board.push_san(move[i:i + chars])
                printDebug(str("move_scan: " + str(move[i:i + chars])))
                noOfFails = 0
                return
            except:
                pass

    printDebug("move_FAIL")

    if not board.is_checkmate() and noOfFails <= config_file["GPT_Settings"]["Max_fails"]:
        noOfFails += 1
        handleChatInput(get_gpt_response(inputMove))
    elif noOfFails >= config_file["GPT_Settings"]["Max_fails"]:
        print(f'Max amount of failes reached ({config_file["GPT_Settings"]["Max_fails"]})')
        exit()


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


def get_gpt_response(illegalMove):
    if board.turn == chess.WHITE:
        color = "white"
    else:
        color = "black"

    if illegalMove:
        if board.is_check():
            prompt = f"Reply next chess move as {color}. You are in check. Play one of these: {str(board.legal_moves)[36:-2]}. Only say the move. {str(chess.pgn.Game.from_board(board))[93:-2]}"

        else:
            prompt = f"Reply next chess move as {color}. Play one of these: {str(board.legal_moves)[36:-1]}. Only say the move. {str(chess.pgn.Game.from_board(board))[93:-2]}"
    else:
        prompt = f"Reply next chess move as {color}. Only say the move. {str(chess.pgn.Game.from_board(board))[93:-2]}"

    printDebug(str("\n" + prompt))
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

    printDebug(gptMove)
    return gptMove


## Mainloop ##
from datetime import date

today = date.today()


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


def printDebug(printInput):
    if config_file["ChatGPT_ChatGPT"]["Output"]["Print_debug"]:
        print(printInput)


def printPGN(val):
    if config_file["ChatGPT_Player"]["Output"]["Print_PGN"] == val:
        game = chess.pgn.Game.from_board(board)
        game.headers["Event"] = config_file["ChatGPT_ChatGPT"]["PGN"]["Event"]
        game.headers["Date"] = today.strftime("%d.%m.%Y")
        game.headers["White"] = "ChatGPT"
        game.headers["Black"] = "ChatGPT"
        print(f"\nPGN:\n{game}")


if __name__ == "__main__":
    board.push_san("e4")
    board.push_san("e5")

    print(bcolors.OKBLUE, "ChatChess", bcolors.ENDC)
    while True:
        if config_file["ChatGPT_ChatGPT"]["Output"]["Print_board"]:
            printBoard()
        handleChatInput(get_gpt_response(""))
        printPGN("true")

        if board.is_checkmate():
            print("CHECKMATE!")
            printPGN("end")
            exit()
