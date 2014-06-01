import re
import urllib.request

def load_url():
	stranica = urllib.request.urlopen(input("Enter the website address\n"))
	html = "".join(stranica.read().decode(encoding='UTF-8',errors='ignore'))
	return html

html = load_url()

##
# pronaci i izlistati sve linkove na druge stranice
def find_urls(html):
	url_list = []
	m = re.findall('href *= *[\'"]([^\'"]+)', html) # find the href
	if m: url_list.extend(m)
	return url_list

print("All links on page: \n")
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

print("Host\tCount\n")
print(find_and_count_hosts(find_urls(html)))

##
# pronaci sve e-mail adrese u toj stranici
def find_emails(html):
	# http://incurlybraces.com/python-extract-email-address-regular-expression.html
	regexp_email = r'''([w-.+]+@w[w-]+.+[w-]+)'''
	pattern = re.compile(regexp_email)
	email_list = re.findall(pattern, html)
	return email_list

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

def list_imgs(html):
	img_list = []
	for tag in re.findall('< *img +src[^>]+', html): # find the img tags
		m = re.search('src *= *[\'"]([^\'"]+)', tag) # find the src
		if m:
			img_list.append(m.group(1)) # add the sub match
	return img_list
