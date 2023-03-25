from confluent_kafka import Producer
import json
import time
import logging
import random

from testdata import TestData


logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


p = Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')


def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = f'Produced message on topic {msg.topic()} with value of {msg.value()}\n'
        logger.info(message)
        print(message)


def main():
    testdata = TestData()

    topic = 'user-tracker'

    for _ in range(100):
        data = {
           'user_id': testdata.get_hash(),
           'user_name':testdata.get_name(),
           'user_email': testdata.get_email(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
           'signup_at': str(testdata.get_past_datetime()),
        }
        m = json.dumps(data)
        p.poll(1)
        p.produce(topic, m, callback=receipt)
        p.flush()
        # time.sleep(random.random())


if __name__ == '__main__':
    main()
