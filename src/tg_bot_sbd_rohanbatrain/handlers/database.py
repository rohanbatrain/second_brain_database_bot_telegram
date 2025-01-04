from pymongo import MongoClient # type: ignore
from collections import OrderedDict

# Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client['sbd']
collection = db['telegram_bot']

# Cache to store backend URLs with a max limit of 1000
backend_url_cache = OrderedDict()

def get_backend_url(user_id: int) -> str:
    """
    Retrieve the backend URL for a given user ID. If the URL is cached, return it from the cache.
    Otherwise, fetch it from the database, cache it, and return it. The cache has a max limit of 1000 entries.

    Args:
        user_id (int): The user ID for which to retrieve the backend URL.

    Returns:
        str: The backend URL for the given user ID, or "Backend URL not found" if not available.
    """
    if user_id in backend_url_cache:
        # Move the accessed item to the end to show that it was recently used
        backend_url_cache.move_to_end(user_id)
        return backend_url_cache[user_id]
    
    user_data = collection.find_one({"user_id": user_id})
    if user_data and "backend_url" in user_data:
        backend_url = user_data["backend_url"]
        backend_url_cache[user_id] = backend_url
        # If the cache exceeds the max limit, remove the oldest item
        if len(backend_url_cache) > 1000:
            backend_url_cache.popitem(last=False)
        return backend_url
    else:
        return "Backend URL not found"