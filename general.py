import os

def create_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		
def write_file(path, data):
	f = open(path, 'w')
	try:
		f.write(data)
	except (ValueError, TypeError):
		pass
	f.close()
