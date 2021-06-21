# Cow Herd Service
This is a REST API service written in Python Flask to manage Cows as part of the assessment for Halter, New Zealand.

## Usage
Ensure that you have [Docker](https://www.docker.com/) installed in your host machine before trying to run the application.

```
$ git clone https://github.com/kaikoh95/cow-herd-service.git
$ cd cow-herd-service
$ docker-compose up
```

Now redirect to http://localhost:5000

Once you have your local server running, 
you can view Swagger docs at /spec with [Swagger](https://editor.swagger.io/)
by importing the [full URL](http://localhost:5000/spec) for the docs endpoint.