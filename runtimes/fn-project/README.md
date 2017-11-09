# Fn Project

![Fn Project](https://raw.githubusercontent.com/paguos/serverless/master/runtimes/fn-project/fn_logo.png)

## Prerequisites

* [Docker](https://www.docker.com/) 17.05 or later installed and running
* A Docker Hub account (Docker Hub)
* Log Docker into your Docker Hub account
* [Homebrew](https://brew.sh/)
* Go Library

## Install CLI

Install the CLI using Homebrew:
```sh
brew install fn
```
Save your Docker username in your `.bash_profile` file:
```sh
export FN_REGISTRY=<DOCKERHUB_USERNAME>
```

## Run Fn Server
Execute the following commnad:
```sh
fn start
```

## Commands

The following commands should be executed in the same directory of function desired to deploy.

* Initialize a function:
```sh
fn init
```
* Test your function:
```sh
fn run
```
* Deploy your functions to the Fn server (default localhost:8080):
```sh
fn deploy --app app_name
```
* You can call your function deployed to the Fn server:
```sh
fn call app_name /function_name
```



