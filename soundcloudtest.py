import urllib, os, re


def find_songs(url):
    page = urllib.urlopen(url).read()
    print page
    songs = re.findall(r'href=[\'"]?([^\'" >]+/download)', page)
    songs.append(re.findall(r'href=[\'"]?([^\'" >]+.mp3)', page))
    print songs
    #songs.append(re.findall('rhref=[\'"]?([^\'" >]+.mp3)'

def download_songs(url):
    os.chdir('/Users/Pierce/Music')
    resp = urllib.urlopen(url)
    image_data = resp.read()
    # Open output file in binary mode, write, and close.
    f = open('test.mp3','wb')
    f.write(image_data)
    f.close()


