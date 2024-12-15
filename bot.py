import telebot
import yt_dlp
from os import remove
from time import sleep
from yt_dlp import YoutubeDL
from random import randrange

token = "7759974599:AAEat0xZn2z1v4J7ZoirL13lnvMFQCjXBHY"

bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hola👋, soy tu bot asistente de descarga mp3 de yt 🤖. ")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message,"Puedes interactuar conmingo usando comandos 💻 \n🔽/down <urlyt>: Para descargar videos en formato mp3, la sintaxis es /down <url>")


@bot.message_handler(commands=["down"],content_types=["text"],func=lambda m: True)
def download_music(message):
    bot.reply_to(message,message.text[6:])
    url: str = message.text[6:]
    try:
        
        ydl_optss = {'quiet': True,'extract_flat': True,}
        
        # Extraer el nombre del video, o el titulo
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
            'ffmpeg_location': r'C:\Users\Usuario\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin',
        }
    
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            bot.reply_to(message,"Espere... 🤖🐍")
        with open(f'{video_title}.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio)
            bot.reply_to(message, "¡Descarga completada!")
        sleep(2)
        remove(f"./{video_title}.mp3")
    except Exception as e:
            bot.reply_to(message, f"Ocurrió un error: {str(e)}")
            
@bot.message_handler(commands=["down4"])
def download_mp4(message):
    try:
        bot.reply_to(message,message.text[7:])
        url: str = message.text[7:]
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=True)
            output_filename = ydl.prepare_filename(info_dict)
            print(f"downloaded {output_filename}")
        with open(f"{output_filename}","rb") as video:
            bot.reply_to(message,"Descargandooo 👋 ")
            bot.send_video(message.chat.id,video)
            bot.reply_to(message,"Enviado con exito")
    except Exception as error:
        bot.reply_to(message,error)
    finally:
        sleep(1)
        remove(f"./{output_filename}")


@bot.message_handler(func=lambda m:True)
def echo_all(message): 
    mensajes_lists : list = ["Que mierda es esto","WTF ES ESTO 🤖","NO ENTIENDO ESTA CACORRADA"]
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




bot.infinity_polling()


"""
Es importante la descarga de la ruta de ffmpeg
Thanks 👋
"""