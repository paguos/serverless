# OpenFaaS

![OpenFaaS](https://github.com/paguos/serverless/blob/master/runtimes/openfaas/openfaas_logo.png)
An serverless application runtime based on docker.

## Prerequisites

* [Docker 17.05](https://www.docker.com/) or higher
* [Homebrew](https://brew.sh/)

## Install OpenFaaS

**Note:** This instructions are for the deployment using Docker Swarm. 

Get the lastest version of the repository:
```sh
git clone https://github.com/openfaas/faas
```
Initialize the Swarm moed on your Docker daemon:
```sh
docker swarm init
```
Intall the CLI with `brew`:
```sh
brew install faas-cli
```

## Deployment

In order to deploy OpenFaaS run the following commnads:
```sh
cd /your/path/to/faas
./deploy_stack.sh
```
Test the deployment visiting the WebUI in the following URL: http://localhost:8080.

## Demo Function

Create a new python function using the CLI:
```ssh
faas-cli new --lang python hello-python
```

It creates the following files:
```
hello-python/handler.py  
hello-python/requirements.txt  
hello-python.yml
```
Edit the `handler.py` with the following content:
```python
def handle(req):  
    print("Hello! You said: " + req)
```

Build the funciton with the following commnad:
```ssh
faas-cli build -f ./hello-python.yml
```
 Test the function usig with a HTTP-Post method:
 ```ssh
 curl localhost:8080/function/hello-python -d "My first serverless function using OpenFaaS!"
 ```



