import selenium
from selenium import webdriver


import os
import sys
import subprocess
import time

#print "---------------"
#print os.environ["PATH"]
#os.environ["PATH"] += os.pathsep + "/usr/bin"
#print os.environ["PATH"]

#print "--------------- sys.path"
#print(sys.path)
#sys.path.append("/usr/bin")
#print(sys.path)
#print "--------------- PYTHONPATH"
#print(os.getenv('PYTHONPATH'))
#print "---------------"
#print(subprocess.check_output(["which", "chromedriver"]))

browser = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path='/usr/bin/')
time.sleep(0)
browser.get('https://ezgif.com/reverse?url=http://i.imgur.com/IWfFk1h.mp4')
browser.find_element_by_css_selector('.button.primary').click()

time.sleep(5)
#browser.find_element_by_css_selector('.outfile')
#rev_url = browser.find_elements_by_tag_name('video')[1].find_element_by_tag_name('source').get_attribute('src')
rev_url= browser.find_element_by_xpath('//*[@id="output"]/p[1]/video/source').get_attribute('src')
print(rev_url)
time.sleep(5)
browser.quit()
