import string

def get_opened_file(text_inputed):
  file = open(text_inputed, 'r')
  text = file.read()
  file.close()
  return text

def get_lower_case(text_inputed):
  text = text_inputed
  text = text.lower()
  return text

def get_open_and_lower(text_inputed):
  text_open = get_opened_file(text_inputed)
  text = get_lower_case(text_open)
  return text

