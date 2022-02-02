import random
import sys
from random import shuffle

quotes = sys.argv[1:]

def random_python_quote():
    random.shuffle(quotes)
    return ' '.join(quotes)

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)



# Take user input and randomly returns just one input (Not command-line arguments as I first thought)
# random_user_words = ('')

# user_input = list(map(int,input().split()))

# def random_words():
#   user_input = list(map(int,input().split()))
#   random_index = random.randint(0, len(user_input) -1 )
#   return random_user_words[random_index]

# if __name__ == '__main__':
#   new_sentence = random_words()
#   print(new_sentence)




# BELOW take user input and shuffle the input (Not command-line arguments as I first thought)
# def scramble(sentence):
#   # Split inputted sentence/string into a words list
#   split = sentence.split()  
#   # Shuffles list around
#   shuffle(split)
#   # Returns the list into a string
#   return ' '.join(split)

# words = input('What words would you like to scramble?: ')
# print(scramble(words))


