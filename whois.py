import os

def get_whois(url):
	print(f'Getting WHOIS info for {url} ')
	command = 'whois ' + url
	process = os.popen(command)
	results = str(process.read())
	return results

#print(get_whois('https://www.microsoft.com/'))
