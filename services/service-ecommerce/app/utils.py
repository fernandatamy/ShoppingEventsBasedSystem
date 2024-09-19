import datetime
from kafka import KafkaConsumer
from kafka import KafkaProducer
import random

# adress = 'kafka:9093'

adress = 'localhost:9092'

def generate_order_message(index):
    the_dt = str(datetime.datetime.now())
    key_number = random.getrandbits(24)
    message = "Pedido #"+str(index)+": "+str(key_number)+" Criado em: "+str(the_dt)
    return key_number,message

def send_to_queue(topic, key, message):
    producer = KafkaProducer(bootstrap_servers=[adress])
    producer.send(topic=topic, key=str(key).encode(encoding='utf8'), value=message.encode(encoding='utf8'))
    producer.flush()
    print(topic, key, message)
    
def send_to_dlq(msg, error):
    send_to_queue('dlq-topic', msg.key, str(error))
    
def evaluate_payment_message(msg):
    key = msg.key.decode()
            
    if (int(key)%23 == 0): #Simulacao de erro 
        raise ValueError(f"Erro no pagamento")
    return key

def evaluate_packaging_message(msg):
    key = msg.key.decode()
            
    if (int(key)%31 == 0): #Simulacao de erro 
        raise ValueError(f"Erro no processamento")
    return key

def evaluate_shipping_message(msg):
    key = msg.key.decode()
            
    if (int(key)%47 == 0): #Simulacao de erro 
        raise ValueError(f"Erro na expedição")
    return key

def create_consumer(topicName, groupName):
    consumer = KafkaConsumer(topicName,  
    bootstrap_servers=[adress],  
    auto_offset_reset='earliest',  
    enable_auto_commit=True,  
    group_id=groupName, 
    max_poll_records=1)
    
    return consumer

def generate_appended_message(message,attachment):
    new_message = message+attachment+str(datetime.datetime.now())    
    return new_message