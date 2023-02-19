from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "6117473467:AAHgj3sCqGc23LwIsetiEkq5L9Fug84qf9c"  # Your bot API key
    OWNER_ID = 1234567890  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [1234567890, 6234365091]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001572866647]  # List of chat id's to forward messages to.

    REMOVE_TAG = True
    WORKERS = 4
