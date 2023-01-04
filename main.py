from fastapi import FastAPI, Request
import json
from kafka import KafkaProducer
import asyncio

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=["localhost:9092"], value_serializer=lambda x: json.dumps(x).encode('utf-8'))
topic = 'delhaize_shop'

@app.post("/data")
async def data(order: dict):

    print(order)
    producer.send(topic, value=order)
    producer.flush()

    return {"status": "ok"}