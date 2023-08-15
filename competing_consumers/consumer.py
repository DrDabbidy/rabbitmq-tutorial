import pika
import time
import random


def on_message_recieved(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"Recieved '{body}'. Will take {processing_time} seconds to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"Finished processing '{body}'")


connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

# This option is what allows for the competing consumers pattern.
# It will not assign a message to a consumer if the consumer is still
# processing a message.
# We have to run multiple instances of the consumer script for this to work
# or we have to develop a program with multiple threads.
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="letterbox", on_message_callback=on_message_recieved)
print("Waiting for messages...")

channel.start_consuming()
