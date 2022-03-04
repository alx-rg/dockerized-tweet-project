import string

def clean_text(text):
  punct = string.punctuation
  for chars in text:
    if chars in punct:
      text = text.replace(chars, '')
  return text

