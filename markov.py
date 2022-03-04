from dictogram import Dictogram
from histogram import word_file, stochastic, histogram, histogram_fileopen
from random import random, randint

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

# def word_frequency(hist):
#     count = 0 
#     dic = histogram(hist)
#     for key in dic:
#         count += dic[key]

#     dart_random_number = random.randint(1, count)
#     index = 0
#     for key in dic:
#       index += dic[key]
#       if dart_random_number <= index:
#         return key

# def next_word(word_list, word):
#   inner_dictionnary = word_list[word]
#   random_word = word_frequency(inner_dictionnary)
#   return random_word

# def sentences(word_list):
#     word_1 = list(word_list.keys())[0]
#     word_2 = next_word(word_list, word_1)
#     new_sentence = word_1 + ' ' + word_2 + ' '
#     prev_word = word_2

#     for word in range(0, random.randint(1, 101)):
#         new_word = next_word(word_list, prev_word)
#         prev_word = new_word
#         new_sentence += new_word + ' '
#     return new_sentence

def create_sentence(markov):
    new_sentence = ''
    # convert list to iterator
    iterator_text = iter(markov)
    # the next element is the first element
    first_word = next(iterator_text)
    #start the sentence / makov with the first word
    new_sentence += first_word
    limit = 75
    while len(new_sentence) < limit:
        new_sentence_list = new_sentence.split()
        last_word = new_sentence_list[-1]
        last_word_histogram = markov[last_word]
        next_word = last_word_histogram.sample()
        new_sentence += ' ' + next_word
    return new_sentence

if __name__ == "__main__":
    # test_words = histogram_fileopen('testsampletext.txt')
    # test_markov = markov_chain(test_words)
    test_markov = markov_chain(['one', 'fish', 'moose', 'one', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'fish', 'moose', 'one', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'dog', 'moose', 'dog', 'moose'])
    test_sentence = create_sentence(test_markov)

    print(test_sentence)