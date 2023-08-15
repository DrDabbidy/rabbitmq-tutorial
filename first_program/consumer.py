import pika


def on_message_recieved(ch, method, properties, body):
    print(f"Recieved '{body}'")


connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

channel.basic_consume(
    queue="letterbox", auto_ack=True, on_message_callback=on_message_recieved
)
print("Waiting for messages...")

channel.start_consuming()
