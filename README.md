
# Sistemas distribuidos: Tarea 3

En esta tarea se desarrolla el uso de Hadoop para crear una búsqueda de trabajos en los cuales han participados diversos actores, directores y guionistas en la base de datos de IMDb. En este repositorio se encuentra el link que dirige al drive que contiene tanto el vídeo de explicación como informe.
# Inicio
Para iniciar los contenedores, se debe clonar el repositorio y ejecutar el comando:

    docker build -t hadoop-mapper-reducer 
Y luego se levanta el contenedor con el siguiente comando:

    docker run -it --name hadoop-container hadoop-mapper-reducer
Una vez levantado el contenedor, se verifica la conexión con hadoop en localhost.
# Ingresar al contenedor
Para ingresar al contenedor, se utiliza el siguiente comando en otra terminal
    
    docker exec -it hadoop bash
Se deben crear las siguientes carpetas, utilizando los siguientes comandos:
   
    hdfs dfs -mkdir /user
    hdfs dfs -mkdir /user/hduser
    hdfs dfs -mkdir input	



# Utilizar mapreduce
Para instalar el mapper, se debe instalar mrjob con el comando:
    pip install mrjob
Y luego para correrlo:
    python mapper.py --actors name_actor.tsv --movies title_movie.tsv > resultado.tsv


    python create.py

Y finalmente, nuestro buscador lo utilizamos colocando el comando:

    python app.py
