## Chess ##
import chess

board = chess.Board()
allMoves = []

def handlePlayerInput(input):
    try:
        board.push_san(input)
        allMoves.append(input)
    except:
        pass

def handleChatInput(input):
    moves = input.split(" ")
    for move in moves:
        try:
            board.push_san(move)
            allMoves.append(move)
            break
        except:
            pass

## ChatGPT ###
import openai

openai.api_key = ""

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
        print("\n", board, "\n")
        handlePlayerInput(input("Make a move: "))
        print("\n", board, "\n")
        handleChatInput(get_gpt_response())