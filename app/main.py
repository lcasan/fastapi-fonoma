from models import Json
from dependencies import process_orders
from fastapi import FastAPI

app = FastAPI()

@app.post("/solution")
def solution(json: Json):
    return process_orders(json.orders, json.criterion)