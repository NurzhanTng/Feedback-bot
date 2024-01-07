from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message


class NotCommand(BaseFilter):
  async def __call__(self, message: Message) -> Any:
    if message.text.startswith('/'):
      return False
    return True