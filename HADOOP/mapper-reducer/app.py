import json
import os

import pandas as pd

actor_movies = {}

reader=  pd.read_csv('title_movie.tsv', sep='\t')
#next(reader)   Omitir la primera línea de encabezado
for i, row in enumerate(reader):
            if i >= 5:
                break
            print(row)
#if not reader.__sizeof__ == 0:
#    for row in reader:
#        print(row)

for row in reader:
    actor_id = row[0]
    movie_title = row[2]

    if actor_id not in actor_movies:
        actor_movies[actor_id] = []

    actor_movies[actor_id].append(movie_title)
actor_names = {}

j =   open("./name_actor.tsv", "r")
reader = csv.reader(j, delimiter='\t')
if not reader.__sizeof__ == 0:
        for row in reader:
            print(row)


for row in reader:
    actor_id = row[0]
    actor_name = row[1]
    actor_names[actor_id] = actor_name

with open('resultado.tsv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['Actor', 'Películas'])

    for actor_id, actor_name in actor_names.items():
        movies = actor_movies.get(actor_id, [])
        writer.writerow([actor_name, ', '.join(movies)])


# Create a json database
with open(os.path.expanduser('HADOOP\mapper-reducer\data.json'), 'a+') as f:
    data = json.load(f)

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
    
