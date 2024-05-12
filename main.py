def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  print(text)
  num_words = count_words(text)
  print(f"\nThe number of words contained in the text is: {num_words}\n")
  print(count_letters(text))

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words = text.split()
  return len(words)

def count_letters(text):
  # create dictionary
  letter_count = {}

  # convert all text to lowercase
  lowercase_text = text.lower()

  # loop through the text
  for character in lowercase_text:

    # if character is a letter isalpha() checks for things in the alphabet 
    if character.isalpha():

      # if character in dictionary add 1 to the value count
      if character in letter_count:
        letter_count[character] += 1
      # else add character to the dictionary set value = 1
      else:
        letter_count[character] = 1
  
  # sort the dictionary by the key or alphabetical return the dictionary
  return dict(sorted(letter_count.items()))

main()