from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
def read_root():
    return {
        "Persons": {
            "Alek Stagram": "A Hellknight of the ",
            "Warbal Bumblebrasher": "A goblin from the Bumblebrasher clan"
        },
        "Factions": {
            "Hellknights": "An order of knights",
            "Bumblebrashers": "A clan of goblins that had set up in the ruins of Castle Altaerein"
        },
        "Locations": {
            "Breachill": "The town where the adventure began"
        }
    }