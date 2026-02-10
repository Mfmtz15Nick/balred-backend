from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

class MongoDBClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDBClient, cls).__new__(cls, *args, **kwargs)
            cls._instance._init_client(*args, **kwargs)
        return cls._instance

    def _init_client(self, *args, **kwargs):
        # uri = 'mongodb+srv://mfonseca:4jbRemCIoRhDIUWy@heatmapcluster.ouq6agc.mongodb.net/?retryWrites=true&w=majority&appName=HeatmapCluster'  # Replace with your actual MongoDB URI
        # uri = 'mongodb+srv://balredroot:gJLFObX8hVtniFb5@cluster0.tkgfx2p.mongodb.net/?appName=Cluster0'
        uri = os.getenv('MONGO_URI')
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client['balred']  # Replace with your actual database name

    def get_db(self):
        return self.db

def ping_mongo():
    client = MongoDBClient().client
    try:
        client.admin.command('ping')
        return True
    except Exception as e:
        print(f'Error connecting to MongoDB: {e}')
        return False

def create_mongo_client():
    return MongoDBClient()





