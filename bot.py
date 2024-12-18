import telebot
import yt_dlp
from os import remove,listdir,path
from time import sleep
from yt_dlp import YoutubeDL
from random import randrange
from io import BytesIO
import os


print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))
print("NO_PROXY:", os.getenv("NO_PROXY"))


directorio = listdir()
extensiones = [".mp3",".webm",".jpg"]

for file in directorio:
    if path.splitext(file)[1] in extensiones:
        remove(f"./{file}")
        print("Limpiando directorio 🤖🤖🤖")

APITOKEN = "7759974599:AAEat0xZn2z1v4J7ZoirL13lnvMFQCjXBHY"

bot = telebot.TeleBot(token=APITOKEN)


@bot.message_handler(commands=["toto"])
def output_file(message):
    text = str(message.text.split(" ")[2])
    bot.reply_to(message,text)



@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello you 👋, soy tu bot asistente de descarga mp3, mp4 y webm hecho con Python  🤖. ")




@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message,"c 0867")


@bot.message_handler(commands=["down"],content_types=["text"],func=lambda m: True)
def download_music(message):
    bot.reply_to(message,message.text[6:])
    url: str = message.text[6:]
    try:
        # Extraer el nombre del video, o el titulo
        if len(message.text) <= 4:
            bot.reply_to(message,"Demasiado corto, try again")

        else:
            ydl_optss = {'quiet': True,'extract_flat': True,}
            with yt_dlp.YoutubeDL(ydl_optss) as ydl:
                info_dict = ydl.extract_info(url, download=False)  
                video_title = info_dict.get('title', 'audio')
                bot.reply_to(message,video_title)
                ydl_opts = {
                'cookies': 'cookies.txt',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': video_title,
                'ffmpeg_location': r".\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                bot.reply_to(message,"Espere... 🤖🐍")
            with open(f'{video_title}.mp3', 'rb') as audio:
                bot.send_audio(message.chat.id, audio)
                bot.reply_to(message, "¡Descarga completada!")
    except Exception as e:
            bot.reply_to(message, f"Ocurrió un error: {str(e)}")
    finally:
        sleep(1)
        remove(f"./{video_title}.mp3")



@bot.message_handler(commands=["down2"],content_types=["text"],func=lambda m: True)
def download_music(message):
    texto = list(message.text.split(" "))
    url: str = texto[1]
    bot.reply_to(message,f"Output NamefileSong 🎵🎶: {texto[2]}")
    bot.reply_to(message,url)
    name_fileoutput : str = texto[2]
    try:
        if len(url) > 43:
            bot.reply_to(message,"Demasiado Largo, no se pueden descargar formatos de radio o mix. 🌋")
        elif len(url) == 43:
            ydl_optss = {'quiet': True,'extract_flat': True,}
            with yt_dlp.YoutubeDL(ydl_optss) as ydl:
                info_dict = ydl.extract_info(url, download=False)  
                video_title = info_dict.get('title', 'audio')
                bot.reply_to(message,video_title)
                ydl_opts = {
                'cookies': 'cookies.txt',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': name_fileoutput,
                'ffmpeg_location': r".\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                bot.reply_to(message,"Espere... 🤖🐍")
                bot.reply_to(message,"Descargando... 🤖🐍")
            with open(f'{name_fileoutput}.mp3', 'rb') as audio:
                bot.send_audio(message.chat.id, audio)
                bot.reply_to(message, "¡Descarga completadaaa!")
    except Exception as e:
            bot.reply_to(message, f"Ocurrió un error: {str(e)}")
    finally:
        sleep(1)
        remove(f"./{name_fileoutput}.mp3")
@bot.message_handler(commands=["down4"])
def download_mp4(message):
    try:
        if len(message.text) <= 6:
            bot.reply_to(message,"Demasiado corto, intente de nuevo.")
        else:
            bot.reply_to(message,message.text[7:])
            url: str = message.text[7:]
            with YoutubeDL() as ydl:
                info_dict = ydl.extract_info(url, download=True)
                output_filename = ydl.prepare_filename(info_dict)
                print(f"downloaded {output_filename}")
            with open(f"{output_filename}","rb") as video:
                bot.reply_to(message,"Descargando... 👋 ")
                bot.send_video(message.chat.id,video)
                bot.reply_to(message,"Descargado con exito 🤖")
    except Exception as error:
        bot.reply_to(message,error)
    finally:
        sleep(1)
        remove(f"./{output_filename}")



@bot.message_handler(func=lambda m:True)
def echo_all(message): 
    mensajes_list = [
    "Lo siento, no entendí eso. ¿Podrías repetirlo?",
    "Hmm, no estoy seguro de qué quieres decir. ¿Puedes explicarlo de otra manera?",
    "¡Ups! No entendí. ¿Puedes intentarlo de nuevo?",
    "Perdón, no capté eso. ¿Podrías decirlo de otra forma?",
    "No estoy seguro de qué quieres decir. ¿Puedes ser más claro?",
    "Lo siento, no entendí. ¿Puedes darme más detalles?",
    "No estoy seguro de qué significa eso. ¿Puedes explicarlo mejor?",
    "Perdón, no entendí. ¿Puedes intentarlo de nuevo?",
    "Hmm, eso no tiene sentido para mí. ¿Puedes decirlo de otra manera?",
    "Lo siento, no capté eso. ¿Puedes explicarlo mejor?",
    "Por favor utiliza mis comandos"
]
    mensaje_send = mensajes_list[randrange(0,len(mensajes_list))]   
    bot.reply_to(message,f"{mensaje_send} 🤖🐍: {message.text} ")





@bot.message_handler(content_types=["photo"])
def obtener_imagenes(message):
    with open("imagen_recibida.jpg","rb") as image:
        bot.send_video(message.chat.id,image)


bot.infinity_polling()






"""
Es importante la descarga de la ruta de ffmpeg
Thanks 👋


"""