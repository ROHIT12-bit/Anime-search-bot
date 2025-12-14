from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Create bot client
app = Client(
    name="anime_search_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ==============================
# Import all handlers
# ==============================
from handlers.start import start
from handlers.search import search
from handlers.callback import callbacks
from handlers.owner import stats

# ==============================
# Bot start
# ==============================
if name == "main":
    print("🤖 Anime Search Bot Started...")
    app.run()
