import confluent_kafka
import json
import time
import logging


logger = logging.getLogger(__name__)


class KafkaProducer(confluent_kafka.Producer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.info('Kafka Producer has been initiated...')

    def receipt(self, err, msg):
        if err is not None:
            logger.warn(f'Kafka Producer Error: {err}')
        else:
            message = f'Produced message on topic {msg.topic()} with value of {msg.value()}\n'
            logger.info(message)

    def send_message(self, topic, message):
        data = {
            'message': message,
            'timestamp': time.time()
        }
        kafka_message = json.dumps(data)
        logger.info('Sending Kafka message: {}'.format(kafka_message))
        self.poll(1)
        self.produce(topic, kafka_message, callback=self.receipt)
        self.flush()
