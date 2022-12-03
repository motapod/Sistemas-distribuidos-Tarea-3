import sys

actual_word = None
actual_count = 0
actual_doc = None
word = None
documento = None
dict = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count, documento = line.split('\t', 3)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # if word is not in the dictionary, add it
    if word not in dict:
        dict[word] = {documento: count}
    # if word is in the dictionary, but the document is not, add it
    else:
            if documento not in dict[word]:
                dict[word][documento] = count
    # if word and document are in the dictionary, add 
            else:
                dict[word][documento] += 1
print('Word [Documento1, Count1], [Documento2, Count2], ...')

#### Imprimir en qué documentos aparece cada palabra
for palabra, conteo in dict.items():
    print(palabra + "\t")
    for key in conteo:
        print('[', key, ',', conteo[key], ']', end=' ')
    print("\n")