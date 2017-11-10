def hello():
	return "Hello World from Snafu!"

def lambda_handler(event, context):
	return hello()
