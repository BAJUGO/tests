from funcs import get_connection

def produce_channel(channel) -> None:
    queue = channel.queue_declare(queue="hellos")
    channel.basic_publish(
        exchange="", # direct exchange
        routing_key="hellos", # По этому адрессу доставляем / получаем данные
        # ЭТО именно выбор очереди, куда отправлять (без объявления очереди отправлять некуда)
        body=b"hello_world totally new"
    )


def main():
    with get_connection() as conn:
        with conn.channel() as channel:
            produce_channel(channel)




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