import logging
from aiogram import Bot, Dispatcher, executor, types
from settings import API_TOKEN
from roll_dice import roll_dice


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
   await message.reply("Я бот для броска костей.\nНабор комманд: roll4, roll6, roll8, roll10, roll12, roll20, roll100")


@dp.message_handler(commands=["roll4", "roll6", "roll8", "roll10", "roll12", "roll20", "roll100"])
async def send_welcome(message: types.Message):
   dice = int(message.text[5:])
   facet = roll_dice(dice)
   await message.answer(facet)


@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)
