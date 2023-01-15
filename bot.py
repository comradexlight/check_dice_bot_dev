import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from settings import API_TOKEN
from utils import roll_dice, from_image_to_bytes
from make_img import print_number

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dice_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                          one_time_keyboard=True).row(
    types.KeyboardButton(text="Кинуть d4"),
    types.KeyboardButton(text="Кинуть d6")).row(
    types.KeyboardButton(text="Кинуть d8"),
    types.KeyboardButton(text="Кинуть d10")).row(
    types.KeyboardButton(text="Кинуть d12"),
    types.KeyboardButton(text="Кинуть d20"))

@dp.message_handler(regexp="Кинуть d\d*")
async def send_roll(message: types.Message):
   dice = int(message.text[8:]) 
   rolled_number = roll_dice(dice)
   number_image = print_number(rolled_number)
   img_to_send = from_image_to_bytes(number_image)
   print(message.from_user.id, message.from_user.first_name)
   await message.answer_photo(img_to_send, reply_markup=dice_keyboard)


@dp.message_handler(commands=["start", "help"])
@dp.message_handler()
async def send_welcome(message: types.Message):
   await message.answer("Я бот для броска костей.\n", reply_markup=dice_keyboard)
