from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command

from core.filters.NotCommand import NotCommand
from core.settings import settings


router = Router()
router.message.filter(F.from_user.id == settings.bots.admin_id)


@router.message(NotCommand())
async def answer_message(message: Message, bot: Bot):  
  try:
    user_id: str = message.reply_to_message.text.split('\n')[0]
    await bot.send_message(user_id, f'{message.text}')
    await message.answer()
  except AttributeError:
    await message.answer(f'Используйте предыдущие сообщения для ответа')