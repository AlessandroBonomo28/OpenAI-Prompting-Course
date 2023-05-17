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
> \# If you are using windows Windows
> 
> ./env/Scripts/activate
> 
> \# If you are using Linux
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
Is a basic template that I made for making custom telegram bots. This bot speaks like Yoda from Star Wars.
### Multi ego bot
Is a more sofisticated bot that and can switch into its neapolitan alter ego.
#### Bot in action
Yoda can do a lot of things! Here's an example of me chatting with him

![yodacommands](https://github.com/AlessandroBonomo28/OpenAI-Prompting-Course/assets/75626033/c52e7fdd-145b-4666-a22e-7d6b04707812)

Now let's ask him some questions

![story](https://github.com/AlessandroBonomo28/OpenAI-Prompting-Course/assets/75626033/e1d5387c-3a2e-4494-bd42-81b140c506c3)

Yoda seems pretty chill, let's switch to its neapolitan ego



## .env configuration for scripts in the telegram folder
> \#.env file
>
> OPENAI_API_KEY = "xxxxxxx"
> 
> TOKEN_TELEGRAM = "xxxxxxx"
> 
> WHITELIST_ID_TELEGRAM = "aaaa,bbbb,cccc,ddddd"
