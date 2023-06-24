import json

# Create a json database
f1 = open('data.json')
data = json.load(f1)

# Save urls in a array 
urls = []
urls.append(0)

# Save the content of the URL file in urls arrays 
f2 = open("URL.txt", "r")
for line in f2:
    urls.append(line)

# Input the word to search
word = input("Que actor buscas? ")

# Search the word in the json database and see wich file contains the word more times
if word in data:
    print("El actor " + word + " se encuentra en las siguientes peliculas:")
    for i in data[word]:
        print(urls[i])
    # Print the number of times the word appears in each url
    print("El actor " + word + " aparece " + str(data[word][0]) + " veces en el archivo " + urls[data[word][1]])
else:
    print("El actor " + word + " no se encuentra en las peliculas")
    
