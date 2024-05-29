#!/usr/bin/env python
# coding: utf-8

# In[2]:


import telebot
import openai

# Set up OpenAI API key
openai.api_key ='your chat GPT API key '

# Set up Telegram Bot token
TOKEN = 'Your Telegram Bot API KEY '

# Initialize the Telegram Bot
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Lunar magic bot! I am here to assist you. Type /info to get more information.")

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "Hi, this is Lunar magic! How can I assist you today?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.lower()  # Convert user input to lowercase for case-insensitive matching
    
    bot_response = ""
    if user_input == "hai" or user_input == "hi" or user_input == "hii" or user_input == "hello":
        bot_response = "Hai, this is Lunar developed by @itz_classy. How can I help you?"
    if bot_response:  # Check if bot_response is not empty
        bot.reply_to(message, bot_response)
    else:
        # If no specific response matched, generate AI response
        ai_response = generate_ai_response(user_input)
        bot.reply_to(message, ai_response)

def generate_ai_response(prompt):
    model_engine = "gpt-3.5-turbo-instruct" 
    max_tokens = 1050

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return completion.choices[0].text.strip()

# Start the bot
bot.polling()

