
import urllib, datetime, os, musiccrawler, re, csv, random, urllib2, eyed3
today = datetime.datetime.today()       #set global time
print 'url generator'
weekday = today.isoweekday()  #returns an integer corresponding with the weekday, 1 == Monday etc. etc.
####### Variables ######
Mp3Crawl_dir = '/Users/Pierce/Mp3Crawl'
Music_dir = '/Users/Pierce/Music/Captured'


#### ChubbyBeavers, other sites without schedules #####
def GenericSites():
    #no good list
    #Beathau5.com
    urls = ['http://www.chubbybeavers.com/','http://bacauhousemafia.ro/']
    for url in urls:
        musiccrawler.grab_music(url)

##### Thissongissick #####
        

##### Earmilk #####

def wwWednesday():
    print 'Today is Wednesday!'
    wwcount = open(str(Mp3Crawl_dir)+'/wwCount.txt', "r")
    #ww.write(wwcount+1)
    wwnumber = wwcount.readline()
    wwcount.close()
    url = 'http://www.earmilk.com/' + str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/wobble-wednesday-' +  str(wwnumber) + '/'
    print url
    
    #actually start downloading music
    #if there are 0 songs on page, a helper module (check_for_songs) will catch and break the program)

    if musiccrawler.grab_music(url) is False:
        return
    else:
        musiccrawler.grab_music(url)
        
    wwcount = open(str(Mp3Crawl_dir) +'/wwCount.txt', "w+")
    wwnumber = int(wwnumber) + 1
    print 'currently on WobbleWednesday #' + str(wwnumber)
    print 'saving number to wwCount.txt...'
    wwcount.write(str(wwnumber))
    wwcount.close()

def ssSunday():
    print 'Today is Sunday!'
    #open text file that contains the count of the current Suicide Sunday (>109)
    sscount = open(str(Mp3Crawl_dir) + "/ssCount.txt", "r")
    #ww.write(wwcount+1)
    ssnumber = sscount.readline()
    sscount.close()
    url = 'http://www.earmilk.com/' + str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/suicide-sundaes-week-' +  str(ssnumber) + '/'
    print url
    
    #actually start downloading music
    #if grab_music() doesn't finds 0 songs it will return a 0

    musiccrawler.grab_music(url)

    sscount = open(str(Mp3Crawl_dir) + "/ssCount.txt", "w+")
    ssnumber = int(ssnumber) + 1
    print 'currently on WobbleWednesday #' + str(ssnumber)
    print 'saving number to ssCount.txt...'
    sscount.write(str(ssnumber))
    sscount.close()

def ssMonday():
    print 'Today is Monday!'
    #open text file that contains the count of the current Suicide Sunday (>109)
    mmcount = open(str(Mp3Crawl_dir) + "/mmCount.txt", "r")
    
    mmnumber = mmcount.readline()
    mmcount.close()
    url = 'http://www.earmilk.com/' + str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/mashup-monday-week-' +  str(mmnumber) + '/'
    print url
    
    #actually start downloading music
    #if grab_music() doesn't finds 0 songs it will return a 0

    musiccrawler.grab_music(url)

    mmcount = open(str(Mp3Crawl_dir) + "/mmCount.txt", "w+")
    mmnumber = int(mmnumber) + 1
    print 'currently on MashupMonday #' + str(mmnumber)
    print 'saving number to mmCount.txt...'
    mmcount.write(str(mmnumber))
    mmcount.close()

def Daily2Percent:
    #need to figure out how to grab these urls from the homepage, they don't follow a straightforward pattern due to the song title being in the URL 


if weekday == 3: #Wednesday
    wwWednesday()
    
    
elif weekday == 0: #Monday


elif weekday == 7:  #7 equals Sunday
    ssSunday()
