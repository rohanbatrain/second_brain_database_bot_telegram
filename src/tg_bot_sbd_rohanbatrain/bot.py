from telegram.ext import Application, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from handlers import start_handler, help_handler, setup_handler, profile_handler


def main():
    # Initialize the application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start_handler.handle_start))
    application.add_handler(CommandHandler("help", help_handler.handle_help))
    application.add_handler(CommandHandler("setup", setup_handler.handle_setup))  # Add setup handler
    application.add_handler(CommandHandler("profile", profile_handler.profile_handler))
    # Run the bot
    application.run_polling()

if __name__ == "__main__":
    main()
