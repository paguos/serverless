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
Intall the Helm server on your Kubernetes cluster with the following commnads:
```sh
kubectl -n kube-system create sa tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller
```
Install Fission on your Minikube:
```sh
helm install --namespace fission --set serviceType=NodePort https://github.com/fission/fission/releases/download/v0.2.1/fission-all-v0.2.1.tgz
```
Get Fission's the CLI:
```sh
curl -Lo fission https://github.com/fission/fission/releases/download/v0.2.1/fission-cli-osx && chmod +x fission && sudo mv fission /usr/local/bin/
```
Set the environment variables with the following commnads:
```sh
export FISSION_URL=http://$(minikube ip):31313
export FISSION_ROUTER=$(minikube ip):31314
```
