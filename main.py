
with open("My Clippings.txt", 'r') as file:
  file_str = file.read()

entries = file_str.split('==========')
entries = [entry.strip() for entry in entries]

parsed_entries = []

for entry in entries:
  lines = entry.split('\n')

  if (len(lines) == 4):
    parsed_entries.append({
      "title_and_author": lines[0].strip(),
      "metadata": lines[1].strip(),
      "content": lines[3] .strip()
    })

books = list({entry['title_and_author'] for entry in parsed_entries})

# MENU
print('---------- BOOKS ----------')
for index, book in enumerate(books):
  print(f'{index+1}. {book}')

choice = int(input('Choose a book: '))

if choice < 1 or choice > len(books):
  print('Invalid choice!')

else:
  i = 0
  for entry in parsed_entries:
    if entry['title_and_author'] == books[choice-1]:

      if 'Note' in entry['metadata']:
        print(f'Note: {entry['content']}\n')
        continue

      print(f'{i+1}. {entry['content']}\n')
      i += 1