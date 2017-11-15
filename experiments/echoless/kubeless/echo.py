def echo(request):
	return "ECHO: " + request.json["message"]