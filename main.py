#!/usr/bin/python
# Author: hoangdoan

import os, pwd
from time import strftime

# Get username
USER = pwd.getpwuid(os.getuid()).pw_name

# Ubuntu default Download directory
DOWNLOAD_DIR = "/home/%s/Downloads/" %USER
DIR_PREFIX = 'UDO_'

file_extensions = {
	'Slide' : ['ppt', 'pptx'],
	'Compress' : ['tar', 'gz', 'zip', 'rar', '7z', 'tgz'],
	'Office' : ['doc', 'docx', 'odt', 'xls', 'xlsx', 'csv'],
	'Portable_Document' : ['pdf', 'epub'],
	'Database' : ['db', 'sql', 'sqlite', 'sqlite3'],
	'Plain_Text' : ['txt', 'json', 'log'],
	'Package_Installer' : ['deb', 'rpm', 'apk', 'jar'],
	'Images' : ['jpeg', 'png', 'bmp', 'svg'],
	'Others' : ['*']
}

# Add slash
if DOWNLOAD_DIR.endswith('/') == False:
	DOWNLOAD_DIR = DOWNLOAD_DIR + '/'

if os.path.isdir(DOWNLOAD_DIR) == False:
	print "Your DOWNLOAD_DIR not exists"
	exit()

# Print current-time
current_time = strftime("%Y-%m-%d %H:%M:%S")
print "+" + len(current_time)*"-" + "+\n|" + current_time + "|\n" + "+" + len(current_time)*"-" + "+"
print "[+] Your downloads location is %s" %DOWNLOAD_DIR

# Get list file-only
list_files = [f for f in os.listdir(DOWNLOAD_DIR) if os.path.isfile(os.path.join(DOWNLOAD_DIR, f))]

if len(list_files) == 0:
	print '[+] Nothing to do'
	exit()

list_dir = file_extensions.keys()

# Get file extension specified by filename
def get_file_ext(filename):
	t = filename.split('.')
	return t[len(t)-1]

list_files_subdir = {}

for ld in list_dir:
	list_files_subdir[ld] = []

# Organize known file types
pick_files = []
for index, lf in enumerate(list_files):
	for ld in list_dir:
		if get_file_ext(lf) in file_extensions[ld]:
			list_files_subdir[ld].append(lf)
			pick_files.append(index)

# Other files types
list_files_subdir['Others'] = [c for i,c in enumerate(list_files) if (i not in pick_files)]

# Organize files into Sub-directories
for p_dir, p_list in list_files_subdir.iteritems():
	if len(p_list) > 0:
		if (not os.path.isdir(DOWNLOAD_DIR + DIR_PREFIX + p_dir)):
			os.mkdir(DOWNLOAD_DIR + DIR_PREFIX + p_dir)
			print "[+] Make directory %s" %(DOWNLOAD_DIR + DIR_PREFIX + p_dir)
		else:
			print "[+] Directory %s exists" %(DOWNLOAD_DIR + DIR_PREFIX + p_dir)
		for f in p_list:
			print "---> Move file %s to %s" %(f, DIR_PREFIX + p_dir + '/' + f)
			os.rename(DOWNLOAD_DIR + f, DOWNLOAD_DIR + DIR_PREFIX + p_dir + '/' + f)
