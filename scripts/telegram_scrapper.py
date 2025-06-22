from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Initialize Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)

# Function to scrape data from a single channel (without media)
async def scrape_channel(client, channel_username, writer):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    async for message in client.iter_messages(entity, limit=10000):
        writer.writerow([
            channel_title,
            channel_username,
            message.id,
            message.message,
            message.date
        ])

# Main script
async def main():
    await client.start()

    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date'])  # Removed 'Media Path'

        channels = [
            '@Shageronlinestore',
            '@ZemenExpress',
            '@nevacomputer',
            '@meneshayeofficial',
            '@ethio_brand_collection'
            
        ]

        for channel in channels:
            await scrape_channel(client, channel, writer)
            print(f"✅ Scraped data from {channel}")

with client:
    client.loop.run_until_complete(main())
