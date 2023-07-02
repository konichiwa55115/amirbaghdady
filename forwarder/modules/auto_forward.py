from typing import Union

from telegram import Message, MessageId
from telegram.ext import CallbackContext, Filters, MessageHandler
from telegram.error import ChatMigrated
from telegram.update import Update

from forwarder import FROM_CHATS, LOGGER, REMOVE_TAG, TO_CHATS, dispatcher


def send_message(message: Message, chat_id: int) -> Union[MessageId, Message]:
    if REMOVE_TAG:
        return message.copy(chat_id)
    return message.forward(chat_id)



def forward(update: Update, context: CallbackContext):
    message = update.effective_message
    chat = update.effective_chat
    if not message or not chat:
        return
    from_chat_name = chat.title or chat.first_name

    for chat in TO_CHATS:
        to_chat_name = (
            context.bot.get_chat(chat).title or context.bot.get_chat(chat).first_name
        )
        try:
            send_message(message, chat)
        except :
            send_message(message, chat)
        

try:
    FORWARD_HANDLER = MessageHandler(
        ~Filters.status_update & ~Filters.command,
        forward,
        run_async=True,
    )

    dispatcher.add_handler(FORWARD_HANDLER)

except ValueError:  # When FROM_CHATS list is not set because user doesn't know chat id(s)
    LOGGER.warn("I can't FORWARD_HANDLER because your FROM_CHATS list is empty.")
