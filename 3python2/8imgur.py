from imgurpython import ImgurClient

# If you already have an access/refresh pair in hand
client_id = 'ffc7dd68362e1f6'
client_secret = '9a2a06c85329e39648ac4094ed6174a3215f098e'
access_token = '00b4ebf77302bf9665cb8d016858d77e19a4f93a'
refresh_token = '6e7c6da8f481ee71cbae41a046dcedeec84797db'

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

url='https://im.ezgif.com/tmp/ezgif-1-7847e769eb.mp4'

client.upload_from_url(url, config=None, anon=False)
