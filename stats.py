def get_num_words(filepath):
  with open(filepath) as f:
    file_content = f.read()
  words = file_content.split()
  return f"Found {len(words)} total words"

def get_character_frequency(filepath):
  char_count = {}
  with open(filepath) as f:
    text = f.read()
  for char in text.lower():
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  
  return sort_characters_by_count(char_count)

def sort_characters_by_count(char_count):
  char_list = []
  for char, count in char_count.items():
    # Skip non-alphabetic characters
    if not char.isalpha():
      continue
    char_list.append({"char": char, "num": count})
  
  # Sort the list in descending order based on the 'num' value
  char_list.sort(key=lambda x: x["num"], reverse=True)
  
  return char_list