from datetime import datetime, timezone
from elasticsearch import Elasticsearch
import os

class ElasticsearchStore:
  def __init__(self, index):
    self.client = Elasticsearch([os.environ.get("ELASTICSEARCH_HOST")])
    self.index = index

  def save_data(self, request_type, name, response_time, response_length, exception, *args, **kwargs):
    exception_message = ""
    exception_type = ""
    is_success = True
    timestamp = datetime.now(timezone.utc).isoformat()

    if (exception != None):
      exception_message = str(exception)
      exception_type = exception.__class__.__name__
      is_success = False

    document = {
      "request_type": request_type,
      "name": name,
      "response_time": response_time,
      "response_length": response_length,
      "exception_message": exception_message,
      "exception_type": exception_type,
      "is_success": is_success,
      "timestamp": timestamp,
      "host": os.environ.get("HOSTNAME")
    }

    self.client.index(index=self.index, body=document)
