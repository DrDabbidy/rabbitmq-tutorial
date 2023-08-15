import pika

# Can also use this Enum instead of direct str
# from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host="localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# fanout exchange will push the message onto each queue that is bound to it.
channel.exchange_declare(exchange="pubsub", exchange_type="fanout")

message = "Hello World!"

channel.basic_publish(exchange="pubsub", routing_key="letterbox", body=message)
print(f"Sent '{message}'")

connection.close()
