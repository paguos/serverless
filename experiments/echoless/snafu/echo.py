def lambda_handler(event, context):
	return "ECHO: " + event['message']
	