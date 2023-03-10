# ChatChess
A python app to play chess with ChatGPT

**This is work in progress, so it has lots bugs/terrible code**

## How to use

1. Save `config.yml.default` as `config.yml`
2. Paste OpenAI API key as `API_key` into `config.yml`

## Settings
- `GPT_Settings`: Settings sent to ChatGPT
    - `Max_tokens`: Sets the maximum amount of tokens ChatGPT can use per query
- `ChatGPT_ChatGPT`: Options for ChatGPT vs ChatGPT games
    - `Output`: Settings regarding printing
        - `Print_debug`: Print debug info - **Options:** `true` / `false`
        - `Print_board`: Print chessboard - **Options:** `true` / `false`
        - `Print_PGN`: Print game in PGN format - **Options:** `true` / `end` / `false`
        
## View games

I upload some ChatGPT vs ChatGPT games to https://lichess.org/@/chat_chess
