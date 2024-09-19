import time

from utils import create_consumer, evaluate_packaging_message, generate_appended_message,send_to_queue


def service_packaging():

    consumer = create_consumer('kafka-approval','operation')
    consumer.poll()

    for msg in consumer:
        try:
            key = evaluate_packaging_message(msg)
            new_message = generate_appended_message(msg.value.decode(), "Produção finalizada em: ")
            send_to_queue("kafka-log", key, new_message)
            send_to_queue("kafka-dispatch", key, new_message)
            time.sleep(1.5)
        except Exception as ex:
            print("Houve um erro. "+str(ex))
            send_to_queue('dlq-topic', msg.key, str(ex))

service_packaging()