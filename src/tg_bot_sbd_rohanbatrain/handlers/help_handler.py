from telegram import Update
from telegram.ext import ContextTypes

async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Respond to the /help command.

    Provides a brief description of the bot's capabilities.
    """
    response = (
        "🤖 *Help Menu*\n\n"
        "This bot supports the following commands:\n"
        "- /start: Start the bot and see a welcome message.\n"
        "- /help: Display this help menu.\n\n"
        "More features coming soon! 🚀"
    )
    await update.message.reply_text(response, parse_mode="Markdown")
