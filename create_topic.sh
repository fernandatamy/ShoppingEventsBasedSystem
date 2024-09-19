#/bin/bash

/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_DLQ --bootstrap-server localhost:9092 --partitions 1
echo "topic $TOPIC_DLQ was create"
/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_LOG --bootstrap-server localhost:9092 --partitions 3
echo "topic $TOPIC_LOG was create"
/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_ECOMMERCE --bootstrap-server localhost:9092 --partitions 3
echo "topic $TOPIC_ECOMMERCE was create"
/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_PAYMENT --bootstrap-server localhost:9092 --partitions 3
echo "topic $TOPIC_PAYMENT was create"
/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_DISPATCH --bootstrap-server localhost:9092 --partitions 3
echo "topic $TOPIC_DISPATCH was create"
/opt/kafka/bin/kafka-topics.sh --create --topic $TOPIC_SHIPPING --bootstrap-server localhost:9092 --partitions 3
echo "topic $TOPIC_SHIPPING was create"