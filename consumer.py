from kafka import KafkaConsumer
import json

product_categories = {
    "Fruit": ["apple", "banana", "orange", "pear", "kiwi"],
    "Bakery": ["bread", "croissant", "baguette", "cake"],
    "Drink": ["water", "soda", "beer", "wine"],
}

def categorize_products(order):
    for product in order["products"]:
        name = product["name"].lower()
        for category, products in product_categories.items():
            if name in products:
                product["category"] = category
                break

def process_order(order):
    categorize_products(order)
    total_price = sum(product["price"] for product in order["products"])
    order["total_price"] = total_price
    return order

consumer = KafkaConsumer("orders", bootstrap_servers=["localhost:9092"])

with open("database.json", "w") as f:
    for message in consumer:
        order = message.value
        processed_order = process_order(order)
        f.write(json.dump(processed_order))
        f.write("\n")