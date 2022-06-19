import random
from pymongo import MongoClient

from constants import MONGODB_URI, SITE_URL, CHARS


class Database:
    def __init__(self) -> None:
        client = MongoClient(MONGODB_URI)["url-shortener"]
        self.urls = client["urls"]

    def create_url(self, url: str) -> str:
        _id = "".join(random.choices(CHARS, k=8))

        self.urls.insert_one({"_id": _id, "url": url})

        return f"{SITE_URL}/{_id}"

    def get_url(self, url_id: str) -> str:
        url = self.urls.find_one({"_id": url_id})
        if not url:
            return None

        return url["url"]
