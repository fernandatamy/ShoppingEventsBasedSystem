from utils import send_to_queue, generate_order_message

def service_ecommerce(index):    
    try:
        key_value, message = generate_order_message(index)
        send_to_queue("kafka-purchase", key_value, message)
        send_to_queue("kafka-log", key_value, message)
            
    except Exception as ex:
        print("Houve um erro. "+str(ex))
        send_to_queue('dlq-topic', 0, str(ex))

for index in range(1000):
    service_ecommerce(index)

