# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        """
        Initializes the Anagram class with the given word.
        """
        self.word = word.lower()

    def match(self, word_list):
        """
        Takes a list of words and returns a list of anagrams from the list that match the initialized word.
        """
        # Sort the letters in the initialized word for comparison
        sorted_word = sorted(self.word)

        # Find and return matching anagrams from the word_list
        return [candidate for candidate in word_list if sorted(candidate.lower()) == sorted_word]


if __name__ == "__main__":
    listen = Anagram("listen")
    word_list = ['enlists', 'google', 'inlets', 'banana']
    print(listen.match(word_list))  # Output: ['inlets']
