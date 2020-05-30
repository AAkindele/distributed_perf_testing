TODO:
- send data directly from locust to elasticsearch.
  - not worrying about impact on the locust workers at this time
  - need to also include information about the host where the data is coming from
- k8s cluster and resource definitions

Goal: Distributed performance testing with Locust, Kubernetes, Elasticsearch.

Testing locally with Docker Compose
```
# build the testing server. simple nginx http server that return "Hello, World!"
docker build ./nginx -t test-server

# build the test locust container. it has a single test that hits the test-server
docker build ./locust -t my-locust

# start the components
# elasticsearch will keep its data in the "elasticsearch/data" directory
docker-compose up
```

- The test http server can be reached at `http://localhost:8080/`.
- The Locust web ui can be reached at `http://localhost:3000/`.
- Elasticsearch is avaiable at `http://localhost:9200/`.
- Kibana is available at `http://localhost:5601/`.

Create the index where the performance data will be stored. One way to do this is to use the Kibana console.
Whichever way you choose, send a PUT request to the desired index. In this example that will be `/performance_data`.
The example below is a mapping definition that will be sent in the performance_data index.
```json
{
  "mappings": {
    "properties": {
      "request_type": { "type": "keyword" },
      "name": {
        "type": "text",
        "fields": {
          "raw": { "type": "keyword" }
        }
      },
      "response_time": { "type": "double" },
      "response_length": { "type": "integer" },
      "args": {
        "type": "text",
        "fields": {
          "raw": { "type": "keyword" }
        }
      },
      "exception": {
        "type": "text",
        "fields": {
          "raw": { "type": "keyword" }
        }
      },
      "is_success": { "type": "boolean" },
      "timestamp": { "type": "date" }
    }
  }
}
```
