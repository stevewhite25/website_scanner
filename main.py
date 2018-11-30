from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

root_dir = 'targets'
create_dir(root_dir)

def gather_info(name, url):
	domain_name = get_domain_name(url)
	ip_address = get_ip_address(domain_name)
	nmap = get_nmap('-F', ip_address)
	robots_txt = get_robots_txt(url)
	whois = get_whois(domain_name)
	
	create_report(name, url, domain_name, nmap, robots_txt, whois)
	
def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
	project_dir = root_dir + '/' + name
	print(f'Creating Directory - {project_dir}')
	create_dir(project_dir)
	write_file(project_dir + '/full_url.txt', full_url)
	write_file(project_dir + '/domain_name.txt', domain_name)
	write_file(project_dir + '/nmap.txt', nmap)
	write_file(project_dir + '/robots_txt.txt', robots_txt)
	write_file(project_dir + '/whois.txt', whois)
	
while True:
	question = 'What would you like the new folder to be called? (i.e., google, reddit, etc) To quit press \'q\' at any time. '
	filename = input(question)
	if filename == 'q':
		break
	else:
		web_question = 'What website would you like to scan? Please include https:// or http://  '
		website_addr = input(web_question)

		gather_info(filename, website_addr)
		
		continue_question = input('Would you like to scan another site? (y/n?) ')
		if continue_question == 'n':
			break

# example of manual entry  -->  gather_info('mountain_state', 'http://www.mountainstatefinancial.com')
