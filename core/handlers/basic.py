from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command

from core.filters.NotCommand import NotCommand
from core.settings import settings


router = Router()

@router.message(Command(commands=['start', 'run']))
async def start(message: Message):
  await message.answer('Привет ✌️\nC моей помощью ты можешь связаться с моим хозяином и получить от него ответ. Просто напиши что-нибудь в этот диалог')

@router.message(NotCommand(), F.from_user.id != settings.bots.admin_id)
async def send_message_to_author(message: Message, bot: Bot):
  try:
    await bot.send_message(settings.bots.admin_id, f'{message.from_user.id}\nСообщение от {message.from_user.full_name}\n{message.text}')
    await message.answer(f'Ваше сообщение отправлено 📩\nЕсли хотите еще что-то оправить, напишите мне')
  except Exception as e:
    await message.answer(f'Произошла ошибка во время отправки сообщения. Попробуйте чуть позже')
