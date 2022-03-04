import string

# word_list = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish', 'one', 'dog', 'moose', 'doodle']
# text = "Regular expressions use the backslash character ( '\' ) to indicate special forms or to allow special characters to be used without invoking their special ..."

def get_token(text):
  no_punctuation = get_clean_text(text)
  word_list = word_split(no_punctuation)
  return word_list

def get_clean_text(text):
  punct = string.punctuation
  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

def word_split(text_inputed):
  # print(f"word before getting split : {text_inputed}")
  word_list = text_inputed.split()
  # print(f"word AFTER getting split : {word_list}")
  return word_list

