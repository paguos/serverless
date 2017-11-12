# Kubeless
![Kubeless](https://github.com/paguos/serverless/blob/master/runtimes/kubeless/kubeless_logo.png)
Kubeless is a Kubernetes native serverless application runtime.

## Prerequisites
* Kubernetes client: [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* Kubernetes commnad-line tool: [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* Homebrew

## Intall Kubeless
Install the `kubeless` CLI using `brew`:
```sh
brew install kubeless/tap/kubeless
```
Create a `kubeless` namespace with the following commands:
```sh
export RELEASE=v0.2.3
kubectl create ns kubeless
```
Use one of the YAML manifests found in the release page to deploy kubeless:
```sh
kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless-$RELEASE.yaml
```

## Demo Function
Create a `demo.py` file with the following function:
```python
def foobar(context):
   print context.json
   return context.json
```
Deploy it into `kubeless` with the following commnad:
```ssh
kubeless function deploy get-python --runtime python2.7 --from-file demo.py --handler demo.foobar --trigger-http
```
Test your function with the following command:
```sh
kubeless function call get-python --data '{"echo": "echo echo"}'
```
You should become the following response: `{"echo": "echo echo"}`

Or using a `kubectl proxy`:
```sh
kubectl proxy -p 8080 &
curl -L --data '{"echo": "echo echo"}' localhost:8080/api/v1/proxy/namespaces/default/services/get-python:function-port/ --header "Content-Type:application/json"
```

## Other Commands
Get a list of the depoyed functions:
```sh
# Using kubectl
kubectl get functions
# Using the kubeless cli
kubeless function ls
```


