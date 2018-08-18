# Import requests (to download the page)
import requests
# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup
# Import Time (to add a delay between the times the scape runs)
import time
# Import smtplib (to allow us to email)
import smtplib
# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.
# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "http://kk.reservertid.nu/Time/1026?pid=1051"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # making sure we get the site
    downloaded = False
    while downloaded == False:
        try:
            # download the homepage
            response = requests.get(url, headers=headers)
            downloaded = True
        except:
            print("Error getting site, trying again in 60 sec")        
            time.sleep(60)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")
    # if the number of times the word "Google" occurs on the page is less than 1,
    dates=["20170805","20170806","20170807",
           "20170808","20170809","20170810","20170811",
           "20170812","20170813"]
    for date in dates:
        if str(soup).find(date) == -1:
            #for debugging, comment later
            #2017 08 12
            print(date[0:4]+'-'+date[4:6]+'-'+date[6:8]+' not found')
            # continue with the script,
            continue
        #if date is available,
        else:
            # create an email message with just a subject line,
            msg = 'Encontro algo!\n'+\
                   date[0:4]+'-'+date[4:6]+'-'+date[6:8]+'\n'+\
                   url
            # set the 'from' address,
            fromaddr = 'mail@gmail.com'
            # set the 'to' addresses,
            toaddrs  = ['mail@gmail.com']
            #toaddrs  = ['jacksparrow.88@gmail.com','A_SECOND_EMAIL_ADDRESS', 'A_THIRD_EMAIL_ADDRESS']
            # setup the email server,
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password,
            server.login("mail", "mail-pass")
            
            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)
            
            # send the email
            server.sendmail(fromaddr, toaddrs, msg)
            # disconnect from the server
            server.quit()
            #end while loop
            break
    # wait 300 seconds if no date was found available,
    print('Waiting 300 segs...')
    # wait 300 seconds and search again
    time.sleep(300)




