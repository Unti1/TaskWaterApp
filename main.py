from .app.routes import router
from settings import *
from bot.handlers import *
app = FastAPI()

app.include_router(router)

async def bot_start():
    bot = Bot(token = config['telegram']['api'])

    dp = Dispatcher()
    dp.include_routers(
                       commands.router,
                       messages.router
                       )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
