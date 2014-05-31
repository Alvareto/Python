import re, urlib.request

# koristim Visual Studio, pa mi se ne isplati ostvarivati preko argumenata naredbenog retka (to je ionako piece of cake)
url = input("Enter the website address")

stranica = urlib.request.urlopen(url)
mybytes = stranica.read()
html = mybytes.decode("utf8")
print html



##
# pronaci i izlistati sve linkove na druge stranice
def find_urls(html):
    regexp_link = r'''</?a((s+w+(s*=s*(?:".*?"|'.*?'|[^'">s]+))?)+s*|s*)/?>w+</a>'''
    pattern = re.compile(regexp_link)

	url_list = re.findall(pattern, html)

	return url_list

##
# napraviti listu svih hostova kojima se sa stranice može pristupiti (bez ponavljanja)
##
# za svaki host odrediti broj referenciranja u razmatranoj stranici
def find_and_count_hosts(url_list):
	host_list = {}
	for url in url_list:
		# https://www.fer.unizg.hr/predmet/skrjez
		host = url.split(r'//').split('/')[0]
		if host in host_list:
			host_list[host] = 1
		else:
			host_list[host]++
	return host_list

##
# pronaci sve e-mail adrese u toj stranici
def find_emails(html):
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
            img_count++
    return img_count
