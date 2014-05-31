import re, urlib.request

# koristim VS, pa mi se ne isplati ostvarivati preko argumenata naredbenog retka (to je ionako piece of cake)
url = input("Enter the website address")

stranica = urlib.request.urlopen(url)
mybytes = stranica.read()
html = mybytes.decode("utf8")
print html

## 
#  => označava opis problema kojeg fja rješava#  

##
# pronaci i izlistati sve linkove na druge stranice
def find_urls(html):
    regexp_link = r'''</?a((s+w+(s*=s*(?:".*?"|'.*?'|[^'">s]+))?)+s*|s*)/?>w+</a>'''
    pattern = re.compile(regexp_link)

	url_list = re.findall(pattern, html)

	return url_list

print find_urls(html)

##
# napraviti listu svih hostova kojima se sa stranice može pristupiti (bez ponavljanja)
##
# za svaki host odrediti broj referenciranja u razmatranoj stranici
def find_and_count_hosts(url_list):
	host_list = {}
	
	for url in url_list:
		# i.e. https://www.fer.unizg.hr/predmet/skrjez
		host = url.split(r'//')[1].split(r'/')[0] # prvi split odvaja https, drugi odvaja host, tj domenu
	
		if host in host_list:
			host_list[host] = 1 # Python ne postavlja početno automatski u nulu kao što radi blaženi Perl
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
            img_count++
            
    return img_count
