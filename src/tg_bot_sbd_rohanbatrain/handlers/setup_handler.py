from tg_bot_sbd_rohanbatrain.config import USER_BACKEND_URLS
from telegram import Update
from telegram.ext import ContextTypes
from tg_bot_sbd_rohanbatrain.handlers.database import collection



async def handle_setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract command and backend URL from the message
    if len(context.args) < 2 or context.args[0] != "backend_url":
        await update.message.reply_text("Usage: /setup backend_url <url>")
        return
    
    backend_url = context.args[1]
    
    # Store the backend URL in MongoDB
    user_id = update.message.from_user.id
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"backend_url": backend_url}},
        upsert=True
    )
    
    await update.message.reply_text(f"Backend URL '{backend_url}' has been set up successfully.")