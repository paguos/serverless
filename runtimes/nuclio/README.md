# Nuclio
![Nuclio](https://github.com/paguos/serverless/blob/master/runtimes/nuclio/nuclio.png)
Serverless Application Runtime for Real-Time Events and Data Processing.

## Prerequisites

* [Docker](https://www.docker.com/) 17.05 or later installed and running
* Go Library

## Install Nuclio
Run the following docker command on the terminal:
```sh
docker run -p 8070:8070 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp nuclio/playground:stable-amd64
```

Then open the following website on your browser: [http://localhost:8070](http://localhost:8070)

## Install the CLI
Run the following commands:
```sh
export GOPATH=~/nuclio && mkdir -p $GOPATH
go get -u github.com/nuclio/nuclio/cmd/nuctl
PATH=$PATH:$GOPATH/bin
```

Test the installation with by deploying a demo funcion and calling it:
```sh
nuctl deploy -p https://raw.githubusercontent.com/nuclio/nuclio/master/hack/examples/golang/helloworld/helloworld.go --registry 0.0.0.0:5000 helloworld --run-registry localhost:5000
nuctl invoke helloworld
```