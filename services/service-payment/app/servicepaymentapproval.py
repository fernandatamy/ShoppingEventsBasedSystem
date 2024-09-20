import time

from utils import create_consumer, evaluate_payment_message, generate_appended_message,send_to_queue


def service_payment_approval():

    consumer = create_consumer('kafka-purchase','operation')
    consumer.poll()

    for msg in consumer:
        try:
            key = evaluate_payment_message(msg)
            new_message = generate_appended_message(msg.value.decode(), "Pagamento Aprovado em: ")
            send_to_queue("kafka-log", key, new_message)
            send_to_queue("kafka-approval", key, new_message)
            time.sleep(1.5)
        except Exception as ex:
            print("Houve um erro. "+str(ex))
            send_to_queue('dlq-topic', msg.key, str(ex))
            
service_payment_approval()