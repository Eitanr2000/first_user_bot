from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
import random
import asyncio
import logging

app = Client("my_account", api_id=1737949, api_hash="f75dbae0bec8059703ccd3bcf71ef2bb")
def get_random_unicode_char():
    chosen_range = random.choice(allowed_ranges)
    return chr(random.randint(chosen_range[0], chosen_range[1]))
allowed_ranges = [
    (0x0020, 0x007F),  #Basic Latin (ASCII)
    (0x0400, 0x04FF),  #Cyrillic
    (0x0100, 0x017F),  #Latin Extended-A
    (0x0370, 0x03FF),  #Greek and Coptic
    (0x0590, 0x05FF),  #hebrew
    (0x2600, 0x26FF),  #symbols
]
alpha={
  "а": "CAACAgIAAxkBAAOHZs4pJDZ6KgsWXcW2lPgsLAdKms8AAuk1AAJOAWBI2M6MD6mqYnUeBA",
  "б": "CAACAgIAAxkBAAOJZs4pKCEJwhxHCvo7tcIRbJBf8NIAAik0AAIQ-mlIKURhZ-epgw4eBA",
  "в": "CAACAgIAAxkBAAOLZs4pKw14n1t6Sk6DyWrtE33mneoAAmk6AALXx2FIXuy6mEB21DUeBA",
  "г": "CAACAgIAAxkBAAONZs4pLXaL7dPIIu9B6mo5QljgHCgAAkc2AAJNDGFIln6-YH3CtG8eBA",
  "д": "CAACAgIAAxkBAAOPZs4pL2SgpHJuDjqTV_s53c8h_D8AAtsvAAK4EWhIqZXCCDINmkYeBA",
  "е": "CAACAgIAAxkBAAORZs4pMiTb_p_8BTs8dJa8pn-zMNQAAgo5AAIfiWFIAAHXqV8tp0TeHgQ",
  "ё": "CAACAgIAAxkBAAOTZs4pNMQ2AAHyyPeO8Ap4KTlRcjcpAAIMOAACp1BhSJrRPsTaPM2RHgQ",
  "ж": "CAACAgIAAxkBAAOVZs4pNnPAo0qg7VecaGoOggABlnIgAAKBNgACWMlhSGAuTLETcLyfHgQ",
  "з": "CAACAgIAAxkBAAOXZs4pOE_Tdw-M0qlqZ_tzFDH5ItIAAg84AAIedWBIMGfOpEgSwKIeBA",
  "и": "CAACAgIAAxkBAAOZZs4pOkB6glL-SFFn2i1Pp4kBRfYAAo83AALZhGFIoHLWgOqE9PEeBA",
  "й": "CAACAgIAAxkBAAObZs4pPJ0p2uvdl-PM2DRBcsRMKJMAArJEAAJ9CWlIpLCc-yjRN7ceBA",
  "к": "CAACAgIAAxkBAAOdZs4pPnjGZmsQpNLv-CTBI6ta540AApQzAALX92BIYv_V67g455UeBA",
  "л": "CAACAgIAAxkBAAOfZs4pQPs75vcki4vC96YsTK7vj0UAAmY1AAL4mWhISd_neur7opgeBA",
  "м": "CAACAgIAAxkBAAOhZs4pQmci3OpQSFrj9fQ6oWGg0NIAAnU1AAIt_GBIVGWlSnsOTeMeBA",
  "н": "CAACAgIAAxkBAAOjZs4pQ2Ut452jSWH4xrfqdLzrz3cAAsk6AAITxmhILmPS69OsnNMeBA",
  "о": "CAACAgIAAxkBAAOlZs4pRde5po0VDwgdY4tduFsrFcgAArM0AAImvGFIhfN2ZZwJTdQeBA",
  "п": "CAACAgIAAxkBAAOnZs4pRzP4lhWpQCD5t_ZFEsolH7kAAkQ6AAI4qGFIrshpWI_0fdQeBA",
  "р": "CAACAgIAAxkBAAOpZs4pSA_zo8UaptLQb-3pO7_IfeUAAlg2AALX7mlIcKwqz0n7FTseBA",
  "с": "CAACAgIAAxkBAAOrZs4pShgwXfACVGqyDYG_Ia6GGdkAAos2AAJ7O2BIQDmxXv2hspIeBA",
  "т": "CAACAgIAAxkBAAOtZs4pTGVemCFa0DGQ5h22uJ8nIFIAAqMyAAL-MGBIDvXJaUP-rN0eBA",
  "у": "CAACAgIAAxkBAAOvZs4pTwE_QSmyWWSfLvT4AodoEDQAAsg5AAK_qGhI0iDEA8SkIj8eBA",
  "ф": "CAACAgIAAxkBAAOxZs4pUJ04Nq2NMZhcoKSV1hiJRq4AAqQ8AAISVWFIgKux-4hcPpceBA",
  "х": "CAACAgIAAxkBAAOzZs4pUsZMpmb10QABOGjrzS9R0Go6AALuMgACtz1pSB53_DGQY_D9HgQ",
  "ц": "CAACAgIAAxkBAAO1Zs4pVCwjwAjoBJQEQsnLCxWZclYAAng4AAIBiWFIhFXYo4u8Te0eBA",
  "ч": "CAACAgIAAxkBAAO3Zs4pVtJU0xC42EqPEtFxDuUy890AAsM6AAIZXWBIxMUs-CT2askeBA",
  "ш": "CAACAgIAAxkBAAO5Zs4pWPkVXD9aDCPw21DZlQSrpL8AAvw3AAIcUGFIreV-HCdpsHseBA",
  "щ": "CAACAgIAAxkBAAO7Zs4pWTnnvsalyh66rnzZ0_BQ8kQAAlw2AALHv2BIKd06vK1CjpAeBA",
  "ъ": "CAACAgIAAxkBAAO9Zs4pXOklra9bjkIu3g1O9YAETXkAAi04AAIh5mFI9m-AqxuO7gweBA",
  "ы": "CAACAgIAAxkBAAO_Zs4pXn3gkP-a0d3jYT_bL0WJBOAAAiA5AAKWCmhICq24mPkng7AeBA",
  "ь": "CAACAgIAAxkBAAPBZs4pYBqs1bZDWzgzCUSYntC7VVEAAl07AAIgC2FI6rdV4PwByAoeBA",
  "э": "CAACAgIAAxkBAAPDZs4pYYEV40ZTAAEwBucAAUm_zkCMkwACEjkAAtvaYEgNZ_tzj-tC_R4E",
  "ю": "CAACAgIAAxkBAAPFZs4pYnRHaxRyl4SPNCFlgl4omQ8AAog1AAJDimhIBBDht-8LV3MeBA",
  "я": "CAACAgIAAxkBAAPHZs4pZLqcHGqCMwgfFGi1jjmedq8AAmg4AAJTJmFI2PgQuLWp4RgeBA",
  " ": "CAACAgIAAxkBAAPJZs4pZWEPdQEkOJG4ywm4nAGjqjkAAqc5AALZk2BIoKOD34iiesEeBA",
"1": "CAACAgIAAxkBAAPNZs9tVPxUqxnNG1h3_ifGvcFcIIYAAl01AALLLmhIKfJsaIRJ-eceBA",
"2": "CAACAgIAAxkBAAPPZs9tV3dAM2lzjAqELah_h6NoDKcAAjg9AAILjmFIamUL_ZI3m8UeBA",
"3": "CAACAgIAAxkBAAPRZs9tWbIB8i4OarftMB1NAlr1MIUAAt42AAIQkWhISN3dzMFcdYAeBA",
"4": "CAACAgIAAxkBAAPTZs9tW_YW-5auvepTXRl6sijUswADnDkAAttcYUh6-n355LWVyx4E",
"5": "CAACAgIAAxkBAAPVZs9tXqPyAAHzO1z_39ygOz5uYklGAAIyOgACHPJpSATuSrLmRhExHgQ",
"6": "CAACAgIAAxkBAAPXZs9tYDcFjMbN3b5xmcaJkS0_Yz0AAmA3AAJOxmBIYCQX9l7wU0MeBA",
"7": "CAACAgIAAxkBAAPZZs9tYquwkQvN-Ue3kJhz90w-aEUAAs0xAAI9wmBIhr22REkhGbQeBA",
"8": "CAACAgIAAxkBAAPbZs9tY-N3qSqpK1VsF0bdC4AM6SIAAmA4AAL4EmFIAp_-9O90m_oeBA",
"9": "CAACAgIAAxkBAAPdZs9tZtCEFXnHuCFpoiwTswnz2OAAAodFAAJJOxBK4md3dCTMqPAeBA",
"0": "CAACAgIAAxkBAAPfZs9ta2aOaWbduC8UIdziheIwtpUAAgs5AALSmGlIb-IKQ9XoqqseBA",
"!": "CAACAgIAAxkBAAPhZs9tbjIyjmzABmHNw5whrkzCKooAAt8_AAIwaWlIteW_WPNHs1geBA",
"?": "CAACAgIAAxkBAAPjZs9tcdXT7cKD0ZSd1un_39aYUmIAAjY3AAKMMmBI-fnJmYKv0uUeBA",
":": "CAACAgIAAxkBAAPlZs9tch4NiQRHHsmoECDtIZllt7sAAjA3AAJa3WBIjco6srJww50eBA",
",": "CAACAgIAAxkBAAPnZs9tdZZSDa4jvDQAAVbSqs9TPnr5AALFOgACLkJpSEOLW2q-rpOEHgQ",
".": "CAACAgIAAxkBAAPpZs9tdyR1GpoT08s2EEARFPaNSXUAAo83AAIljmBIiNmuCWnT1lUeBA",
"a": "CAACAgIAAxkBAAPrZs9teZ9xufHrjp_hvvPeWmBy8wwAAltHAAL6rhBKWtW_JgEtwVQeBA",
"b": "CAACAgIAAxkBAAPtZs9te0R1jBbirTYY8CltayWLKQYAAoZSAALM0QlKb85B50JCSzEeBA",
"c": "CAACAgIAAxkBAAPvZs9tfRQ_RMq6hrd3TNt1eOQqLD8AAjtHAALQFRBKKeRO6IdGWRweBA",
"d": "CAACAgIAAxkBAAPxZs9tfsTTkU5fAcu0FoUw5LEOkuAAAkNGAAKlrxFKW9gO3x80dfkeBA",
"e": "CAACAgIAAxkBAAPzZs9tf4RS5y8YndhE0g1rfamcBOIAAn9HAAKQ5RFKQDCc-ygnl0geBA",
"f": "CAACAgIAAxkBAAP1Zs9tgQ3UPQ2Py569B1b4JfqDd0gAAlpHAAI6QhFKmLnSXnUCfJseBA",
"g": "CAACAgIAAxkBAAP3Zs9tgsXnTD_SWjE323jB_PUV2ZAAAnBJAAIlYRBKysFjnfnlrf0eBA",
"h": "CAACAgIAAxkBAAP5Zs9thGt10NQahAaa_Co7jK3ShXMAAiBDAALw1hBKvWmzIuohM7YeBA",
"i": "CAACAgIAAxkBAAP7Zs9thZv9mHggNhIud8qZD8gFNk8AAsNGAAKGKhFKBUHxp0XgTZUeBA",
"j": "CAACAgIAAxkBAAP9Zs9thnfDydJSusAXyGNMGPwwzV4AAqdJAAJTPRBKAkIj2JS3ChUeBA",
"k": "CAACAgIAAxkBAAP_Zs9tiDzvI17XdkY6LOviEwAB8uerAAKlSgACT8sQSmTjMb7mUamjHgQ",
"l": "CAACAgIAAxkBAAIBAWbPbYnaiO48hSvhadJDMwpcJaNaAAKrRgACV3AQSgF0uZ8H3g_RHgQ",
"m": "CAACAgIAAxkBAAIBA2bPbYu2IjWkRFHmNZG_nz2VT8RzAAJrTQAC8PkISotaBRrFcK7eHgQ",
"n": "CAACAgIAAxkBAAIBBWbPbYxqKVWWaSkUugG-xl83Lq6jAALiRAACcDsRSqiW5VyyU9nxHgQ",
"o": "CAACAgIAAxkBAAIBB2bPbY2MRnPY-vHYv3QYtwABycMWsQAC8UcAAq34EUr-0KBlZk79Ih4E",
"p": "CAACAgIAAxkBAAIBCWbPbY-iJ-tcMOizobGJWT9TRngwAAKJRQACkkIQSlCDs3WOU4R1HgQ",
"q": "CAACAgIAAxkBAAIBC2bPbZAPhDXedPtNYG6fUJSzTKPtAAJkRwACVowQShfHiX6ZE-UNHgQ",
"r": "CAACAgIAAxkBAAIBDWbPbZJ8JSmzgrdgLsoxxNRs5yWNAAIrTAACDiYQSqD5eHFaV58IHgQ",
"s": "CAACAgIAAxkBAAIBD2bPbZOEokq8OENn84oiSLdaQF5sAAJ_SQACIekQSn70NjuTRFgQHgQ",
"t": "CAACAgIAAxkBAAIBEWbPbZXiuRlHlqtbtdHG6CEUIJrMAAJ6TQACQrQQSmvFqeeIW7XEHgQ",
"u": "CAACAgIAAxkBAAIBE2bPbZbZHFN5W6MZz7ufhoIl5MNyAAJ6SwACEGkQSoFKPIjwfsKCHgQ",
"v": "CAACAgIAAxkBAAIBFWbPbZgw0_6Tli-y4WrrdnwuDV8EAAJKRwACG1AQSlZOb7PLklFDHgQ",
"w": "CAACAgIAAxkBAAIBF2bPbZm6f80R5D1dmseF-wcFGxIRAAJyRQACOWERSg8HrHVBK5MqHgQ",
"x": "CAACAgIAAxkBAAIBGWbPbZsZqZR-1JWwM-DVmPWnTyxjAALVUQACO8IRSsPDn-RG-BQlHgQ",
"y": "CAACAgIAAxkBAAIBG2bPbZxS2sYT_WCPPZCPIvSZB7sYAAInRwACGjoQSjn3nrTTeOt5HgQ",
"z": "CAACAgIAAxkBAAIBHWbPbZ7Bpw5kmfpW3-xc6k8r-D4OAAI0TQACdOUQSi-8LC8p4efKHgQ"
}


logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def log_message(message):
    logging.debug(message)

async def handle_message(client, msg, message):
    log_message(f"Handling message: {message}")
    if message.startswith(".write"):
        fake_message = await client.send_message(msg.chat.id, message)
        await write(client, fake_message)
    elif message.startswith(".spam"):
        fake_message = await client.send_message(msg.chat.id, message)
        await spamm(client, fake_message)
    elif message.startswith(".type"):
        fake_message = await client.send_message(msg.chat.id, message)
        await type(client, fake_message)
    else:
        await client.send_message(msg.chat.id, message)

@app.on_message(filters.command("time", prefixes=".") & filters.me)
async def time_command(client, message):
    try:
        args = message.text.strip().split()
        time_value = int(args[1])
        time_unit = args[2].lower()

        if time_unit == "s":
            seconds = time_value
        elif time_unit == "m":
            seconds = time_value * 60
        elif time_unit == "h":
            seconds = time_value * 3600
        else:
            await message.reply("Неправильный выбор времени. Используйте 's' для секунд, 'm' для минут, 'h' для часов.")
            return

        command_to_run = " ".join(args[3:]) if len(args) > 3 else None
        await message.reply(f"Обратный отсчёт начинается через {time_value} {time_unit}")

        for i in range(seconds, 0, -1):
            await message.reply(f"Осталось {i} секунд(ы)")
            await asyncio.sleep(1)

        if command_to_run:
            log_message(f"Running command: {command_to_run}")
            if command_to_run.startswith(".write"):
                fake_message = await client.send_message(message.chat.id, command_to_run)
                await write(client, fake_message)
            elif command_to_run.startswith(".spam"):
                fake_message = await client.send_message(message.chat.id, command_to_run)
                await spamm(client, fake_message)
            elif command_to_run.startswith(".type"):
                fake_message = await client.send_message(message.chat.id, command_to_run)
                await type(client, fake_message)
            else:
                await client.send_message(message.chat.id, command_to_run)
        else:
            await message.reply("Время вышло!")

    except (IndexError, ValueError):
        await message.reply("Пожалуйста, укажите правильное количество времени и единицу времени.")
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

