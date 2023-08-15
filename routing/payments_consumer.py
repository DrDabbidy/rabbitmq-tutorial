import pika


def callback(ch, method, properties, body):
    print(f"Recieved payment: {body}. Route: {method.routing_key}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange = channel.exchange_declare(exchange="router", exchange_type="topic")

queue = channel.queue_declare(queue="", exclusive=True)

channel.queue_bind(
    exchange="router", queue=queue.method.queue, routing_key="user.payments"
)

channel.basic_consume(queue=queue.method.queue, on_message_callback=callback)

channel.start_consuming()
