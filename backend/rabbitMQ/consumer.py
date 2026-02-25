import pika
import funcs
from time import sleep

connection_params = funcs.connection_params


def callback(ch, method, properties, body):
    print(f"ВСЯКИЕ НЕНУЖНЫЕ ХУЕПОРАММЕТРЫ:\n{ch}\n{method}\n{properties}\n")
    print(f"Тело: {body.decode()}\n\n")
    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )  # Сообщения обработаны, если ошибок нет. После чего они удалятся из рэбита
    sleep(2)


def consume_message(channel, queue):
    channel.basic_qos(prefetch_count=1)
    '''
    Ограничить возможное количество неопознанных сообщений в "запасе"
    Данная настройка позволяет не отдавать консьюмеру все сообщения сразу.
    Благодаря этому, при двух одновременно запущенных консьюмерах, сообщения
    будут разделяться в порядке свободного консьюмера (свободен - держи), а не
    в разделении пополам.
    
    Ну или ещё раз - брокер отправляет сообщение только тогда, когда консьюмер
    подтвердит, что получил и обработал сообщение (ack)
    
    Теперь даже если запустить один консьюмер после того, как первый уже начал всё
    обрабатывать, то второй захапает пару сообщений, ибо сообщения первому передаются 
    по одному
    '''

    channel.basic_consume(
        queue=queue,
        on_message_callback=callback,
        #auto_ack=True,
    )
    print("Жду сообщения!")
    channel.start_consuming()


def main():
    with pika.BlockingConnection(connection_params) as conn:
        with conn.channel() as channel:
            consume_message(channel=channel, queue="hellos")




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt happened\n")