@app.on_message(filters.command("write", prefixes="."))
async def write(client, message):
    try:
        orig_text = message.text.split(".write ", maxsplit=1)[1].lower()
        await client.delete_messages(message.chat.id, message.id)
        for i in orig_text:
            typing_symbol = alpha.get(i)
            if typing_symbol:
                await client.send_sticker(message.chat.id, typing_symbol)
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

@app.on_message(filters.command("spamm", prefixes="."))
async def spamm(client, msg):
    log_message("Debug: Starting spamm function")

    try:
        await client.delete_messages(msg.chat.id, msg.id)
        log_message("Debug: Message deleted")
    except Exception as e:
        log_message(f"Debug: Exception caught during message deletion: {str(e)}")
        return

    try:
        parts = msg.text.split(".spamm", maxsplit=1)[1].strip().split(" ", maxsplit=1)
        count_str = parts[0].strip()
        count = int(count_str)
        if len(parts) < 2:
            raise IndexError("Message part is missing")
        message = parts[1].strip()
        log_message(f"Debug: Extracted count '{count}' and message '{message}'")
    except (IndexError, ValueError) as e:
        log_message(f"Debug: Exception caught during count extraction: {str(e)}")
        await msg.reply("Пожалуйста, укажите правильное количество сообщений для спама.")
        return

    for j in range(count):
        try:
            log_message(f"Debug: Sending message {j + 1}/{count}")
            if message:
                await handle_message(client, msg, message)
        except FloodWait as e:
            log_message(f"Debug: FloodWait exception caught: {str(e)}")
            await asyncio.sleep(e.value)
        except Exception as e:
            log_message(f"Debug: Exception caught during message sending: {str(e)}")
            await msg.reply(f"Произошла ошибка: {str(e)}")
            break

