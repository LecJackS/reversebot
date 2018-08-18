#import the library used to query a website
import urllib, urllib2

#specify the url
#wiki = "https://ezgif.com/reverse-video/ezgif-4-b856e71256.mp4"
url = "https://ezgif.com/reverse?url=http://i.imgur.com/IWfFk1h.mp4"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(url)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html5lib")
#print "All:"
#print soup.prettify().encode('UTF-8')
print "---------------- Form ----------------"
#print soup.find("input", {"class":"button primary","name":"effects","type":"submit","value":"Reverse!"})
complete_form = soup.find("form", {"class":"form ajax-form"}).prettify()
print complete_form

fetchedurl = "https://ezgif.com/reverse-video/ezgif-4-b856e71256.mp4"
url = "https://ezgif.com/reverse-video/ezgif-4-b856e71256.mp4"
form_data = {'file':"ezgif-4-b856e71256.mp4",
             'token':"dc149fb208",
             'audio':"false",
             'mute':'false',
             'effects':'Reverse!'}
params = urllib.urlencode(form_data)
print "params "+params
response = urllib2.urlopen(url, params)
data = response.read()
print "---------------- Printing shit ----------------"
print BeautifulSoup(data, "html5lib").prettify().encode('UTF-8')
print "---------------- searching shit ----------------"

#print data.find("https://im4.ezgif.com/tmp/ezgif-4-2ac683f788.mp4")

print data.find("2ac683f788.mp4")










