import functools
import pika
import logging,json
from pika.exchange_type import ExchangeType


class AmqpConfig(object):

    EXCHANGE = 'radadspread_analytics'
    EXCHANGE_TYPE = ExchangeType.topic

    def __init__(self, amqp_url):
        self._url = amqp_url
        self._connection=False
        self._channel=False

    def connect(self):
        return pika.BlockingConnection(
            pika.URLParameters(self._url))

    def start(self)->pika.BlockingConnection.channel:
        self._connection=self.connect()
        self._channel=self._connection.channel()
        self._channel.exchange_declare(exchange=self.EXCHANGE,
                                       exchange_type=self.EXCHANGE_TYPE)
        return self._channel


 