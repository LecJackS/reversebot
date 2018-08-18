import mechanize
from bs4 import BeautifulSoup

print "0-------------------------------"
url = "https://ezgif.com/reverse-video"
br = mechanize.Browser()
br.open(url)


#def select_form(form):
#    return form.attrs.get('class', None) == 'multipart/form-data'

form = br.forms()[0]
#form = br.forms()[0]
print form
print "1-------------------------------"
form['new-image-url'] = 'http://i.imgur.com/IWfFk1h.mp4'
print form
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this

request2 = form.click()
print request2
print ".-testeando after first click------------------------"
for link in br.links():
    pass
    #print link
try:
    response2 = mechanize.urlopen(request2)
except mechanize.HTTPError, response2:
    pass
    
print "2-------------------------------"    
print response2.geturl()
br.open(response2.geturl())
form = br.forms()[0]
print form
request3 = form.click()
print "-----------------------"
print "- request after click on Reverse! --------------------------"
print request3.get_data()
print "-----------------------"

#print "br shit-------------------"
#for link in br.links():
#    pass
    #print link
#print BeautifulSoup(mechanize.urlopen(request2).read(), "html5lib").prettify().encode('UTF-8')
try:
    response3 = br.open(request3)
except mechanize.HTTPError, response3:
    pass
print "3-response3-geturl-----------------------------"    

#print BeautifulSoup(response3.read(), "html5lib").prettify().encode('UTF-8')

print response3.geturl()


'''
url = "https://ezgif.com/reverse?url=http://i.imgur.com/IWfFk1h.mp4"

form_data = {'file':"ezgif-4-b856e71256.mp4",
             'token':"dc149fb208",
             'audio':"false",
             'mute':'false',
             'effects':'Reverse!'}


def select_form(form):
    #print 'Entra a select_form'
    #print form.attrs.get('class', None)
    return form.attrs.get('class', None) == 'form ajax-form'



br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
#br.set_handle_robots(False)   # ignore robots
#br.set_handle_refresh(False)  # can sometimes hang without this
#br.addheaders =  [('User-agent', 'Firefox')]  	      	# [('User-agent', 'Firefox')]
#br.open(mechanize.urljoin(url, ""))
br.open(url)

#print br.title()
#print response1.geturl()
#print response1.info()  # headers
#print response1.read()  # body

#forms = list(br.forms())
#print forms
#br.select_form(predicate=select_form)
form = br.forms()[0]
print form
request2 = form.click()

#print BeautifulSoup(mechanize.urlopen(request2).read(), "html5lib").prettify().encode('UTF-8')
#print mechanize.urlopen(request2).read()
 ##print list(br.links())

#br.set_all_readonly(False)
#br['file'] = 'ezgif-4-b856e71256.mp4'
#br['token'] = 'dc149fb208'
#br['audio'] = False
#br['mute'] = False
#br['effects'] = 'Reverse!'
#br.submit()
#br.click()
#print br.response().read()
#print BeautifulSoup(br.response().read(), "html5lib").prettify().encode('UTF-8')


'''








