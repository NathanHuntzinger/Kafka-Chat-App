# -*- coding: utf-8 -*-
import json

from endpoints import Controller
from datatypes import logging

import producer


logger = logging.getLogger(__name__)


kafka_producer = producer.KafkaProducer({'bootstrap.servers':'localhost:29092'})
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
        # TODO - get messages from elasticsearch
        return "Message GET endpoint hit"

    # @auth()
    def POST(self, **kwargs):
        kafka_producer.send_message('chat-message', kwargs['body'])
        logger.info(f'Sent Kafka message: {kwargs["body"]}')
        return f'Sent Kafka message: {kwargs["body"]}'
