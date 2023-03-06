# ChatChess
A python app to play chess against ChatGPT

**This is work in progress, so it has lots bugs/terrible code**

## How to use

1. Save `config.yml.default` as `config.yml`
2. Paste OpenAI API key as `API_key` into `config.yml`

## Settings
### `GPT_Settings` - Settings sent to ChatGPT
- `Tokens_added`: Sets the amount of tokens that ChatGPT can use query. This number will be added to the number of moves played so far. (Set to -1 for a fix amount of tokens ChatGPT can use defined in Max_tokens)
- `Max_tokens`: Sets the maximum amount of tokens ChatGPT can use per query
- `Temperature`: Sets the temperature of ChatGPT (creativity)
