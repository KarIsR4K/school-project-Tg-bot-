from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
from app.modul_time import get_lesson_time

router = Router()


@router.message(Command('time'))
async def cmd_time(message: Message):
    text = get_lesson_time()
    await message.answer(text=text, reply_markup=kb.main)
    

@router.message(Command("start"))
async def cmd_start(message: Message):
    user_guide = (
        "Добро пожаловать в бота-помощника для отслеживания времени уроков!\n\n"
        "Инструкция по использованию:\n"
        "- Нажмите /start, чтобы увидеть это руководство.\n"
        "- Нажмите /time, чтобы узнать, сколько времени осталось до начала или конца урока.\n\n"
        "Бот использует стандартное расписание уроков. Если уроки закончились, бот сообщит об этом."
    )
    await message.answer(user_guide, reply_markup=get_lesson_time())

