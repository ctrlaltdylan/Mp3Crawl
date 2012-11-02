import urllib, os, re, csv, random, urllib2, eyed3

####### Variables ######
Mp3Crawl_dir = '/Users/Pierce/Mp3Crawl'
Music_dir = '/Users/Pierce/Music/Captured'


os.chdir(Mp3Crawl_dir)
print 'Musiccrawler.py loaded'


def create_song_list(url):
    page = urllib.urlopen(url).read()
    print 'Compiling List...'
    songs = re.findall(r'href=[\'"]?([^\'" >]+.mp3)', page)
    
    

def find_songs(url):
    page = urllib.urlopen(url).read()
    print "Page retrieved succesfully"
    print "are songs present?.."
    songs = re.findall(r'href=[\'"]?([^\'" >]+.mp3)', page)
    method2 = re.findall(r'href=[\'"]?([^\'" >]+/download)', page)
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
    audiofile = eyed3.load(song)
    print audiofile.tag.artist
    print audiofile.tag.title
    newname = str(audiofile.tag.title) + ".mp3"
    os.rename(song,newname)


def grab_music(url):
    songs = find_songs(url)
    if songs is False:
        return False
    else:
        os.chdir(Music_dir)
        title = 'Current_Download'   #iteration used to name the files when they are downloading, once they are finished, then changefilename() will be used to change to the actual name
        for song in songs:
         #experiment with filename
            file_name = str(title) + ".mp3"  #song.split('/')[-1]
            u = urllib2.urlopen(song)
            f = open(file_name, 'wb')
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
                print status,

            f.close()
            #title iteration
            title = title + 1
            #call to change the file name from arbitiary number to actual song name
            changefilename(file_name)



