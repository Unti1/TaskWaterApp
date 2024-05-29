from settings import *
router = Router()

@router.message(Command('start'))
async def send_welcome(message: types.Message):
    if os.path.exists(USER_DATA_PATH):

        with open(USER_DATA_PATH, 'r', encoding='utf-8') as fl:
           json_data = json.load(fl)
        
        json_data['subscribed_users'].append(message.chat.id)

        with open(USER_DATA_PATH, 'w', encoding='utf-8') as fl:
           json_data = json.dump(fl)
    else:    
        json_data['subscribed_users'] = [message.chat.id]

        with open(USER_DATA_PATH, 'w', encoding='utf-8') as fl:
           json_data = json.dump(fl)
        
    await message.reply("Welcome! This bot will send you daily reports at 21:00. If you want desubscribe you can use command /desub")

@router.message(Command('start'))
async def send_welcome(message: types.Message):
    try:
        if os.path.exists(USER_DATA_PATH):
            with open(USER_DATA_PATH, 'r', encoding='utf-8') as fl:
               json_data = json.load(fl)

            json_data['subscribed_users'].remove(message.chat.id)

            with open(USER_DATA_PATH, 'w', encoding='utf-8') as fl:
               json_data = json.dump(fl)
    except ValueError:
        await message.reply("You are not subscribed on daily report yet")
        return
    await message.reply("This bot will not send you daily reports. If you want subscribe again you can use command /start")