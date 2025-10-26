from telethon import TelegramClient, events
from telethon.tl.types import Document
import json, datetime, os, asyncio, signal, sys

# ================= CONFIG =================
api_id = 26171619
api_hash = '3c260ef7c1b76977ee4f661fd96db072'
session_name = 'gate_listener_session'

channels_to_listen = ['gatecsitstudymaterial']
KEYWORDS = [
    "DBMS"
]

HISTORICAL_LIMIT = 100
DOWNLOAD_DIR = "downloads"
JSON_FILE = "messages.json"

# ================= SETUP =================
def signal_handler(sig, frame):
    print("\n Stopping collector...")
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)
client = TelegramClient(session_name, api_id, api_hash)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

# ================= HELPERS =================
def contains_keyword(text):
    if not KEYWORDS: return True
    if not text: return False
    return any(keyword.lower() in text.lower() for keyword in KEYWORDS)

def save_message(data):
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            messages = json.load(f)
    except: messages = []
    
    if not any(msg.get('id') == data.get('id') for msg in messages):
        messages.append(data)
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)

async def download_pdf(message):
    try:
        if not message.media or not isinstance(message.media, Document):
            return None
        
        file_name = message.file.name or f"document_{message.id}.pdf"
        if not file_name.lower().endswith('.pdf'):
            return None
        
        file_path = os.path.join(DOWNLOAD_DIR, file_name)
        if not os.path.exists(file_path):
            await message.download_media(file=file_path)
            print(f"📥 Downloaded: {file_name}")
        
        return file_path
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

# ================= HISTORICAL FETCH =================
async def fetch_historical_messages():
    print(f" Fetching last {HISTORICAL_LIMIT} messages...")
    
    for channel in channels_to_listen:
        try:
            print(f" Scanning: {channel}")
            total_processed = 0
            total_saved = 0
            
            async for message in client.iter_messages(channel, limit=HISTORICAL_LIMIT):
                total_processed += 1
                msg_text = message.text or ""
                pdf_path = None
                
                if total_processed % 20 == 0:
                    print(f"   Progress: {total_processed}/{HISTORICAL_LIMIT}")
                
                if message.media and isinstance(message.media, Document):
                    pdf_path = await download_pdf(message)
                
                if contains_keyword(msg_text):
                    data = {
                        "id": message.id,
                        "channel": channel,
                        "message": msg_text,
                        "pdf_file": pdf_path,
                        "timestamp": message.date.isoformat(),
                        "type": "historical"
                    }
                    save_message(data)
                    total_saved += 1
            
            print(f" {channel}: Saved {total_saved} out of {total_processed} messages")
            
        except Exception as e:
            print(f" Error processing {channel}: {e}")

# ================= REAL-TIME LISTENER =================
@client.on(events.NewMessage(chats=channels_to_listen))
async def real_time_handler(event):
    try:
        msg_text = event.message.text or ""
        pdf_path = None
        
        if event.message.media and isinstance(event.message.media, Document):
            pdf_path = await download_pdf(event.message)
            print(f" New PDF: {event.message.file.name}")
        
        if contains_keyword(msg_text):
            data = {
                "id": event.message.id,
                "channel": getattr(event.chat, 'username', 'Unknown'),
                "message": msg_text,
                "pdf_file": pdf_path,
                "timestamp": datetime.datetime.utcnow().isoformat(),
                "type": "real_time"
            }
            save_message(data)
            print(f" New message: {msg_text[:60]}...")
            
    except Exception as e:
        print(f"❌ Error processing real-time message: {e}")

# ================= MAIN =================
async def main():
    print(" Starting GATE Study Material Collector...")
    await client.start()
    print(" Connected to Telegram!")
    
    await fetch_historical_messages()
    
    print(" Listening for new messages... (Ctrl+C to stop)")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n Collector stopped!")