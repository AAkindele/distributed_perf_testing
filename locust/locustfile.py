from locust import HttpUser, TaskSet, task, between, events

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

@events.request_success.add_listener
def request_success_handler(request_type, name, response_time, response_length, **args):
  print("request_success_handler")
  print(request_type) # "GET"
  print(name) # "/"
  print(response_time) # "3.9076805114746094" milliseconds
  print(response_length) # "68" bytes
  print(args) # "{}"

@events.request_failure.add_listener
def request_failure_handler(request_type, name, response_time, response_length, exception, **args):
  print("request_failure_handler")
  print(request_type) # "GET"
  print(name) # "/does_not_exist"
  print(response_time) # "1.703500747680664" milliseconds
  print(response_length) # "154" bytes
  print(exception) # Exception instance : 404 Client Error: Not Found for url: http://web-server:8080/does_not_exist
  print(args) # "{}"
