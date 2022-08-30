from typing import Union
from fastapi import FastAPI
from astar_search import astar_search

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/puzzle/")
def get_puzzle_solution():
    return "here would be the solution"