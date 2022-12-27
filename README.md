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
