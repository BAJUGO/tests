from funcs import get_connection

def main():
    with get_connection() as conn:
        print(conn)
        while True:
            pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt happened\n")



# import pika
#
# credentials = pika.PlainCredentials("user", "password")
#
# connection_params = pika.ConnectionParameters(
#     host="localhost",
#     port=5672,
#     credentials=credentials,
# )
#
#
# def main():
#     with pika.BlockingConnection(connection_params) as conn:
#         with conn.channel() as ch:
#             ch.queue_declare(queue="messages")
#
#             ch.basic_publish(
#                 exchange="",
#                 routing_key="messages",
#                 body=b"Hello RabbitMQ",
#             )
#             print("Message sent")
#
#
# if __name__ == "__main__":
#     main()