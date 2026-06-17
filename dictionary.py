"""It has a Verdurian dictionary."""
class Dictionary:
    """It's a class for dicts"""
    def __init__(self, to_lang, from_lang, corpus_path):
        self.to_lang = to_lang
        self.from_lang = from_lang
        self.corpus_path = corpus_path
        self.dictionary = {}

        if self.to_lang == "verdurian" and self.from_lang == "english":
            with open(corpus_path, 'r', encoding="utf-8") as file:
                for line in file:
                    array = line.strip().split(" - ")
                    english_word = array[0][1:]
                    if len(array) == 3:
                        verdurian_word = array[2]
                        self.dictionary[english_word] = verdurian_word
        elif self.to_lang == "english" and self.from_lang == "verdurian":
            with open(corpus_path, 'r', encoding="utf-8") as file:
                for line in file:
                    array = line.strip().split(" - ")
                    english_word = array[0][1:]
                    if len(array) == 3:
                        verdurian_word = array[2]
                        self.dictionary[verdurian_word] = english_word

    def lookup(self, word):
        """It looks up a word in the dictionary."""
        if self.dictionary.get(word):
            return self.dictionary[word]
        return word

    def items(self):
        """Returns the whole dictionary."""
        return self.dictionary.items()
