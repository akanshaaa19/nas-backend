from pymongo.server_api import ServerApi
from pymongo.server_api import ServerApi
from base import Doctor 
from motor.motor_asyncio import AsyncIOMotorClient

uri = 'mongodb+srv://nashospital:PU153a2P7Ijd6BeH@cluster0.epfrp5b.mongodb.net/?retryWrites=true&w=majority'
# uri = "mongodb://localhost:27017"
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

database = client.nashospital
docCollection = database.doctors

async def add_doctor(document):
    print(document)    
    result = await docCollection.insert_one(document)
    return result