import pika
import time
import random

connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

i = 1
while True:
    message = f"Message number {i}."
    i += 1

    channel.basic_publish(exchange="", routing_key="letterbox", body=message)
    print(f"Sent '{message}'")

    time.sleep(random.randint(1, 3))
