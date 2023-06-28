from mrjob.job import MRJob
from mrjob.step import MRStep

class ActorMovieJob(MRJob):

    def configure_args(self):
        super(ActorMovieJob, self).configure_args()
        self.add_file_arg('--name-actor', help='name_actor.tsv')
        self.add_file_arg('--title-movie', help='title_movie.tsv')

    def mapper_init(self):
        self.name_actor_data = self.read_tsv(self.options.name_actor)
        self.title_movie_data = self.read_tsv(self.options.title_movie)

    def read_tsv(self, file_path):
        data = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            next(file)  # Saltar la primera línea (encabezado)
            for line in file:
                line = line.strip().split('\t')
                data[line[0]] = line[1:]
        return data

    def mapper(self, _, line):
        actor_line = line.strip().split('\t')
        actor_id = actor_line[0]
        actor_name = actor_line[1][0]
        movie_ids = actor_line[1][4].split(',')
        for movie_id in movie_ids:
            movie_info = self.title_movie_data.get(movie_id)
            if movie_info:
                movie_title = movie_info[2]
                yield (movie_id, (movie_title, actor_name))

    def reducer(self, movie_id, movie_actor_pairs):
        actors = [pair[1] for pair in movie_actor_pairs]
        yield (movie_id, actors)

    def steps(self):
        return [
            MRStep(mapper_init=self.mapper_init, mapper=self.mapper, reducer=self.reducer)
        ]


if __name__ == '__main__':
    ActorMovieJob.run()