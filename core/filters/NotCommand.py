from aiogram.filters import BaseFilter
from aiogram.types import Message


class NotCommand(BaseFilter):
  async def __call__(self, message: Message):
    if message.text.startswith('/'):
      return False
    return True