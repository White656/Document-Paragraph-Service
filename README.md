# Asynchronous Tasks with FastAPI and Celery

Example of how to handle background processes with FastAPI, Celery, and Docker.

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost](http://localhost:80) to view the app or to [http://localhost/api/openapi](http://localhost/api/openapi) to view api documentations

Trigger a new task:

```sh
$ curl http://localhost/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```

Check the status:

```sh
$ curl http://localhost/tasks/<TASK_ID>
```
