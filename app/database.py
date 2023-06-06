from motor.motor_asyncio import AsyncIOMotorClient
import app.settings as settings

client = AsyncIOMotorClient(settings.mongodb_uri)

db = client['journal']