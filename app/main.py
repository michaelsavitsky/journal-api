from typing import List
from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.entry import EntryModel, UpdateEntryModel
from app.database import db

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", response_description="List all entries", response_model=List[EntryModel])
async def list_entries():
    entries = await db["entries"].find().to_list(1000)
    return entries

@app.get("/{id}", response_description="Get single entry", response_model=EntryModel)
async def get_entry(id: str):
    if (entry := await db["entries"].find_one({"_id": ObjectId(id)})) is not None:
        return entry
    
    raise HTTPException(status_code=404, detail=f"Entry {id} not found")

@app.put("/{id}", response_description="Update entry", response_model=EntryModel)
async def update_entries(id: str, entry: UpdateEntryModel):
    entry = {k: v for k, v in entry.dict().items if v is not None}

    if len(entry) >= 1:
        update_result = await db["entries"].update_one({"_id": ObjectId(id)}, {"$set": entry})

        if update_result.modified_count == 1:
            if (
                updated_entry := await db["entries"].find_one({"_id": ObjectId(id)})
            ) is not None:
                return updated_entry

    if (existing_entry := await db["entries"].find_one({"_id": ObjectId(id)})) is not None:
        return existing_entry

    raise HTTPException(status_code=404, detail=f"Entry {id} not found")

# @app.delete("/{id}", response_description="Delete an entry")
# async def delete_entry(id: str):
#     delete_result = await db["entries"].delete_one({"_id": ObjectId(id)})

#     if delete_result.deleted_count == 1:
#         raise HTTPException(status_code=204)

#     raise HTTPException(status_code=404, detail=f"entry {id} not found")