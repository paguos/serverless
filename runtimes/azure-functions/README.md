# Azure Functions Core Tool
![Azure Functions](https://github.com/paguos/serverless/blob/master/runtimes/azure-functions/azure-functions_logo.png)

This is a small version of the Azure Functions with the goal to test functions locally before its deployment.

## Prerequisites

* [Node.js](https://nodejs.org/en/) 8.5 or higher
* [.NET Core Tools](https://www.microsoft.com/net/learn/get-started/macos)

## Install Azure Functions Core Tool

Install the package using npm:
```sh
sudo npm i -g azure-functions-core-tools@core --unsafe-perm
```

## Demo Function

Create a new project with the following commands:

```sh
func init .
func new --language JavaScript --template HttpTrigger --name HttpTriggerJavaScript
```

Depploy your function with the following commnad:
```sh
func host start
```
Visit the following website: http://localhost:7071/api/HttpTriggerJavaScript?name=Azure%20Rocks

Everything is working fine if you become the following output:
```sh
Hello Azure Rocks
```
