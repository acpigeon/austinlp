# The commented lines allow us to handle input with accented or non-Western characters.
# Always follow the principle of the Uniocde sandwich: decode all inputs upon input, encode all outputs upon output.
# An excellent resource for any of problems in this area: http://nedbatchelder.com/text/unipain.html

import csv


word, definition = [], []


with open('vocab.csv', 'rU') as file:
    csv_object = csv.reader(file, delimiter=',', quotechar='"')
    for row in csv_object:
        unicode_row = [unicode(cell, 'utf-8') for cell in row] # Python list comprehension to decode on input
        word.append(unicode_row[0])
        definition.append(unicode_row[1])


# Do things with text!


output = zip(word, definition)
headers = ["Word", "definition"]
output.insert(0, headers)

output_file = csv.writer(open('vocab_output.csv', 'ab'), delimiter=",", quotechar='"')
for utf8_row in output:
    unicode_row = [utf8_row[x].encode('utf8') for x in range(len(utf8_row))] # Python list comprehension to encode on output
    output_file.writerow(unicode_row)
