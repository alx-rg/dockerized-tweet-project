from dictogram import Dictogram
from histogram import word_file, stochastic, histogram, histogram_fileopen
from random import random, randint
from tokens import get_token
from tasks import get_open_and_lower

# word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'doodle']

def markov_chain(word_list):
  new_dictionary = {}
  for index in range(len(word_list) - 1):
    word = word_list[index]
    word_2 = word_list[index +1]
    if word not in new_dictionary:
      adding_word = Dictogram()
      adding_word.add_count(word_2)
      new_dictionary[word] = adding_word
    else:
      new_dictionary[word].add_count(word_2)
  return new_dictionary

def create_sentence(markov, char_length):
    new_sentence = ''
    # convert list to iterator
    iterator_text = iter(markov)
    # the next element is the first element
    first_word = next(iterator_text)
    #start the sentence / makov with the first word
    new_sentence += first_word
    char_limit = char_length
    while len(new_sentence) < char_limit:
        new_sentence_list = new_sentence.split()
        last_word = new_sentence_list[-1]
        last_word_histogram = markov[last_word]
        next_word = last_word_histogram.sample()
        new_sentence += ' ' + next_word
    return new_sentence

if __name__ == "__main__":
    # test_words = histogram_fileopen('testsampletext.txt')
    # test_markov = markov_chain(test_words)
    file_text = get_open_and_lower("words-sample.txt")
    word_list = get_token(file_text)
    # test_markov = markov_chain(['one', 'fish', 'moose', 'one', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'fish', 'moose', 'one', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'dog', 'moose', 'dog', 'moose'])
    test_markov = markov_chain(word_list)
    test_sentence = create_sentence(test_markov , 60)
    print(test_sentence)