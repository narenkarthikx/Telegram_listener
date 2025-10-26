GATE Telegram Study Material Collector

Automatically fetches study materials from Telegram channels, filters by keywords, and downloads PDFs.

📥 Features

Fetches historical messages from Telegram channels

Filters messages based on keywords

Downloads PDF files automatically

Saves all messages to a JSON file

Listens for new messages in real-time

⚡ Quick Start
1. Install Dependencies
pip install telethon

2. Run the Listener
python listener.py


Note: The first time you run it, you'll need to enter your phone number and the login code sent by Telegram.

⚙️ Configuration

Edit listener.py to configure channels, keywords, and fetch limits.

Channels
channels_to_listen = ['gatecsitstudymaterial']  # Add more channels if needed

Keywords (for filtering messages)
KEYWORDS = ["DBMS", "GATE", "PYQ", "notes", "pdf", "syllabus"]


To save all messages without filtering:

KEYWORDS = []  # Empty list = save everything

Fetch Limit (historical messages)
HISTORICAL_LIMIT = 100  # Fetch last 100 messages from each channel

💡 What It Does

Fetches last HISTORICAL_LIMIT messages from each channel

Filters messages containing the keywords

Downloads PDF files automatically to downloads/ folder

Saves messages in messages.json

Listens for new messages in real-time

Stop the listener anytime with Ctrl+C

🗂️ Files Created

messages.json – All collected messages

downloads/ – PDF files folder

gate_listener_session.session – Telegram login session

📑 Output Example
{
  "id": 123,
  "channel": "gatecsitstudymaterial",
  "message": "DBMS notes for GATE 2025",
  "pdf_file": "downloads/dbms_notes.pdf",
  "timestamp": "2024-01-15T10:30:00",
  "type": "historical"
}

🛠️ Troubleshooting

No messages? Check if you've joined the channels

PDFs not downloading? Check your internet connection

Login issues? Delete .session file and try again