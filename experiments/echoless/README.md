# Echoless
Test some of the analysed serverless application runtimes with a comon _echo_ function:

* [Azure Functions Core Tool](https://github.com/paguos/serverless/tree/master/runtimes/azure-functions)
* [Fn Project](https://github.com/paguos/serverless/tree/master/runtimes/fn-project)
* [Kubeless](https://github.com/paguos/serverless/tree/master/runtimes/kubeless)
* [Snafu](https://github.com/paguos/serverless/tree/master/runtimes/snafu)

**Note:** The designed funcitons for each runtime are in a individual folder with the runtime's name. 

## Usage

In order to run the `echoless` execute the following command in this folder:

```sh
python echoless.py -r <runtime_name> -m <message_to_be_repeated> -c <number_of_excutions>
```

The only optional argument is `-c`. With it's omision the default value is one.

## TODO

* Add support to the other runtimes of this analysis
* Add multithread support
