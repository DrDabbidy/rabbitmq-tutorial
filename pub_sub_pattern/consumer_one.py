import pika


def on_message_recieved(ch, method, properties, body):
    print(f"consumer_one recieved '{body}'")


connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# We must declare the exchange on the producer and consumer side.
channel.exchange_declare(exchange="pubsub", exchange_type="fanout")

# exclusive=True means that when connection is closed, this queue can be deleted
# we don't need to set a name becuase it's only for this connection
queue = channel.queue_declare(queue="", exclusive=True)

# we must bind the queue to the exchange
channel.queue_bind(exchange="pubsub", queue=queue.method.queue)

channel.basic_consume(
    queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_recieved
)
print("Waiting for messages...\n")

channel.start_consuming()
