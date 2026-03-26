from typing import Final
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from crawl import get_listings, get_addresses, get_prices_and_details
import asyncio
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm Rental-scraper!")

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    listings_links = get_listings()
    addresses = get_addresses()
    prices, details = get_prices_and_details()


    for i in range(len(listings_links)):
        await update.message.reply_text(f"""
address: {addresses[i]}

price: {prices[i].replace("/", "/\u200b")}

square meters: {details[i][0]}

bedrooms: {details[i][1]}

energy label: {details[i][2]}

https://www.funda.nl/{listings_links[i]}""" )
        await asyncio.sleep(0.5)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler("start", start_command)
    list_handler = CommandHandler("list", list_command)
    
    application.add_handler(start_handler)
    application.add_handler(list_handler)
   
    print("Polling...")
    application.run_polling(poll_interval=3)
