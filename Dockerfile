# Usa una imagen base de Python
FROM python

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del bot al contenedor
COPY . /app/

# Instala las dependencias
RUN pip install --upgrade pip &&  pip install  -r requerimentos.txt
RUN apt-get update && apt-get install -y ffmpeg
# Ejecuta el bot
CMD ["python", "bot.py"]

