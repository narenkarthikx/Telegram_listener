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

## GATE Telegram Study Material Collector

This project listens to Telegram channels, fetches historical messages, filters them by keywords, and downloads attached PDF study materials. It also saves collected messages to `messages.json` and can run continuously to capture new posts in real time.

## Features
- Fetch historical messages from one or more Telegram channels
- Filter messages by keywords (e.g., "GATE", "DBMS", "notes")
- Auto-download PDFs and save them to the `downloads/` folder
- Save message metadata to `messages.json`
- Keep a persistent Telegram session in `gate_listener_session.session`

## Quick start
1. Install dependencies

```powershell
pip install telethon
```

2. Run the listener

```powershell
python listener.py
```

Note: On first run you'll be prompted for your phone number and the Telegram login code.

## Configuration
Open `listener.py` and edit the following variables to suit your needs:

- `channels_to_listen` — list of channel usernames or IDs, e.g. `['gatecsitstudymaterial']`
- `KEYWORDS` — list of keywords to filter messages. Use `[]` to save everything.
- `HISTORICAL_LIMIT` — number of past messages to fetch per channel (e.g., `100`).

Example (in `listener.py`):

```python
channels_to_listen = ['gatecsitstudymaterial']
KEYWORDS = ["DBMS", "GATE", "PYQ", "notes", "pdf", "syllabus"]
HISTORICAL_LIMIT = 100
```

## Output / Files
- `messages.json` — stored message records and metadata
- `downloads/` — folder where PDF files are saved
- `gate_listener_session.session` — Telegram session file (keeps you logged in)

Sample saved record:

```json
{
  "id": 123,
  "channel": "gatecsitstudymaterial",
  "message": "DBMS notes for GATE 2025",
  "pdf_file": "downloads/dbms_notes.pdf",
  "timestamp": "2024-01-15T10:30:00",
  "type": "historical"
}
```

## Usage notes
- The script fetches historical messages up to `HISTORICAL_LIMIT` and then listens for new messages.
- Stop the listener with Ctrl+C.
- If you want to collect everything, set `KEYWORDS = []`.

## Troubleshooting
- No messages? Make sure your account has joined the channel(s) you want to read.
- PDFs not downloading: check internet access and file permissions for the `downloads/` folder.
- Login problems: delete `gate_listener_session.session` and re-run to re-authenticate.

## Safety & Privacy
- The script uses your Telegram account to access channels you have access to. Do not share `gate_listener_session.session`.

## Next steps / Improvements
- Add command-line arguments for channels, keywords and limits.
- Add logging and retry logic for failed downloads.
- Add unit tests for message parsing and filtering.

---

If you want, I can also add a short example `listener.py` snippet or add command-line flags — tell me which you prefer.