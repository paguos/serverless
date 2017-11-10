# Snafu
Snake Functions or Snafu is a small and simple serverless application runtime. It is designed to run on-premise and allow developers to test function before its deployment in a bigger platform.

## Prerequisites

* [Python 3](https://www.python.org/downloads/)
* `flask`and `pyesprima3` modules
* Interpreters for supported languages (i.e. Node.js, Java)

To install the additional python modules run the following commands:
```sh
# Install flask
pip3 install flask
# Install pyesprima3
pip3 install pyesprima3
```
## Intall Snafu
In order to install snafu clone the Git reposirtory:
```sh
git clone --depth=1 https://github.com/serviceprototypinglab/snafu.git
```
Add the following lines to your `.bash_profile` file:
```sh
alias snafu="/your/path/to/snafu/snafu"
alias snafu-control="/your/path/to/snafu/snafu-control"
```

## Demo Function

Create a new file called `demo.py` and writte the following function:
```python
def hello():
	return "Hello World from Snafu!"
```
### Execute a function
In the the same directory execute the following command and type the name of the function (`demo.hello`):
```sh
snafu demo.py
```
### Host a function
Snafu only host function with a lambda function. Open your `demo.py` file and add the following function:
```python
def lambda_handler(event, context):
	return hello()
```
To invoke the function use a HTTP-Post method with empty arguments:
```sh
curl -H "Content-Type: application/json" -X POST -d '{"event": ""}' http://localhost:10000/2015-03-31/functions/demo.lambda_handler/invocations
```
