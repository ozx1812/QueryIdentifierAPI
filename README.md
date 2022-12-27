# QueryIdentifierAPI

An API that identifies the type of input text is a sentence, paragraph, question, or URL

## Problem statement

Design a server that accepts requests from the user, processes the inputs from the requests, and returns the result to the user.

The server should handle requests from different users parallelly

The user request will contain English text

The server should decide whether the input text is a sentence, paragraph, question, or URL

## Problem solving

- here the input text identification task is simple and compute intensive, can be solved using regex match
- api can be developed using various frameworks.
- fastapi - high performance api, built around starlette and pydantic

## Design

- to support huge number of concurrent http requests,
  - an api should be deployed on machine with many resources(more cpu core) or
  - multiple replicas of an api should be running behind a good http load-balancer
- the first option is not a viable.
- so choosing 2nd option, with nginx as a load balancer and running multiple replicas of dockerized api behind it.

![Alt text](design.png?raw=true 'System Design')

## How to Run

- prerequisites : A system with docker and docker-compose
- steps
  - unzip the code
  - run `docker-compose build` - to build the images
  - run `docker-compose up` - to start the services
  - use below curl POST request to test api

### CURL post request examples

---

#### **query**

```
curl -X POST \
  'http://172.17.0.1:9998/query' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{"text": "Am i question?"}'
```

#### **response**

```
{"query_type":"question"}
```

---

#### **query**

```
curl -X POST \
  'http://172.17.0.1:9998/query' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{"text": "I am sentence."}'
```

#### **response**

```
{"query_type":"sentence"}
```

---

#### **query**

```
curl -X POST \
  'http://172.17.0.1:9998/query' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{"text": "I am sentence1. I am part of paragraph."}'
```

#### **response**

```
{"query_type":"paragraph"}
```

---

#### **query**

```
curl -X POST \
  'http://172.17.0.1:9998/query' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{"text": "https://github.com/"}'
```

#### **response**

```
{"query_type":"url"}
```

## Scaling

- To add more replicas
  - add below block in **docker-compose.yml**
    ```
    apireplicanew:
      build: ./src
      ports:
        - '<newport>:80'
    ```
  - add below block in **nginx.conf** in **nginx/**
    ```
    upstream app {
        .
        .
        server 172.17.0.1:<newport>;
    }
    ```
  - build the images again using `docker-compose build`
  - start the services again `docker-compose up`
