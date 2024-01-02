file = open('Text.csv', 'w')

CSV_TEXT = 'ASDFGHJKLQWERTYUIOPZ'
text = 'key,ja,en,ch\n'
for keyCount in range(20000):
    text += CSV_TEXT + str(keyCount) + ','
    text += CSV_TEXT + str(keyCount) + ','
    text += CSV_TEXT + str(keyCount) + ','
    text += CSV_TEXT + str(keyCount) + '\n'

file.write(text)
file.close()