
import urllib, datetime, os, musiccrawler, re, csv, random, urllib2, eyed3
today = datetime.datetime.today()       #set global time
print 'url generator'
weekday = today.isoweekday()  #returns an integer corresponding with the weekday, 1 == Monday etc. etc.


#Thissongissick
        

#Earmilk

def wwWednesday():
    'Today is Wednesday!'
    wwcount = open("//Users/Pierce/Documents/Programming/wwCount.txt", "r")
    #ww.write(wwcount+1)
    wwnumber = wwcount.readline()
    wwcount.close()
    url = 'http://www.earmilk.com/' + str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/wobble-wednesday/' +  str(wwnumber) + '/'
    print url
    
    #actually start downloading music
    #if grab_music() doesn't finds 0 songs it will return a 0
    if int(musiccrawler.grab_music(url)) == 0:
        return   #return out of the function without changing the contents of wwCount.xt
    
    else:
        musiccrawler.grab_music(url)

    wwcount = open("/Users/Pierce/Documents/Programming/wwCount.txt", "w+")
    wwnumber = int(wwnumber) + 1
    print 'currently on WobbleWednesday #' + str(wwnumber)
    print 'saving number to wwCount.txt...'
    wwcount.write(str(wwnumber))
    wwcount.close()

def ssSunday():
    'Today is Sunday!'
    #open text file that contains the count of the current Suicide Sunday (>109)
    sscount = open("//Users/Pierce/Documents/Programming/ssCount.txt", "r")
    #ww.write(wwcount+1)
    ssnumber = sscount.readline()
    sscount.close()
    url = 'http://www.earmilk.com/' + str(today.year) + '/' + str(today.month) + '/' + str(today.day) + '/suicide-sundaes-week-' +  str(ssnumber) + '/'
    print url
    
    #actually start downloading music
    #if grab_music() doesn't finds 0 songs it will return a 0
    if int(musiccrawler.grab_music(url)) == 0:
        return   #return out of the function without changing the contents of wwCount.xt
    
    else:
        musiccrawler.grab_music(url)

    sscount = open("/Users/Pierce/Documents/Programming/ssCount.txt", "w+")
    ssnumber = int(ssnumber) + 1
    print 'currently on WobbleWednesday #' + str(ssnumber)
    print 'saving number to ssCount.txt...'
    sscount.write(str(ssnumber))
    sscount.close()



if weekday == 3: #Wednesday
    wwWednesday()
    
    
#elif weekday == 0: #Monday


elif weekday == 7:  #7 equals sunday
    ssSunday()
