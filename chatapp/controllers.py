# -*- coding: utf-8 -*-
import json

from endpoints import Controller
from datatypes import logging

import producer


logger = logging.getLogger(__name__)

kafka_producer = producer.KafkaProducer({'bootstrap.servers':'localhost:9092'})
logger.info('Kafka Producer has been initiated...')

# from endpoints.decorators.auth import AuthDecorator


# class auth(AuthDecorator):
#     def target(self, *args, **kwargs):
#         if kwargs["key"] != 'foo':
#             raise ValueError("invalid access token")


class Default(Controller):
    # @auth()
    def GET(self):
        return "Default GET endpoint hit"

    # @auth()
    def POST(self, **kwargs):
        return 'hello {}'.format(kwargs['name'])


class Message(Controller):
    # @auth()
    def GET(self, **kwargs):
        return "Message GET endpoint hit"

    # @auth()
    def POST(self, **kwargs):
        kafka_producer.send_message('test', kwargs['body'])
        logger.info('Sent Kafka message: {}'.format(kwargs['body']))
        return 'Sent Kafka message: {}'.format(kwargs['body'])
