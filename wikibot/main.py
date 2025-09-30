import logging
import asyncio
import wikipedia
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '8315248525:AAElmquwM6Wo6bLI4kD5gVNQcqXrVv8328k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Set Wikipedia language to Uzbek
wikipedia.set_lang("uz")

# Handler for /start and /help commands
@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: types.Message):
    await message.reply(
        "Salom!\nMen WikipediaBotman!\nIstalgan so‘zni yoz, men O‘zbekcha Wikipedia’dan qisqacha ma’lumot beraman."
    )

# Wikipedia + Echo handler
@dp.message()
async def sendWiki(message: types.Message):
    query = message.text.strip()
    if not query:
        await message.reply("Iltimos, haqiqiy so‘z kiriting.")
        return
    try:
        summary = wikipedia.summary(query, sentences=3)
        if summary.strip() == "":
            raise wikipedia.PageError(query)
        await message.answer(summary)
    except wikipedia.DisambiguationError as e:
        await message.reply(
            f"Bir nechta natijalar topildi, iltimos aniqroq so‘z kiriting.\nVariantlar:\n{e.options[:5]}"
        )
    except wikipedia.PageError:
        await message.reply(
            "O‘zbekcha sahifa topilmadi. Siz yozgan xabarni qaytaraman:"
        )
        await message.reply(message.text)
    except Exception as ex:
        await message.reply(f"Xatolik yuz berdi: {str(ex)}")
        await message.reply(message.text)

# Run the bot
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))












