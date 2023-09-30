from models import MSG
from dependencies import process_orders
from fastapi import FastAPI
from redis import Redis
import os

REDIS_URL = os.getenv("REDIS_URL")
cache = Redis.from_url(REDIS_URL)

app = FastAPI()

@app.post("/solution")
def solution(msg: MSG) -> float:
    """
    The endpoint return the result of executing the function process_orders() with the parameters obtained 

    Parameters:
    - msg: A ModelBase containing the orders and the criterion.

    Returns:
    - float: The total revenue for the filtered orders.
    """
    result = cache.get(msg.model_dump_json())
    
    if not result:
        result = process_orders(msg.orders, msg.criterion)
        cache.set(msg.model_dump_json(), result)
    
    return float(result)