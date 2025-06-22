from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Initialize Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)

channels = [
    '@Shageronlinestore',
    '@ZemenExpress',
    '@nevacomputer',
    '@meneshayeofficial',
    '@ethio_brand_collection'
]

# CSV file setup — Append mode to prevent overwriting
csv_file_path = 'telegram_data.csv'
header = ['Channel Title', 'Channel Username', 'ID', 'Message', 'Date']
if not os.path.exists(csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(header)

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    async for message in client.iter_messages(entity, limit=50):  # Adjust limit for freshness
        writer.writerow([
            channel_title,
            channel_username,
            message.id,
            message.message,
            message.date
        ])

# Main scraping task
async def run_scraper():
    print("🔄 Running scheduled scraping task...")
    await client.start()
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for channel in channels:
            try:
                await scrape_channel(client, channel, writer)
                print(f"✅ Scraped data from {channel}")
            except Exception as e:
                print(f"❌ Error scraping {channel}: {e}")
    print("✅ Scraping cycle complete.")

# Schedule the scraping task
async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(run_scraper, 'interval', minutes=5)  # Run every 5 minutes
    scheduler.start()

    print("⏳ Scheduler started. Press Ctrl+C to stop.")
    while True:
        await asyncio.sleep(3600)  # Keep the script running

# Run everything
with client:
    client.loop.run_until_complete(main())
