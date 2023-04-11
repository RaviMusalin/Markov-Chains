"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    return contents    


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
        
    # your code goes here
    words = text_string.split()
    
    for word in range(0, len(words) - 2):
        if (words[word],words[word + 1]) not in chains:
            chains.setdefault((words[word], words[word + 1]), [])
            chains[(words[word], words[word + 1])] = [words[word + 2]]
        elif (words[word],words[word + 1]) in chains:
            chains[(words[word], words[word + 1])].append(words[word + 2])
    
    return chains
        


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    
    for key in chains:
        words.extend(sorted(key), chains.get(key))
    print(words)
    # testing = choice(list([chains.items()]))
    # testing = choice(list(chains.keys())) 
    # words.extend(testing)
    # print(words)

    # Get a random word from the list of word that follow 

    # Use second word in key and radnom word to make new key, pull a random word out of resulting list

    return #' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)


# print(random_text)
