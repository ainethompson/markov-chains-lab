"""Generate Markov text from text files."""

from random import choice

import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path)
    text = contents.read()
    contents.close()

    return text

#print(open_and_read_file('green-eggs.txt'))
"""Generate Markov text from text files."""


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    #contents = open_and_read_file("green-eggs.txt")

    chains = {}

    words = text_string.split()

    words.append(None)

    # for index in range(len(words) -1):
    #     print (words[index], words[index +1])

    for idx in range(len(words) -2):
        key = (words[idx], words[idx + 1])
        value = words[idx +2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    # for key, value in chains.items():
    #     print(f'{key}: {value}')
        #return chains
        #chains[words[word], words[word +1]] = chains.get(words[word + 2])
    return chains

#print(make_chains("green-eggs.txt"))

def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])
    
    #chains = make_chains("green-eggs.txt")

    #words = []

    #for key in chains:
        #new_key = (key[1], random.choice(value))
        #value at random index

    #print(new_key)

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return " ".join(words)

#make_text('chains')

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
