def read_tsv(file_path):
    data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        next(file)  # Saltar la primera línea (encabezado)
        for line in file:
            line = line.strip().split('\t')
            data[line[0]] = line[1:]
    return data

def map_actor_movie(actor_line, movie_data):
    actor_id = actor_line[0]
    actor_name = actor_line[1][0]
    movie_ids = actor_line[1][4].split(',')
    for movie_id in movie_ids:
        movie_info = movie_data.get(movie_id)
        if movie_info:
            movie_title = movie_info[2]
            yield (movie_id, (movie_title, actor_name))

def reduce_actor_movie(movie_id, movie_actor_pairs):
    actors = [pair[1] for pair in movie_actor_pairs]
    yield (movie_id, actors)

# Lectura de los archivos TSV
name_actor_data = read_tsv('name_actor.tsv')
title_movie_data = read_tsv('title_movie.tsv')

# Mapeo de actores a películas
mapped_data = []
for actor_line in name_actor_data.items():
    
    mapped_data.extend(map_actor_movie(actor_line, title_movie_data))

# Reducción de los datos mapeados
reduced_data = {}
for movie_id, movie_actor_pair in mapped_data:
    reduced_data.setdefault(movie_id, []).append(movie_actor_pair)

# Impresión de los resultados
for movie_id, movie_actors in reduced_data.items():
    print(f"Película: {title_movie_data.get(movie_id)[2]}")
    print("Actores:")
    for movie_actor in movie_actors:
        movie_title, actor_name = movie_actor
        print(f"  - {actor_name} ({movie_title})")
    print() 
