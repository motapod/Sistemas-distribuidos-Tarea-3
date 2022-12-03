
# Sistemas distribuidos: Tarea 3

En esta tarea se desarrolla el uso de Hadoop para mejorar la búsqueda de artículos Wikipedia y así apoyar estudios. En este repositorio se encuentra el link que dirige al drive que contiene tanto el vídeo de explicación como informe, además del link del repositorio del ayudante del cual se basó para la creación del map-reduce y conexión con Hadoop.

# Inicio
Para iniciar los contenedores, se debe clonar el repositorio y ejecutar el comando:

    docker build --no-cache -t hadoop .
Y luego se levanta el contenedor con el siguiente comando:

    docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
Una vez levantado el contenedor, se verifica la conexión con hadoop en localhost.
# Ingresar al contenedor
Para ingresar al contenedor, se utiliza el siguiente comando en otra terminal
    
    docker exec -it hadoop bash
Se deben crear las siguientes carpetas, utilizando los siguientes comandos:
   
    hdfs dfs -mkdir /user
    hdfs dfs -mkdir /user/hduser
    hdfs dfs -mkdir input	

Para pasar el input a utilizar, se usará el siguiente comando:

    hdfs dfs -put mapper-reducer/doc1-5/*txt mapper-reducer/doc6-10/*txt input

# Utilizar mapreduce
Tras realizar la generación de carpetas y haber entregado el input a HADOOP, se utiliza el siguiente comando para hacer correr mapper y reducer, quienes generan el contador de palabras (wordcount):

    mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py

Finalmente, para colocar el output en un archivo .txt, utilizamos el siguiente comando:

    hdfs dfs -cat /user/hduser/output/*

# Buscador de palabras
Para utilizar el buscador de palabras, debemos utilizar el siguiente comando tras realizar todos los pasos anteriores. Colocará todos los datos del output a un json, que actuará como base de datos:

    python create.py

Y finalmente, nuestro buscador lo utilizamos colocando el comando:

    python app.py
# Video e informe
En el siguiente drive se encuentra el acceso para el vídeo y el informe solicitados para la tarea.

[Drive con vídeo e informe](https://drive.google.com/drive/folders/1WJGvCNPXYalMSL2bNtLYHZvPopZ-k058?usp=sharing)

[Repositorio de ayudante](https://github.com/Naikelin/map-reduce-hadoop)
