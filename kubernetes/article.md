---
title: Kubernetes
created: 2018-06-07
taxonomy:
  category: [DevOps]
  status: in progress
---

## Context

## Learned in this study

## Things to explore

# Overview

# Notes
* Volume: Storage space
* Containerized app: Application living inside of a container/pod
* Pod: Abstraction that represents a group of one or more application containers and some shared resources for those containers
* Node: Worker machine
* Service: Abstraction which defines a logical set of pods and a policy by which to access them

# Cheat sheet
## List all containers (only IDs)
docker ps -aq

## Stop all running containers
docker stop $(docker ps -aq)

## Remove all containers
docker rm $(docker ps -aq)

## Remove all images
docker rmi $(docker images -q)

# See also

# References
* http://blog.baudson.de/blog/stop-and-remove-all-docker-containers-and-images
