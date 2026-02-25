from funcs import get_connection
from time import sleep

def declare_queue(channel, queue):
    channel.queue_declare(queue=queue)


def produce_channel(channel, idx: int) -> None:
    body = f"New message with index {idx}"
    channel.basic_publish(
        exchange="", # direct exchange
        routing_key="hellos", # По этому адрессу доставляем / получаем данные
        # ЭТО именно выбор очереди, куда отправлять (без объявления очереди отправлять некуда)
        body=body
    )
    print(f"published message with index {int(body[-2:])}")



def main():
    with get_connection() as conn: # pika.BlockingConnection
        with conn.channel() as channel:
            declare_queue(channel, "hellos")
            for idx in range(1, 11):
                produce_channel(channel, idx=idx)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt happened\n")
