TODO:
- send data directly from locust to elasticsearch.
  - come up with mapping definition first
  - not worrying about impact on the locust workers at this time
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
