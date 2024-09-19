import time
import datetime

from utils import create_consumer

def service_dlq():

    consumer = create_consumer('dlq-topic','operation')
    consumer.poll()

    for msg in consumer:

        key = msg.key.decode()
        value = msg.value.decode()

        print(key+' '+value+' Processado em: '+ str(datetime.datetime.now()))
        
        time.sleep(2.5)

service_dlq()