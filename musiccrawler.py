import urllib, os, re, csv, random, urllib2, eyed3

####### Variables ######
Mp3Crawl_dir = '/Users/Pierce/Mp3Crawl'
Music_dir = '/Users/Pierce/Music/Captured'


os.chdir(Mp3Crawl_dir)
print 'Musiccrawler.py loaded'

def download_song(url):
    os.chdir(Music_dir)
    DownloadedURLs = [] #if URL is a success, it will be returned as a item in this list
    try:
        file_name = "CurrentDownload.mp3"  #this is temporary, change_filename() will change the name at the end
        u = urllib2.urlopen(url)
        mp3_data = u.read()
        f = open(file_name, 'wb')
        f.write(mp3_data)
        #script to display download progress#
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
            
        #call to change the file name from arbitiary number to actual song name
        changefilename(file_name)
        #return the valid URL so it can be added to records to eliminate redundancy
        return DownloadedURLs.append(url)
    except ValueError:
        print "oops! not valid a URL"
    except urllib2.HTTPError:
        print "HTTP Error 404: Not Found"
    except IndexError:
        print "list index out of range"
    

    
def dupe_checker(songs): #by songs I actually mean a listing of URL's
    print 'dupe checker loaded'
    os.chdir(Mp3Crawl_dir)
    URLlist = []
    newURLs = []
    songs_csv = open("songs_listing.csv", "r")
    record = csv.reader(songs_csv, delimiter=",")
    for records in record:
        for urls in records:
            URLlist.append(urls)
    print URLlist
    if songs is False:
        return False
    for song in songs:
        if song in URLlist:
            print 'Duplicate song URL found'
        else:
            newURLs.append(song)
    print str(len(newURLs)) + " brand spankin new songs found"
    return newURLs

def csv_writer(songs): #by songs I actually mean URL's list
    os.chdir(Mp3Crawl_dir)
    songs_csv = open("songs_listing.csv", "a")
    record = csv.writer(songs_csv)
    record.writerow(songs)
    print 'songs added to URL record'
    
def find_songs(url):
    SCtrackno = []
    fixedAPIurl = []
    page = urllib.urlopen(url).read()
    print "Page retrieved succesfully"
    print "are songs present?.."
    songs = re.findall(r'href=[\'"]?([^\'" >]+.mp3)', page)
    method2 = re.findall(r'href=[\'"]?([^\'" >]+/download)', page)
    literalstring = 'url\\=http\\%3A\\%2F\\%2Fapi\\.soundcloud\\.com\\%2Ftracks\\%2F[0-9]{8}'
    method3 = re.findall(literalstring, page)
    print method3
    for partial in method3:
        SCtrackno.append(partial[-8:])
    for number in SCtrackno:
        fixedAPIurl.append('http://api.soundcloud.com/tracks/'+ number +'/download?client_id=0f8fdbbaa21a9bd18210986a7dc2d72c')
    print fixedAPIurl
    for url in fixedAPIurl:
        songs.append(url)
    for song in method2:
        songs.append(song)
    print str(len(songs)) + " songs found"
    if len(songs) == 0:
        return False
    else:
        print "Yes, songs are here"
        return songs
    



def changefilename(song): #module to change the filename of the mp3 when it's finished downloding. Earmilk uses a strange filenaming convention
    os.chdir(Music_dir)
    try:
        audiofile = eyed3.load(song)
        print audiofile.tag.artist
        print audiofile.tag.title
        newname = str(audiofile.tag.title) + ".mp3"
        os.rename(song,newname)
    except AttributeError:
        print 'No valid ID3 tag present'


def grab_music(url):
    DownloadedURLs = []
    songs = find_songs(url)
    songs = dupe_checker(songs)
    if songs is False:
        return False
    else:
        for song in songs:
            os.chdir(Music_dir)
            DownloadedURLs.append(download_song(song))
    print "here's what's going into records"
    print DownloadedURLs
    print "here's what's going into records"
    csv_writer(DownloadedURLs)
