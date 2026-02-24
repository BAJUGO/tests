import pika

credentials = pika.PlainCredentials("user", "password")

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=credentials,
)

def callback(ch, method, properties, body):
    print(f"ВСЯКИЕ НЕНУЖНЫЕ ХУЕПОРАММЕТРЫ:\n{ch}\n{method}\n{properties}\n")
    print(f"Тело: {body.decode()}\n\n")

    ch.basic_ack(delivery_tag=method.delivery_tag) # Сообщения обработаны, если ошибок нет. После чего они удалятся из рэбита



def main():
    with pika.BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:

            ch.basic_consume(
                queue="hello", # из какой очереди взять (объявлять в консьюмере очередь ненужно)
                on_message_callback=callback,
            )
            print("Жду сообщение")
            ch.start_consuming()




if __name__ == "__main__":
    main()