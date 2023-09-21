
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from base import Otp 
from motor.motor_asyncio import AsyncIOMotorClient

uri = 'mongodb+srv://nashospital:PU153a2P7Ijd6BeH@cluster0.epfrp5b.mongodb.net/?retryWrites=true&w=majority'
# uri = "mongodb://localhost:27017"
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

database = client.nashospital
collection = database.otpcodes    

async def fetch_one():
     document = await collection.find_one({"name": "Akansha"})
     return True

async def add_otp(item):
     document = item
     res = collection.insert_one(document)
     return res
  
async def fetch_all():
      datas = []
      data =  collection.find({})
      async for d in data:
          #  print(d)
          datas.append(d)
      print(datas)
     #  return datas