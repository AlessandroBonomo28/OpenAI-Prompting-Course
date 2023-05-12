import telepot, openai
import time,datetime, os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')
openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def yoda_response(prompt : str):
    return get_completion(prompt+ "\n\nRispondi come se fossi il maestro Yoda di Star Wars.")

start_time = datetime.datetime.now() 
chat_id_allow = os.getenv("WHITELIST_ID_TELEGRAM").split(",") # IDs stored in .env as Comma Separated Values
# Example of WHITELIST: WHITELIST_ID_TELEGRAM = 123456,24566,344142
infoMessage = """
Commands:\n
1)/ping 🏓
2)/info ❔
3)/time ⏳
"""

def get_message_time_elapsed() -> str:
    now = datetime.datetime.now() 
    seconds = abs(start_time - now).seconds
    minutes = seconds/60
    hours = minutes/60
    days = abs(start_time - now).days
    return f"""Long time passed since Yoda was born ⏳.\n\n{seconds} seconds\n{int(minutes)} minutes\n{int(hours)} hours\n{days} days\n"""

def send_info_commands(chat_id):
    bot.sendMessage(chat_id,infoMessage)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_id not in chat_id_allow:
        bot.sendMessage(chat_id, "I can't share my knowledge with you ⛔.")
        return
    #print(chat_id)
    if content_type == 'text':
        if msg["text"] == "/ping": 
            bot.sendMessage(chat_id, 'pong 🏓')
        elif msg["text"] == "/info": 
            send_info_commands(chat_id)
        elif msg["text"] == "/time": 
            bot.sendMessage(chat_id, get_message_time_elapsed())
        else:
            bot.sendMessage(chat_id, yoda_response(msg["text"]))

bot = telepot.Bot(TOKEN_TELEGRAM)
bot.message_loop(on_chat_message)
    
for id in chat_id_allow:
    bot.sendMessage(id, f'May the force be with you..🍀')
    send_info_commands(id)
print ('Yoda listening ...')


while 1:
    time.sleep(100)
