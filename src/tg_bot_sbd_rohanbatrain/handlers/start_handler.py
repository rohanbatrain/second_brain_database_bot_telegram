from telegram import Update
from telegram.ext import ContextTypes

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    await update.message.reply_text("Welcome to the bot! Use /help to see what I can do.")
