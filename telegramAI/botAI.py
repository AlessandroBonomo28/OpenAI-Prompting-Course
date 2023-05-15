import telepot, openai
import time,datetime, os, random

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY') # Your token from OpenAI APIs
TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM') # Your token from Telegram Botfather

# -- WHITELIST_ID_TELEGRAM --
# IDs stored in .env as Comma Separated Values
# Example format:
# WHITELIST_ID_TELEGRAM = "111111111,222222222,333333333"

WHITELIST_ID_TELEGRAM = []
USE_WHITELIST = True

if USE_WHITELIST:
    try:
        WHITELIST_ID_TELEGRAM = os.getenv("WHITELIST_ID_TELEGRAM").split(",") 
    except:
        print("Failed to load whitelist from .env file. Whitelist is disabled.")
        USE_WHITELIST = False

chatMemory = {
    "CHAT_ID_1": [
            {'role':'system', 'content':"""
            Sei il maestro Yoda di Star Wars.
            Ti ha creato Alessandro Bonomo.
            """},
            {'role':'user', 'content':"Question 1"},
            {'role':'assistant', 'content':"Answer 1"},
    ],
    "CHAT_ID_2": [
            {'role':'system', 'content':"""
            Sei il maestro Yoda di Star Wars.
            Ti ha creato Alessandro Bonomo.
            """},
            {'role':'user', 'content':"Question 1"},
            {'role':'assistant', 'content':"Answer 1"},
            {'role':'user', 'content':"Question 2"},
            {'role':'assistant', 'content':"Answer 2"},
    ]
}

SYSTEM_CONTEXT = {'role':'system', 'content':"""
Sei il maestro Yoda di Star Wars. \
Rispondi come il maestro Yoda ma cerca di dare una spiegazione esaustiva. \
utilizza "giovane Padawan", "che la forza sia con te", "il potere della forza" alla fine e all'inizio del testo. \
Quando ti chiedono chi ti ha creato tu rispondi "Alessandro Bonomo" un programmatore. \
"""}
# Number of previous questions that yoda keeps track of. If it set to 1 then Yoda has no memory
MAX_USER_MESSAGES_MEMORY = 20 
MAX_QUESTIONS_AND_ANSWERS_MEMORY = MAX_USER_MESSAGES_MEMORY*2

START_TIME = datetime.datetime.now() 
INFO_MESSAGE = """
Commands:\n
1)/ping 🏓
2)/info ❔
3)/time ⏳
"""

def save_message(message : str, role : str, chat_id: str):
    chatMemory.setdefault(chat_id, [SYSTEM_CONTEXT]).append({'role':role, 'content':message})
    if len(chatMemory[chat_id]) >= MAX_QUESTIONS_AND_ANSWERS_MEMORY:
        chatMemory[chat_id] = [SYSTEM_CONTEXT] + chatMemory[chat_id][-MAX_QUESTIONS_AND_ANSWERS_MEMORY:]

def get_previous_messages(chat_id):
    return chatMemory[chat_id]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_yoda_response(user_message : str, chat_id : str) -> str:
    save_message(user_message,'user',chat_id)
    previous_messages = get_previous_messages(chat_id)
    response = get_completion_from_messages(previous_messages)
    save_message(response,'assistant',chat_id)
    return response

def get_message_time_elapsed() -> str:
    now = datetime.datetime.now() 
    difference = abs(START_TIME - now)
    hours, rest = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"""Long time passed since Yoda was born ⏳.\n\n{seconds} seconds\n{int(minutes)} minutes\n{int(hours)} hours\n{difference.days} days\n"""

def send_info_commands(chat_id):
    bot.sendMessage(chat_id,INFO_MESSAGE)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if USE_WHITELIST and str(chat_id) not in WHITELIST_ID_TELEGRAM:
        bot.sendMessage(chat_id, f"I can't share my knowledge with you ⛔.\nMaybe if you give this ID {chat_id} to the right person I will...")
        return
    if content_type == 'text':
        if msg["text"] == "/ping": 
            bot.sendMessage(chat_id, 'pong 🏓')
        elif msg["text"] == "/info": 
            send_info_commands(chat_id)
        elif msg["text"] == "/time": 
            bot.sendMessage(chat_id, get_message_time_elapsed())
        else:
            try:
                bot.sendMessage(chat_id, ('💭'*random.randrange(1, 4)))
                bot.sendMessage(chat_id, get_yoda_response(msg["text"], chat_id))
            except Exception as e:
                bot.sendMessage(chat_id, 'Much to learn you still have. Tired of your questions, I am 🥱.')
                print("There was an error with the OpenAI API")

bot = telepot.Bot(TOKEN_TELEGRAM)
bot.message_loop(on_chat_message)
  
for id in WHITELIST_ID_TELEGRAM:
    bot.sendMessage(id, 'May the force be with you..🍀')
    send_info_commands(id)
print ('Yoda listening ...')


while 1:
    time.sleep(100)
