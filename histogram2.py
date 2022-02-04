
from __future__ import print_function
import random

def punctuation(text):
  punct = '''"\.?@#$%^&*_~='',!()-[]{}\;:<>"'''
  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

def word_file(text_inputed):
  file = open(text_inputed, 'r')
  text = file.read()
  file.close()
  text = text.lower()
  text = punctuation(text)
  return text

def word_split(text_inputed):
  # print(f"word before getting split : {text_inputed}")
  word_list = text_inputed.split()
  # print(f"word AFTER getting split : {word_list}")
  return word_list


def histogram(chosen_text):
  file = open(chosen_text, 'r')
  text = file.read()
  file.close()
  text = text.lower()
  text = punctuation(text)

  split_words = text.split()
  # print(split_words)

  histogram = []

  for words in split_words:
    found = False
    for tuple in histogram:
      if tuple[0] == words:
        number = tuple[1]
        number += 1
        histogram.remove(tuple)
        histogram.append((words, number))
        found = True
        break
    if found is False:
      histogram.append((words, 1))

  return histogram

def stochastic(chosen_text):
  open_file = word_file(chosen_text)
  word_count = word_split(open_file)
  histogram_list = histogram(chosen_text)
  dart_random_number = random.randint(1, len(word_count))
  
  index = 0
  for key in histogram_list:
    index += histogram_list[key]
    if dart_random_number <= index:
      return key

def punctuation(text):
  punct = '''"\.?@#$%^&*_~='',!()-[]{\}\;:<>"'''

  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

def unique_words(histogram):
  return len(histogram)

def frequency(histogram, word):
  for tuple in histogram:
    if tuple[0] == word.lower():
      return tuple[1]

if __name__ == '__main__':
  
  print_stochastic = stochastic("testsampletext.txt")
  print(print_stochastic)

  print_historgram = histogram("testsampletext.txt")
  print(print_historgram)
  length_historgram = unique_words(print_historgram)
  print(length_historgram)
  word_historgram = frequency(print_historgram, 'fish')
  print(word_historgram)