@app.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam(client, msg):
    await client.delete_messages(msg.chat.id, msg.id)
    try:
        count = int(msg.text.split(".spam", maxsplit=1)[1].strip())
        for _ in range(count):
            length = random.randint(1, 100)
            message = "".join(get_random_unicode_char() for _ in range(length))
            try:
                await client.send_message(msg.chat.id, message)
            except FloodWait as e:
                await asyncio.sleep(e.value)
    except (IndexError, ValueError):
        await msg.reply("Пожалуйста, укажите правильное количество сообщений для спама.")

@app.on_message(filters.command("type", prefixes=".") & filters.me)
async def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    tbp = ""
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            if orig_text:
                if tbp + typing_symbol != orig_text:  # Проверка перед редактированием
                    await msg.edit_text(tbp + typing_symbol)
                    await asyncio.sleep(0.05)
                    tbp += orig_text[0]
                    orig_text = orig_text[1:]
                else:
                    await msg.edit_text(tbp)  # Завершение редактирования
                    break
            else:
                await msg.edit_text(tbp)  # Завершение редактирования
                break

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except Exception as e:
            await msg.reply(f"Произошла ошибка: {str(e)}")
            break

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
async def hack(client, msg):
    perc = 0
    while perc < 100:
        try:
            text = f"👮‍ поиск пидорасов активирован {perc}%"
            await msg.edit(text)
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.value)

    await msg.edit("пидорас читает это сообщение")
    await asyncio.sleep(3)

    await msg.edit("произвожу взлом жопы пидораса")
    await asyncio.sleep(3)

    perc = 0
    while perc < 100:
        try:
            text = f"взлом жопы {perc}%"
            await msg.edit(text)
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        except FloodWait as e:
            await asyncio.sleep(e.value)

    await msg.edit("взлом произведён успешно, анальная девственность не найдена")

@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
async def thanos(client, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]

    members = [
        x
        for x in await client.get_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]

    random.shuffle(members)

    await client.send_message(chat, "Щелчок Таноса ... *щёлк*")

    for i in range(len(members) // 2):
        try:
            await client.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            await client.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.value, "seconds.")
            await asyncio.sleep(e.value)

    await client.send_message(chat, "Но какой ценой?")

app.run()