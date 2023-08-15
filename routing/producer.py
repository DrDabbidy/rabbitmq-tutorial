import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

exchange = channel.exchange_declare(exchange="router", exchange_type="topic")

# publish a message to user.purchases
channel.basic_publish(
    exchange="router",
    routing_key="user.purchases",
    body="User purchased some goods.",
)
print("Sent 'User purchased some goods.'")

# publish a message to user.payments
channel.basic_publish(
    exchange="router",
    routing_key="user.payments",
    body="User made a payment.",
)
print("Sent 'User made a payment.'")
