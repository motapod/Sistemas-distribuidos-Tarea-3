import json

file = open("output.txt", "r")
data = {}

next(file)
for line in file:
    linea = line.split()
    word, info = linea.split(' ', 1)
    Data = info.split("]")
    for i in Data:
        # Replace parenthesis with empty string and split by comma
        conjunto = (i.replace("[","")).split("]")
        # if a word is in the dictionary, add the document and count in integer format
        if conjunto[0] == '':
            continue
        else:
            arch, count = conjunto[0].split(",")
            arch = arch.replace(",", "")
            count = count.replace(",", "")
        # if a word is not in the dictionary, add it
        if word not in data:
            data[word] = {arch: int(count)}
        else:
            data[word][arch] = int(count)
print(data)

# Write the dictionary to a json file
with open("../data.json", "w") as output:
    json.dump(data, output, indent=4)