import logging
from aiogram import Bot, Dispatcher,  types
from settings import API_TOKEN
from utils import print_number


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

@dp.message_handler(regexp="Кинуть d\\d*")
async def send_roll(message: types.Message):
    dice = int(message.text[8:])
    logging.log(level=logging.INFO,
                msg=f"{message.from_user.first_name} rolled dice: {dice}")
    img_to_send = print_number(dice)
    await message.answer_photo(img_to_send, reply_markup=dice_keyboard)


@dp.message_handler(commands=["start", "help"])
@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.answer("Я бот для броска костей.\n", reply_markup=dice_keyboard)

