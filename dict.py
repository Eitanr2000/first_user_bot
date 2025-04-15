from pyrogram import Client, filters
import asyncio

# Ваш токен бота и имя сессии
API_ID = 1737949
API_HASH = 'f75dbae0bec8059703ccd3bcf71ef2bb'
TOKEN = '1201017698:AAGqRTS3lWHAAklfoqI8byH5u14XOxkYtag'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


# Русский алфавит с учетом ё, ы, ъ и других букв
russian_alphabet = "1234567890!?:,.abcdefghijklmnopqrstuvwxyz"
sticker_dict = {}
sticker_index = 0

@app.on_message(filters.command("start"))
async def start(client, message):
    global sticker_index
    sticker_index = 0
    await message.reply_text('Привет! Отправьте мне стикеры по порядку русского алфавита. Первый стикер будет связан с буквой "а". Отправьте "stop", чтобы получить словарь.')

@app.on_message(filters.command("stop"))
async def stop(client, message):
    if sticker_dict:
        sticker_list = "\n".join([f"{letter}: {file_id}" for letter, file_id in sticker_dict.items()])
        await message.reply_text(f'Ваш словарь стикеров:\n{sticker_list}')
    else:
        await message.reply_text('Словарь стикеров пуст.')

@app.on_message(filters.sticker)
async def handle_sticker(client, message):
    global sticker_index

    if sticker_index < len(russian_alphabet):
        # Получаем текущую букву из алфавита
        letter = russian_alphabet[sticker_index]
        sticker = message.sticker
        sticker_dict[letter] = sticker.file_id
        await message.reply_text(f'Стикер для буквы "{letter}" добавлен в словарь.')
        sticker_index += 1
    else:
        await message.reply_text(f'Все буквы алфавита уже заполнены.')

if __name__ == "__main__":
    app.run()