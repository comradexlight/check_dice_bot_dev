import io
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from settings import API_TOKEN
from roll_dice import roll_dice
from dice_img import make_facet_img

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dice_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    types.KeyboardButton(text="Кинуть d4"), types.KeyboardButton(text="Кинуть d6")).row(
    types.KeyboardButton(text="Кинуть d8"), types.KeyboardButton(text="Кинуть d10")).row(
    types.KeyboardButton(text="Кинуть d12"), types.KeyboardButton(text="Кинуть d20")).row(
    types.KeyboardButton(text="Кинуть d100"))

@dp.message_handler(regexp="Кинуть d\d*")
async def send_roll(message: types.Message):
   dice = int(message.text[8:])
   facet = roll_dice(dice)
   img = make_facet_img(facet)
   content = io.BytesIO(img)
   print(message.from_user.id, message.from_user.first_name)
   await message.answer_photo(content)
   await message.answer(f"{message.from_user.first_name}, у тебя выпало {facet}", reply_markup=dice_keyboard)


@dp.message_handler(commands=["start", "help"])
@dp.message_handler()
async def send_welcome(message: types.Message):
   await message.answer("Я бот для броска костей.\n", reply_markup=dice_keyboard)
