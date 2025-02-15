# Comandos CatchyBot

Bienvenido, Aquí están los comandos disponibles para interactuar con nuestro bot.

## Comandos Generales

- **/start**: Inicia una conversación con el bot y obtén un mensaje de bienvenida.
- **/help**: Muestra este mensaje de ayuda con todos los comandos disponibles.
- **/list**: Muestra la lista de descargas.

# Es importante descargar ffmepg para la descarga:

```sh
   which ffmpeg
```

En linux en diferente distros ya viene descargado para la reproduccion y cambio de formatos.


## Descarga y Procesamiento de Medios

- **/down2 [URL]**: Descarga un video de YouTube y lo convierte en formato mp3.
  - **Ejemplo**: `/down2 https://www.youtube.com/watch?v=nknDqFENQxk detalrune `
 
- **/down4 [URL] [nameoutput]**: Descarga un video de YouTube y lo convierte en formato mp4 [webm].
  - **Ejemplo**: `/down4 https://www.youtube.com/watch?v=nknDqFENQxk`

- **/down [URL]**: Descarga música de YouTube y la convierte en formato MP3 [toma el titulo de el video de youtube y lo pasa como name output].
  - **Ejemplo**: `/down https://www.youtube.com/watch?v=nknDqFENQxk `

## Notas Importantes
- **Ruta de `ffmpeg`**: Es **crucial** tener descargada la ruta correcta de `ffmpeg` para asegurar la conversión adecuada de archivos multimedia. Puedes obtener `ffmpeg` desde [este enlace](https://github.com/BtbN/FFmpeg-Builds/releases).
  - **Descarga**: Puedes usar `wget` para descargar `ffmpeg` desde bash:
    ```sh
    wget https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2024-12-13-12-34/ffmpeg-master-latest-win64-gpl.zip
    ```

---


### ¡Gracias por usar nuestro bot! 👋
Si tienes alguna duda o necesitas ayuda adicional, no dudes en contactarnos.
### Goodbye 👋🐍 
[Link de mi bot aqui 🤖](https://web.telegram.org/a/#7759974599) 
