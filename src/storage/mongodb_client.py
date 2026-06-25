import os

from pymongo import MongoClient


DEFAULT_MONGO_URI = (
    "mongodb://localhost:27017"
)

DEFAULT_DATABASE = "bed_monitoring"


class MongoDBClient:

    def __init__(
        self,
        uri=None,
        database=None
    ):

        self.uri = (
            uri
            or os.getenv("MONGO_URI")
            or DEFAULT_MONGO_URI
        )

        self.database_name = (
            database
            or os.getenv("MONGO_DATABASE")
            or DEFAULT_DATABASE
        )

        self.client = MongoClient(
            self.uri,
            serverSelectionTimeoutMS=3000
        )

        self.db = self.client[
            self.database_name
        ]

    def connect(self):

        self.client.admin.command(
            "ping"
        )

        return self.db

    def get_collection(
        self,
        collection_name
    ):

        return self.db[
            collection_name
        ]

    def close(self):

        self.client.close()
