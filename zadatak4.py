import re
import urllib.request
import sys

if(len(sys.argv) < 2):
	arg = input("Enter the website address\n")
else:
	arg = sys.argv[1]

def load_url():
	stranica = urllib.request.urlopen(arg)
	html = "".join(stranica.read().decode(encoding='UTF-8',errors='ignore'))
	return html

html = load_url()

##
# pronaci i izlistati sve linkove na druge stranice
def find_urls(html):
	url_list = []
	m = re.findall('href *= *[\'"]([^\'"]+)', html) # find the href
	if m:
		for url in m:
			if url[:1] != "/":
				url_list.append(url)
	return url_list

print("\nAll links on page linking to other pages:")
for url in find_urls(html):
	print(url)

##
# napraviti listu svih hostova kojima se sa stranice može pristupiti (bez ponavljanja)
##
# za svaki host odrediti broj referenciranja u razmatranoj stranici
def find_and_count_hosts(url_list):
	host_list = {}
	for url in url_list:
		# https://www.fer.unizg.hr/predmet/skrjez
		try:
			pokusniKunic = str(url).split(r'/')[2]
		except IndexError:
			continue
		host = str(url).split(r'/')[2]
		if host in host_list:
			host_list[host] += 1
		else:
			host_list[host] = 1
	return host_list

print("\n\nDomena\t\tBroj pojavljivanja")
hosts = find_and_count_hosts(find_urls(html))
for host in hosts:
	print(host + "\t" + str(hosts[host]))

##
# pronaci sve e-mail adrese u toj stranici
def find_emails(html):
	regex_email = r'[^@]+@[^@]+\.[^@]+'
	pattern = re.compile(regex_email)
	email_list = []
	for word in html.split():
		email_list.extend(re.findall(pattern, word))
	return email_list

emails = find_emails(html)
if len(emails) == 0:
	print("\nThere are no emails found.\n")
else:
	print("\nThere are " + str(len(emails)) + " emails found:")
	for email in emails:
		print(email)

##
# prebrojati linkove na slike (<img src="url" ... >)
def count_imgs(html):
	img_count = 0
	for tag in re.findall('< *img +src[^>]+', html): # find the img tags
		m = re.search('src *= *[\'"]([^\'"]+)', tag) # find the src
		if m:
			# url_list.append(m.group(1)) # add the sub match
			img_count += 1
	return img_count

images = count_imgs(html)
if images == 0:
	print("\nThere are no images found.\n")
else:
	print("There are " + str(images) + " images found.")

def list_imgs(html):
	img_list = []
	for tag in re.findall('< *img +src[^>]+', html): # find the img tags
		m = re.search('src *= *[\'"]([^\'"]+)', tag) # find the src
		if m:
			img_list.append(m.group(1)) # add the sub match
	return img_list
