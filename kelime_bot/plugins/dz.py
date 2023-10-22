from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto


# /zar komutunu işleyen fonksiyon
@Client.on_message(filters.command('zar'))
def roll_dice(client, message):
    client.send_dice(message.chat.id)

# /sticker komutunu işleyen fonksiyon

@Client.on_message(filters.command('sticker') & filters.reply)
def convert_to_sticker(client, message):
    reply_message = message.reply_to_message
    if reply_message.photo is not None:
        photo = reply_message.photo[-1]
        file_id = photo.file_id
        client.send_sticker(message.chat.id, file_id)
    else:
        client.send_message(message.chat.id, "Bu mesajda fotoğraf bulunmamaktadır.")
        
# /photo komutunu işleyen fonksiyon
@Client.on_message(filters.command('photo') & filters.reply)
def convert_to_photo(client, message):
    reply_message = message.reply_to_message
    if reply_message.sticker:
        sticker = reply_message.sticker
        file_id = sticker.file_id
        file_path = client.download_media(file_id)
        client.send_photo(message.chat.id, file_path)

