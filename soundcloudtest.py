import urllib, os

os.chdir('/Users/Pierce/Music')
url = 'http://soundcloud.com/nickraymondg/bro-safari-feat-dj-craze/download'
resp = urllib.urlopen(url)
image_data = resp.read()
# Open output file in binary mode, write, and close.
f = open('test.mp3','wb')
f.write(image_data)
f.close()
