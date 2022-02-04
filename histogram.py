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

def histogram(text_inputed):
  # Open text file, read the file and enter into the 'file' variable  
  file = open(text_inputed, 'r')
  # Open text, input into the 'file' variable 
  text = file.read()
  file.close()
  text = text.lower()
  text_without_punctuation = punctuation(text)
  word_list = text_without_punctuation.split()
  # print(word_list)
  word_list.sort()
  # print(word_list)

  histogram = {}

  for word in word_list:
      if word not in histogram:
          histogram[word] = 1
      else: 
          histogram[word] += 1
  return histogram

histogram_test = histogram('testsampletext.txt')
word_list = word_file('testsampletext.txt')
word_list = word_split(word_list)
# print(word_list)
length_histogram = len(word_list)
# print(length_histogram)

def stochastic():
  dart_random_number = random.randint(1, length_histogram)
  index = 0
  for key in histogram_test:
    index += histogram_test[key]
    if dart_random_number <= index:
      return key
  
def stochastic_test():
  histogram_totals = {}
  for i in range(10000):
    word_picked = stochastic()
    if word_picked in histogram_totals:
      histogram_totals[word_picked] += 1
    else:
      histogram_totals[word_picked] = 1
  return histogram_totals

def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  return histogram[word.lower()]

if __name__ == '__main__':
    print(stochastic_test())

    # histogram_test = histogram('testsampletext.txt')
    # print(histogram_test)
    # words_test = unique_words(histogram_test)
    # print(words_test)s
    # count_test = frequency('fish', histogram_test)
    # print(count_test)

