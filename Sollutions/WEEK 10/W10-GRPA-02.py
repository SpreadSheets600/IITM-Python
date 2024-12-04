class StringManipulation:
    def __init__(self, words: list):
        self.words = words

    def total_words(self) -> int:
        return len(self.words)

    def count(self, some_word: str) -> int:
        return self.words.count(some_word)

    def words_of_length(self, length: int) -> list:
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char: str) -> list:
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self) -> str:
        return max(self.words, key=len)

    def palindromes(self) -> list:
        return [word for word in self.words if word == word[::-1]]