from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from app.modul_time import Les_time, make_text_for_time

router = Router()


@router.message(CommandStart('start'))
async def cmd_start(message: Message):
    await message.answer('Привет! Чем могу помочь?')


@router.message(Command('time'))
async def cmd_time(message: Message):
    text = make_text_for_time()
    await message.answer(text=text, reply_markup=kb.main)

