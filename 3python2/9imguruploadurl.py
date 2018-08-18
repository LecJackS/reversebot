import pyimgur

CLIENT_ID = "ffc7dd68362e1f6"
PATH = "A Filepath to an image on your computer"

im = pyimgur.Imgur(CLIENT_ID)
#uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
imgurl = 'https://im.ezgif.com/tmp/ezgif-1-1b74e6d257.mp4'
uploaded_image = im.upload_image(url=imgurl, title="Testing something")
print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)