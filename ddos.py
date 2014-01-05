import requests

while(True):
	try:
		requests.get("http://27.251.237.196/pesitcs/")
	except:
		print "error"
