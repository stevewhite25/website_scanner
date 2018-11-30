import urllib.request
import urllib.error
import io

def get_robots_txt(url):
	if url.endswith('/'):
		path = url
		print(f'Getting robots.txt from {url}')
	else:
		path = url + '/'
		print(f'Getting robots.txt from {url}')
	try:
		req = urllib.request.urlopen(path + 'robots.txt', data=None)
		data = io.TextIOWrapper(req, encoding='utf-8')
		return data.read()
	except (urllib.error.HTTPError, urllib.error.URLError):
		print('Error 404 - robots.txt  not found')

# print(get_robots_txt('https://www.reddit.com/'))
# print(get_robots_txt('http://www.mountainstatefinancial.com/'))  #  example with no robots.txt
