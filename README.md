# ChatChess
A python app to play chess with ChatGPT

***A package for this will be published soon***

**This is work in progress, so it has lots bugs/terrible code**

## How to use

1. Save `config.yml.default` as `config.yml`
2. Paste OpenAI API key as `API_key` into `config.yml`

## Settings
- `GPT_Settings`: Settings sent to ChatGPT
    - `Max_tokens`: Sets the maximum amount of tokens ChatGPT can use per query
    - `Max_fails`: Sets the maximum times to resend query to ChatGPT on failed move <br/><br/>
- `ChatGPT_ChatGPT`: Options for ChatGPT vs ChatGPT games
    - `PGN`: Settings regarding PGN
        - `Event`: Set the Event in the PGN
    - `Output`: Settings regarding printing
        - `Print_debug`: Print debug info - **Options:** `true` / `false`
        - `Print_board`: Print chessboard - **Options:** `true` / `false`
        - `Print_PGN`: Print game in PGN format - **Options:** `true` / `end` / `false` <br/><br/>
- `ChatGPT_Player`: Options for ChatGPT vs Player games
    - `PGN`: Settings regarding PGN
        - `Player_name`: Set the Player name in the PGN
        - `Event`: Set the Event in the PGN
    - `Output`: Settings regarding printing
        - `Print_debug`: Print debug info - **Options:** `true` / `false`
        - `Print_board`: Print chessboard - **Options:** `true` / `false`
        - `Print_PGN`: Print game in PGN format - **Options:** `true` / `end` / `false` <br/><br/>
        
## View games

I upload some ChatGPT games to https://lichess.org/@/chat_chess
