from aiogram import Bot, Router, F
from aiogram.types import Message

from core.filters.NotCommand import NotCommand
from core.settings import settings


router = Router()

@router.message(NotCommand())
async def send_message_to_author(message: Message, bot: Bot):
  try:
    await bot.send_message(settings.bots.admin_id, f'Сообщение от {message.from_user.full_name}\n{message.text}')
    await message.answer(f'Ваше сообщение отправлено 📩')
  except Exception as e:
    await message.answer(f'Произошла ошибка во время отправки сообщения. Попробуйте чуть позже')