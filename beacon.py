import urllib
import robotexclusionrulesparser as rerp
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin
# 
def get_page(url):
	page_url = urlparse(url)
	base = page_url[0] + '://' + page_url[1]
	robots_url = base + '/robots.txt'
	rp = rerp.RobotFileParserLookalike()
	rp.set_url(robots_url)
	rp.read()
	if not rp.can_fetch('*', url):
		print "Page off limits!"
		return BeautifulSoup(""), ""
	if url in cache:
		return cache[url]
	else:
		# print "Page not in cache: " + url
		try:
			content = urllib.urlopen(url).read()
			return BeautifulSoup(content), url
		except:
			return BeautifulSoup(""), ""


cache = {}

url_list = []
content_list = []

with open('url.txt') as fin:
	for line in fin:
		url_list.append(line.strip())

content_list = []
page = url_list[2]
print page
soup, url = get_page(page)
desc = soup.find_all('div',attrs={"class" : "article-element body"})
content_list.append(desc[0].text.encode("ascii","ignore"))
print content_list

# with open('meta.txt', 'a') as fout:
# 	for content in content_list:
# 		fout.write(content.strip())


