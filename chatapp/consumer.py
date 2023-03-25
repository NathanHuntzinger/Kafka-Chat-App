# -*- coding: utf-8 -*-
import confluent_kafka
import elasticsearch

from datatypes import logging

import elastic


logger = logging.getLogger(__name__)


class KafkaConsumer(confluent_kafka.Consumer):
    def __init__(self, *args, **kwargs):
        topics = kwargs.pop('topics', [])
        super().__init__(*args, **kwargs)

        self.subscribe(topics)

    def read_messages(self, timeout=0.1):
        try:
            msg = self.poll(timeout)  # timeout
            if msg is None:
                return
            if msg.error():
                print(f'Kafka Consumer Error: {msg.error()}')
                return
            data = msg.value().decode('utf-8')
            logger.info(data)
            return data
        except Exception as e:
            logger.error(f'Kafka Consumer Error: {e}')
            return



def main():
    elastic_config = {
        'host': 'localhost',
        'port': 9200,
        'scheme': 'http'
    }
    es = elastic.Elastic(elastic_config)

    consumer_config = {
        'bootstrap.servers':'localhost:29092',
        'group.id':'python-consumer',
        'auto.offset.reset':'earliest'
    }

    topics = ['chat-message']
    kafka_consumer = KafkaConsumer(consumer_config, topics=topics)
    while True:
        message = kafka_consumer.read_messages()
        if message:
            print(f'Received message: {message}')
            es.push_to_index(message)
    kafka_consumer.close()


if __name__ == '__main__':
    main()
