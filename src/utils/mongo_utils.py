import os
from typing import Any

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database


def get_mongo_database() -> Database[Any]:
    """Return a MongoDB database object using values from environment variables."""
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    mongo_db = os.getenv("MONGO_DB", "crop_yield_pakistan")

    client = MongoClient(mongo_uri)
    return client[mongo_db]
