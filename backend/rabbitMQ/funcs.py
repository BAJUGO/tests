import pika


RMQ_HOST = "0.0.0.0"
RMQ_PORT = "5672"

credentials = pika.PlainCredentials("user", "password")

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=credentials
)

def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(
        parameters=connection_params,
    )



