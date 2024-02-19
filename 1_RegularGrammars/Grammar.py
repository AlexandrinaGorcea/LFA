import random

class Grammar:
    def __init__(self, _Vn: list, _Vt: list, _L: dict, _S: str) -> None:
        self.nonterminals = _Vn
        self.terminals = _Vt
        self.language = _L
        self.start = _S

    def generate_strings(self, num_strings=5) -> list:
        ans = []
        while len(ans) < num_strings:
            current_word = self.start
            while not self.terminal_word(current_word):
                for char in current_word:
                    if not self.terminal_char(char):
                        production = self.__replace(self.language[char])
                        current_word = current_word.replace(char, production, 1)  # Replace only the first occurrence
            if current_word not in ans:
                ans.append(current_word)
        return ans

    def terminal_word(self, word: str) -> bool:
        # Check if all char from word are terminals
        return all(char in self.terminals for char in word)

    def terminal_char(self, char: str) -> bool:
        # Check if char is terminal
        return char in self.terminals

    def __replace(self, value: list) -> str:
        # Choose random from values of dictionary of given char
        return random.choice(value)
