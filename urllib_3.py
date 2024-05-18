import urllib3
resp = urllib3.request("GET", "http://web.mit.edu/jywang/www/cef/Bible/NIV/NIV_Bible/ESTH+1.html")
print(resp.status)
print(resp.data)

html_doc = resp.data
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
#print(soup.dd)
#print(soup.dd['class'])
print("soup.a",soup.a)
print("soup.find_all('a')",soup.find_all('a'))
print(soup.find(id="link3"))
print("soup.body.b",soup.body.b)

#for link in soup.find_all('a'):
    #print("link.get('href')",link.get('href'))

body_tag = soup.body
print("len(body_tag)",len(body_tag))
print("len(body_tag.contents)",len(body_tag.contents))
b_tag = body_tag.contents[0]
print("ord(b_tag)",ord(b_tag))
#print("b_tag.contents",b_tag.contents)
#print("len(soup.contents)",len(soup.contents))
#print("soup.contents[0].name",soup.contents[0].name)