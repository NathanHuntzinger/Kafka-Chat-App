# -*- coding: utf-8 -*-
import confluent_kafka
import elasticsearch

from datatypes import logging


logger = logging.getLogger(__name__)


class KafkaConsumer(confluent_kafka.Consumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.subscribe(kwargs['topics'])

    def read_messages(self, timeout=0.1):
        try:
            msg = self.poll(timeout)  # timeout
            if msg is None:
                return
            if msg.error():
                print('Error: {}'.format(msg.error()))
                return
            data = msg.value().decode('utf-8')
            logger.info(data)
            return data
        except Exception as e:
            logger.error(e)
            return



def main():
    es = elasticsearch.Elasticsearch(['localhost:9200'])
    consumer_config = {
        'bootstrap.servers':'localhost:9092',
        'group.id':'python-consumer',
        'auto.offset.reset':'earliest'
    }

    with KafkaConsumer(consumer_config) as kafka_consumer:
        while True:
            message = kafka_consumer.read_messages()
            if message:
                print(message)


if __name__ == '__main__':
    main()
