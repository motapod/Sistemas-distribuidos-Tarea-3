from mrjob.job import MRJob
import csv

class MovieActorIndex(MRJob):
    
    def configure_args(self):
        print("entre 1")
        super(MovieActorIndex, self).configure_args()
        self.add_file_arg('--actors', help='name_actor.tsv')
        self.add_file_arg('--movies', help='title_movie.tsv')
        
    def mapper_init(self):
        print("entre 2")
        # Cargar el archivo name_actor.tsv
        print("File path:", self.options.movies)  # Agrega esta línea para imprimir la ruta del archivo
        with open(self.options.movies, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            self.actor_names = {row[0]: row[1] for row in reader}
        
    def mapper(self, _, line):
        print("entre 3")
        print(line)
        # Emitir pares clave-valor para actores y películas
        if 'titleType' not in line:
            row = line.split('\t')
            actor_id = row[0]
            movie_id = row[1]
            if actor_id in self.actor_names:
                actor_name = self.actor_names[actor_id]
                yield actor_name, movie_id
                
    def reducer(self, actor_name, movie_ids):
        print("entre 4")
        # Generar la lista de películas para cada actor
        movie_list = list(movie_ids)
        yield actor_name, movie_list

if __name__ == '__main__':
    MovieActorIndex.run()
## para instalar el mapper, se debe instalar mrjob. Y eso lo haces en terminal
## con el comando: pip install mrjob
## y luego para correrlo le doy el comando: python mapper.py --actors name_actor.tsv --movies title_movie.tsv > resultado.tsv
