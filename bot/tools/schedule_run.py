from settings import *
from app.models import Store

async def send_daily_report(bot:Bot, user_id: int, STORE_ID:int) -> None:
    store = Store.get_store(STORE_ID)
    if not store:
        await bot.send_message(user_id, f"No report available for store {STORE_ID}")
        return
    
    report = "\n".join([f"Item ID: {item['item_id']}, Quantity: {item['quantity']}" for item in store['report']])
    await bot.send_message(user_id, f"Daily report for store {STORE_ID}:\n{report}", parse_mode=ParseMode.HTML)
