from telegram import Update
from telegram.ext import CallbackContext, CommandHandler
from tg_bot_sbd_rohanbatrain.handlers.database import get_backend_url


async def profile_handler(update: Update, context: CallbackContext):
    """
    Respond to the /profile command.

    Display the user's profile information.
    """
    user_id = update.message.from_user.id
    backend_url = get_backend_url(user_id)
    response = f"👤 *Profile*\n\n" f"User ID: {user_id}\n" f"Backend URL: {backend_url}"
    await update.message.reply_text(response, parse_mode="Markdown")
