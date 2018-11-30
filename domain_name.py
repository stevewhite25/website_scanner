from tld import get_tld, get_fld

def get_domain_name(url):
	domain_name = get_fld(url)
	print(f'Getting Domain Name from {url}')
	return domain_name
	
# print(get_domain_name('https://www.reddit.com/'))
