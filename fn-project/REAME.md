# Fn Project

![Fn Project](http://fnproject.io/images/fn-300x125.png)

## Prequisites

* [Docker](https://www.docker.com/) 17.05 or later installed and running
* A Docker Hub account (Docker Hub)
* Log Docker into your Docker Hub account
* [Homebrew](https://brew.sh/)

## Install CLI

Install the CLI using Homebrew:
```sh
brew install fn
```
Save your Docker username in your `.bash_profile` file:
```sh
export FN_REGISTRY=<DOCKERHUB_USERNAME>
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
fn deploy --app myapp
```
* You can call your function deployed to the Fn server:
```sh
fn call myapp /hello
```



