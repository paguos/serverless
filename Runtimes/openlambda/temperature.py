
def temperature(): 
	return 42.23

def lambda_handler(event, context):
	return str(temperature())

#class CityTemperature:
	#def temperaturecity(self, city):
	#self.city = city return 99