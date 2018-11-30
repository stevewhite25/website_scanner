import socket

def get_ip_address(url):
	results = socket.gethostbyname(url)
	print(f'Getting IP Address of {url} ')
	return results

# print(get_ip_address('reddit.com'))
