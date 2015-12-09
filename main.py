# -*- coding: utf-8 -*-
#######################################
#   project：Google Image Search Spider
#   author：Xingyuan Bu: sefira32@gmail.com
#   date：2015-12
#   language：Python 2.7
#######################################

import webspider
import json
import os
import urllib
import urllib2

print u"""
--------------------------------------- 
   project：Google Image Search Spider
   author：Xingyuan Bu: sefira32@gmail.com
   date：2015-12
   language：Python 2.7
--------------------------------------- 
"""

print u'start project：'

fp = open("tpc97143e1_fbf3_442a_95d7_c8545b71c10e.txt",'r')
savedir = "image_search"
alllines = fp.readlines()
fp.close()
n_images = 20
countdir = 0
proxy = "127.0.0.1:8087"
opener = urllib2.build_opener( urllib2.ProxyHandler({"http":proxy}) ) 
urllib2.install_opener( opener )

try:	
    for eachline in alllines:
        term = eachline
        dirname = savedir + "/" + ("%04d" % countdir)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        #capturing web
        #print u'capturing web'
        print "\nsearch: %s" % term.strip('\n')
        
        #write termfile:
        term_fname = dirname + "/" + 'search_term.txt'
        termfile = open(term_fname,'w')
        print>>termfile,("(%d, \'%s\')" % (countdir,term.strip('\n')))
        countdir += 1
        termfile.close()
        
        myspider = webspider.webspider()
        res = myspider.querythisword(term, n_images)
        jsonres = json.loads(res.replace("\\","\\\\"))
        allreturn = []
        allreturn.extend(jsonres['responseData']['results'])

        #download images
        countfile = 0
        allurls = []
        allfnames = []
        for i,aret in enumerate(allreturn):
            #print aret
            filename = dirname + "/" + ("%04d" % countfile) + ".jpg"
            countfile += 1
            print "save to: " + filename
            print "downloading: " + aret["tbUrl"]
            #print "\n"
            #urllib.urlretrieve(aret["tbUrl"],filename)
            data = urllib2.urlopen(aret["tbUrl"]).read()
            f = open(filename, 'wb')
            f.write(data)  
            f.close()
            #file = urllib.URLopener()
            #file.retrieve(aret["tbUrl"], filename)
            allurls.append(aret['tbUrl'])
            allfnames.append(filename)
        tojson = dict(results=allreturn, thumburls=allurls, thumbfnames=allfnames)
        jsonfname = dirname + "/" + 'index.json'
        json.dump(tojson, open(jsonfname, 'w'), indent=2)
            
except Exception, e:
    print 'Caught exception %s, so sleeping for a bit' % (e)

    
