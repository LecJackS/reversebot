import praw
from PIL import Image, ImageSequence

bot = praw.Reddit(user_agent='reversebot69',
                  client_id='EP1GYs0pY7LmOA',
                  client_secret='-NDeSW7zUrA_p8Auop2szWlwDVk',
                  username='reversebot69',
                  password='celestereddit159')
                  
subreddit = bot.subreddit('gifs')
#comments = subreddit.stream.comments()

#submissions = subreddit.top
import urllib

for x in subreddit.top('all'):
    #print x.permalink
    #print x.url
    randurl = x.url

#randurl = subreddit.top('all')[0]
randurl = randurl.replace(".gifv",".mp4")
print "Downloading "+randurl


reversedurl = "https://ezgif.com/reverse-video?url="+randurl

testfile = urllib.URLopener()
try:
    testfile.retrieve(randurl, "test.gif")
except Exception,e:
    print e
print "Downloaded"
im = Image.open('test.gif')
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
frames.reverse()
frames[0].save('reversed.gif', save_all=True, append_images=frames[1:])

'''for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'space' in text.lower():
        # Generate a message
        #message = "Why no love for Titan, u/{0} ?".format(author)
        print "Found:"
        print "- User: "+str(author)
        #comment.reply(message) # Send message
        print "waiting..."
        '''