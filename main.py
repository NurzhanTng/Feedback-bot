import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

from core.handlers import basic, author
from core.settings import settings

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main(): 
  logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
  )
  bot  = Bot(settings.bots.bot_token)
  dp = Dispatcher()
  
  dp.message.middleware.register(ChatActionMiddleware())

  dp.include_routers(author.router, basic.router)
  
  try:
    await dp.start_polling(bot)
  finally:
    await bot.session.close()

if __name__ == "__main__":
  asyncio.run(main())
