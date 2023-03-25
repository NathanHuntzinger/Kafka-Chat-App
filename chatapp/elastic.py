import elasticsearch

from datatypes import logging


logger = logging.getLogger(__name__)


class Elastic(elasticsearch.Elasticsearch):
    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 9200)
        config = {
            'host': self.host,
            'port': self.port
        }

        super().__init__([config])

        self.es = None
        self.connect()
        self.INDEX_NAME = "new-relic-log"

    def connect(self):
        self.es = elasticsearch.Elasticsearch([{'host': self.host, 'port': self.port}])
        if self.es.ping():
            print("ES connected successfully")
        else:
            print("Not connected")

    def create_index(self):
        if self.es.indices.exists(self.INDEX_NAME):
            print("deleting '%s' index..." % (self.INDEX_NAME))
            res = self.es.indices.delete(index=self.INDEX_NAME)
            print(" response: '%s'" % (res))
            request_body = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                }
            }
            print("creating '%s' index..." % (self.INDEX_NAME))
            res = self.es.indices.create(index=self.INDEX_NAME, body=request_body, ignore=400)
            print(" response: '%s'" % (res))

    def push_to_index(self, message):
        try:
            response = self.es.index(
                index=self.INDEX_NAME,
                doc_type="log",
                body=message
            )
            print("Write response is :: {}\n\n".format(response))
        except Exception as e:
            print("Exception is :: {}".format(str(e)))
