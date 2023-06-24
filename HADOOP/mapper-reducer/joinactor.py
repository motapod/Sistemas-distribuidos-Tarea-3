import csv

actor_movies = {}

f=   open("HADOOP/mapper-reducer/title.tsv", "w")
reader = csv.reader(f, delimiter='\t')
next(reader)  # Omitir la primera línea de encabezado

for row in reader:
    actor_id = row[0]
    movie_title = row[2]

    if actor_id not in actor_movies:
        actor_movies[actor_id] = []

    actor_movies[actor_id].append(movie_title)
actor_names = {}

j =   open("HADOOP/mapper-reducer/name.tsv", "w")
reader = csv.reader(j, delimiter='\t')
next(reader)  # Omitir la primera línea de encabezado

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

