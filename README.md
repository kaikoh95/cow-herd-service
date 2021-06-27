# Cow Herd Service
This is a REST API service written in Python Flask to manage Cows as part of the assessment for Halter, New Zealand.
The API methods are written in a self-documenting format such that Swagger docs are generated automatically via the related 
schemas and doc strings.

This uses PostgreSQL for persistence and Flask Caching (RedisCache) for caching results.

## Usage
Ensure that you have [Docker](https://www.docker.com/) installed in your host machine before trying to run the application.

```
$ git clone https://github.com/kaikoh95/cow-herd-service.git
$ cd cow-herd-service
$ docker-compose up
```
Now redirect to http://localhost:5000.

Once you have your local server running, 
you can view Swagger docs [here](http://localhost:5000/swagger-ui).
