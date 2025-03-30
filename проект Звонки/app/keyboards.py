from aiogram import F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/time')]],
                                                resize_keyboard=True,
                                                input_field_placeholder='Привет, нажми накнопку time, чтобы узнать актуальную информацию')

