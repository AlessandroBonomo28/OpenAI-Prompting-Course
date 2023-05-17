# OpenAI Prompting Course
 Prompting ChatGPT-3 course by OpenAI
 https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
## Get started
Note: I am using *Python 3.11.0* but I think that this with work also with *3.9* and *3.10* 
- Get the GPT API key from the offical website of OpenAI
- Create a virtual environment 
> python -v venv env
- Create a file named *.env* and edit as follows
> \# .env file
> 
> OPENAI_API_KEY = "Your api key"
- run the environment
> \# in Windows
> 
> ./env/Scripts/activate

> \# in Linux
> 
> source env/bin/activate

- install dependencies
> pip install -r requirements.txt

*Now you can run any python file in the repository*
> python file.py
## What you will find in this repo
In this repo there are two main folders
- lessons
- telegram

**In the lesson folder** there are code example of gpt prompting. I advice you to start with start.py.
**In the telegram folder** I made a telegram chatbot powered by ChatGPT AI. You will find two scripts in this folder:
- multi-ego-bot.py
- simple-bot.py

###  Simple-bot
Is a basic template that I made for making custom telegram bot. This bot speaks like Yoda from Star Wars.
### Multi ego bot
Is a more sofisticated bot that and can switch into its neapolitan alter ego.
## .env configuration for scripts in the telegram folder
> \#.env file
>
> OPENAI_API_KEY = "xxxxxxx"
> 
> TOKEN_TELEGRAM = "xxxxxxx"
> 
> WHITELIST_ID_TELEGRAM = "aaaa,bbbb,cccc,ddddd"
