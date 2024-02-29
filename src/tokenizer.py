class Tokenizer:
    def __init__(self, chars: list[str]):
        self.char_to_token = {ch: i for i, ch in enumerate(chars)}
        self.token_to_char = {i: ch for i, ch in enumerate(chars)}

    def encode(self, string: str):
        return [self.char_to_token[ch] for ch in string]

    def decode(self, tokens: list[int]):
        return ''.join([self.token_to_char[token] for token in tokens])