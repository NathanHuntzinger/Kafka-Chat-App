import elasticsearch

from datatypes import logging


logger = logging.getLogger(__name__)


class Elastic(elasticsearch.Elasticsearch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.check_connection()
        self.index_name = "new-chat-message"

    def check_connection(self):
        """Check connection to ElasticSearch"""
        connected = self.ping()

        if connected:
            logger.info("Successfully connected to ElasticSearch")
            print("Successfully connected to ElasticSearch")
        else:
            logger.warn("Failed to connect to ElasticSearch")

        return connected

    def create_index(self):
        if self.indices.exists(self.index_name):
            logger.info(f"deleting '{self.index_name}' index...")
            res = self.indices.delete(index=self.index_name)
            logger.info(f" response: '{res}'")
            request_body = {
                "settings": {
                    "number_of_shards": 1,
                    "number_of_replicas": 0
                }
            }
            logger.info(f"creating '{self.index_name}' index...")
            res = self.indices.create(index=self.index_name, body=request_body, ignore=400)
            logger.info(f" response: '{res}'")

    def push_to_index(self, message):
        try:
            print(f"Pushing message to ElasticSearch: {message}\n")
            response = self.index(
                index=self.index_name,
                body=message
            )
            logger.warn(f"ElasticSearch response: {response}\n\n")
        except Exception as e:
            logger.warn(f"ElasticSearch Error: {e}")
