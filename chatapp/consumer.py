from confluent_kafka import Consumer


def main():
    consumer_config = {
        'bootstrap.servers':'localhost:9092',
        'group.id':'python-consumer',
        'auto.offset.reset':'earliest'
    }

    with Consumer(consumer_config) as c:
        print('Kafka Consumer has been initiated...')

        print('Available topics to consume: ', c.list_topics().topics)
        c.subscribe(['user-tracker'])

        while True:
            msg = c.poll(1.0)  # timeout
            if msg is None:
                continue
            if msg.error():
                print('Error: {}'.format(msg.error()))
                continue
            data = msg.value().decode('utf-8')
            print(data)


if __name__ == '__main__':
    main()
