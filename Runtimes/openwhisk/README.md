# Apache OpenWhisk
![Apache OpenWhisk](https://cdn-images-1.medium.com/max/1200/1*4Q3kFLD0dZiwbLAKZJGy8Q.png)

## Prerequisites
* [Docker](https://www.docker.com/) 
* [Java 8](http://www.oracle.com/technetwork/java/javase/downloads/index.html) (_Further versions are not supported!_)
* [Homebrew](https://brew.sh/)

Install the following packages using Homebrew:

```sh
echo '
# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# install cask
brew tap caskroom/cask
# install java 8
brew cask install java
# install scala
brew install scala
# install pip
sudo easy_install pip
# install script prerequisites
sudo -H pip install docker==2.2.1 ansible==2.3.0.0 jinja2==2.9.6 couchdb==1.1 httplib2==0.9.2 requests==2.10.0' | bash
```

## Build

Clone the latest version of the OpenWhisk repository:
```sh
git clone --depth=1 https://github.com/apache/incubator-openwhisk.git openwhisk
```

Go to the the parent directory of the repository and use gradle to make a build of the runtime with the following commands:
```sh
cd /your/path/to/openwhisk
./gradlew distDocker
```

## Deployment 
In order to deploy OpenWhisk locally using Ansible, you first need to install Ansible on your development environment:
```sh
sudo apt-get install python-pip
sudo pip install ansible==2.3.0.0
sudo pip install jinja2==2.9.6
```
### Activate docker0 network
This is an optimal step. It creates an interface to interact with the OpenWhsik runtime:
```sh
sudo ifconfig lo0 alias 172.17.0.1/24
```
### Database Setup
OpenWhisk offers many different configurations for the database. For this experiment an Ephemeral CouchDB will be used. Go the `ansible` folder of the repository and execute the following commnad:
```sh
ansible-playbook setup.yml
```
### OpenWhisk Deployment
Execute the following commnads:
```sh
cd <openwhisk_home>
# Make a fresh build
./gradlew distDocker
cd ansible
# Deployment
ansible-playbook couchdb.yml
ansible-playbook initdb.yml
ansible-playbook wipe.yml
ansible-playbook apigateway.yml
ansible-playbook openwhisk.yml
ansible-playbook postdeploy.yml
```
You need to run initdb.yml on couchdb every time you do a fresh deploy CouchDB to initialize the subjects database.

### Cleaning an OpenWhisk Deployment
Execute the following commnad in the `ansible` directory:
```sh
ansible-playbook openwhisk.yml -e mode=clean
```
## Configure the CLI
The CLI is located in `openwhisk/bin`. Add the following line to your `.bash_proifle`:
```sh
alias wsk="/Users/pabloosinaga/Documents/openwhisk/bin/wsk"
```
Go to the `openwhisk` directory and run the following commands:
```sh
# Configure your API Host
./bin/wsk property set --apihost 172.17.0.1
# Configure your Credentials
./bin/wsk property set --auth `cat ansible/files/auth.guest`
```
You can find your **API Host** in the `whisk.properties`file and the **guest user credentials** in the `ansible/files/auth.guest`file.

## Test
In order to test the runtime and the CLI run the following commands to execute an demo function:
```sh
wsk -i action invoke /whisk.system/utils/echo -p message hello --result
```
Everithing is working fine if you become the following output:
```sh
{
    "message": "hello"
}
```
