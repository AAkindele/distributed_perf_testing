from locust import HttpUser, TaskSet, task, between, events
from elasticsearch_store import ElasticsearchStore

class UserTaskSet(TaskSet):
  @task(10)
  def index_page(self):
    self.client.get("/")

  @task(1)
  def test_404_error(self):
    self.client.get("/does_not_exist")

class LocustUser(HttpUser):
  wait_time = between(1, 10)
  tasks = [UserTaskSet]

  def __init__(self, environment):
    super(LocustUser, self).__init__(environment)
    self.store = ElasticsearchStore("performance_data")

    def request_success_handler(request_type, name, response_time, response_length, *args, **kwargs):
      self.store.save_data(request_type, name, response_time, response_length, None, *args, **kwargs)

    def request_failure_handler(request_type, name, response_time, response_length, exception, *args, **kwargs):
      self.store.save_data(request_type, name, response_time, response_length, exception, *args, **kwargs)

    self.environment.events.request_success.add_listener(request_success_handler)
    self.environment.events.request_failure.add_listener(request_failure_handler)
