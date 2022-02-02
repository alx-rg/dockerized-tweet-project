import random

def punctuation(text):
  punct = '''"\.?@#$%^&*_~='',!()-[]{}\;:<>"'''

  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

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

# histogram_test = histogram('testsampletext.txt')
# length_histogram = len(histogram_test)

def stochastic():

  random_dart = random.randint(1, length_histogram)
  print(random_dart)
  pass
  

def unique_words(histogram):
  return len(histogram)

def frequency(word, histogram):
  return histogram[word.lower()]

if __name__ == '__main__':
    # stochastic_test = stochastic('testsampletext.txt')
    # print(stochastic_test)
    histogram_test = histogram('testsampletext.txt')
    print(histogram_test)
    # words_test = unique_words(histogram_test)
    # print(words_test)
    # count_test = frequency('fish', histogram_test)
    # print(count_test)

