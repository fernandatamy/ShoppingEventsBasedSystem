import time

from utils import create_consumer, evaluate_shipping_message, generate_appended_message,send_to_queue


def service_shipping():

    consumer = create_consumer('kafka-dispatch','operation')
    consumer.poll()

    for msg in consumer:
        try:
            key = evaluate_shipping_message(msg)
            new_message = generate_appended_message(msg.value.decode(), "Pedido enviado em: ")
            send_to_queue("kafka-log", key, new_message)
            send_to_queue("kafka-shipping", key, new_message)
            time.sleep(2)
        except Exception as ex:
            print("Houve um erro. "+str(ex))
            send_to_queue('dlq-topic', msg.key, str(ex))
            
service_shipping()