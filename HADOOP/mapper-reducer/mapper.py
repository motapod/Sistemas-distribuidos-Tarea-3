import sys
import re
import os

# Create a list with the words of the file
for line in sys.stdin:
    # Create a list with the words of the file
    line = re.sub(r'\W+',' ',line.strip())
    words = line.split()
    

    root = os.environ['map_input_file']
    root_list = root.split("/", 6)
    documento = root_list[6].split('.', 1)[0]
    documento = documento.split('o', 1)[1]

    # Iterate over the list of words
    for word in words:
        # Write the result to STDOUT
        print('{}\t{}\t{}'.format(word, 1, int(documento)))