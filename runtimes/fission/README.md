# Fission
![Fission](https://github.com/paguos/serverless/blob/master/runtimes/fission/fission_logo.png)
Fission is a framework for serverless functions on Kubernetes.

## Prerequisites
* Kubernetes client: [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* Kubernetes commnad-line tool: [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Homebrew](https://brew.sh/)

## Intall Fission
Install Helm (an installer for Kubernetes) with the `brew`:
```sh
brew install helm
```
Start the `minikube`using k8s version 1.6.4:
```sh
minikube start --kubernetes-version v1.6.4
```
Intall the Helm server on your Kubernetes cluster with the following commnads:
```sh
kubectl -n kube-system create sa tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller
```
Install Fission on your Minikube:
```sh
helm install --namespace fission --set serviceType=NodePort https://github.com/fission/fission/releases/download/0.3.0/fission-all-0.3.0.tgz
```
Get Fission's the CLI:
```sh
curl -Lo fission https://github.com/fission/fission/releases/download/0.3.0/fission-cli-osx && chmod +x fission && sudo mv fission /usr/local/bin/
```
Set the environment variables with the following commnads:
```sh
export FISSION_URL=http://$(minikube ip):31313
export FISSION_ROUTER=$(minikube ip):31314
```

## Demo function

Create a Node.js environment:
```sh
fission env create --name nodejs --image fission/node-env:0.3.0

curl -LO https://raw.githubusercontent.com/fission/fission/master/examples/nodejs/hello.js

fission function create --name hello --env nodejs --code hello.js

fission route create --method GET --url /hello --function hello

curl http://$FISSION_ROUTER/hello
Hello, world!

```
Create a file called `hello.js` with the following content:
```javascript
module.exports = async function(context) {
    return {
        status: 200,
        body: "Hello, world!\n"
    };
}
```
Deploy the function and create route with the following commnads:
```sh
fission function create --name hello --env nodejs --code hello.js
fission route create --method GET --url /hello --function hello
```
If everything is working properly you can invoke the function with `curl`:
```sh
curl http://$FISSION_ROUTER/hello
```
