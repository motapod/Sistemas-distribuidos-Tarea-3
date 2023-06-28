FROM sequenceiq/hadoop-docker:2.7.1

# Instalar dependencias adicionales necesarias para el código
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY mapper-reducer /app/mapper-reducer
COPY data.json /app/data.json
COPY title_movie.tsv /app/title_movie.tsv
COPY resultado.tsv /app/resultado.tsv
COPY name_actor.tsv /app/name_actor.tsv
COPY mappertry.py /app/mappertry.py

# Instalar las dependencias del código
RUN pip3 install mrjob

# Ejecutar el código en el contenedor
CMD python3 /app/mappertry.py
#docker build -t hadoop-mapper-reducer . buidear
#docker run -it --name hadoop-container hadoop-mapper-reducer ejecutar con eso