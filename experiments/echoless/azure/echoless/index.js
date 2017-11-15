module.exports = function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    if (req.query.message || (req.body && req.body.message)) {
        context.res = {
            // status: 200, /* Defaults to 200 */
            body: "ECHO: " + req.body.message
        };
    }
    else {
        context.res = {
            status: 400,
            body: "Please pass a message on the query string or in the request body"
        };
    }
    context.done();
};