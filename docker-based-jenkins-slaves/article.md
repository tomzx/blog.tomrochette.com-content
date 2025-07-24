---
title: Docker-based jenkins slaves
created: 2015-11-07
taxonomy:
  type: post
  tag: [devops, docker, jenkins]
---

# Overview
In this article, we'll go over how to setup Jenkins on an Ubuntu machine to run PHP 7.1 jobs. The steps should easily be adapted for any other OS and target environment.

# Install Jenkins
* https://jenkins.io/

## Install Jenkins plugins
* Docker Slaves Plugin

# Install Docker on the slave (or host)
* https://www.docker.com/

# Create a Docker image
* In a Dockerfile

<pre><code class="language-bash line-numbers">
FROM ubuntu:xenial

COPY sources.list /etc/apt/sources.list
RUN useradd -m --uid=1001 jenkins
COPY known_hosts /home/jenkins/.ssh/known_hosts
RUN chown jenkins:jenkins -R /home/jenkins/.ssh

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y git vim curl wget build-essential python-software-properties software-properties-common unzip

RUN add-apt-repository -y ppa:ondrej/php
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y --force-yes php7.1 php7.1-xml php7.1-mbstring php7.1-zip php7.1-pdo-mysql php7.1-pdo-sqlite

RUN apt-get -y autoremove && apt-get clean && apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
</code></pre>

* docker build -t your/image:1.0.0 -t your/image:latest .

# Configure your Jenkins jobs
## Specify the Docker image to use
* your/image (will use your/image:latest)

## Use SSH keys within Docker
This is particularly useful if you need to pull git repositories from a private repository.

### Notes
As of December 2016, if you want to be able to use the SSH key in a docker container, you have to first start the ssh agent on the node used that will run the docker container and when you run the docker image, pass in the SSH_AUTH_SOCK as a volume so that it is shared with its host.

<pre><code class="language-groovy line-numbers">
sshagent(['IDENTIFIER']) {
	docker.image('your/jenkins-slave-image').inside('--volume $SSH_AUTH_SOCK:$SSH_AUTH_SOCK') {
		// Here your SSH_AUTH_SOCK is shared with the host machine, which may be a jenkins slave
		// All commands that would use SSH for authentication (such as git or composer when installing from private repositories) should work
	}
}
</code></pre>

# Example Pipeline

<pre><code class="language-groovy line-numbers">
node('docker') {
	catchError {
		timestamps {
			wrap([$class: 'AnsiColorBuildWrapper']) {
				sshagent(['private-git']) {
					docker.image('tomzx/jenkins-slave').inside('--volume $SSH_AUTH_SOCK:$SSH_AUTH_SOCK') {
						stage 'Checkout'
							checkout scm

						stage 'Setup dependencies'
							sh 'wget -nc https://getcomposer.org/composer.phar'
							sh 'php composer.phar install'

						stage 'Test'
							sh 'vendor/bin/phpunit'
					}
				}
			}
		}
	}
}
</code></pre>

# References
* https://zapier.com/engineering/continuous-integration-jenkins-docker-github/
* https://engineering.riotgames.com/news/building-jenkins-inside-ephemeral-docker-container
