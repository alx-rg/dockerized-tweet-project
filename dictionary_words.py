import random
import sys

input_number = int(sys.argv[1])
# Open and read the word file
dictionary = open('./web2', 'r')

word_lines = dictionary.read().splitlines()
length_of_dict = len(word_lines)

# close the word file
dictionary.close()

#New array for words
random_selection = []

index = 0
while index < input_number:
  new_word = word_lines[random.randint(0,length_of_dict)]
  random_selection.append(new_word)
  index += 1

# print(len(word_lines))
new_random_sentence = ' '.join(random_selection)
print(new_random_sentence)

#Argument for the file
#Augmenting the dictionary words function 
#

# Small body of text 1, just 1 blog post, 
# analyzing the frequency of words in any body of text
# display the histogram. 
# work on three functions 1st  function is a historgram taking in called file name sourcetext.txt
# read in the file 
# return unique histogram structure that returns the number of unique words within it. 
# last Frequency function = take a word and the frequency itself
# i.e. Mystery IN Sherlock holmes comes back 20 times.
# Choose and do it TWO of the 3 ways of doing it. 
# list, tuples or key-value pairs