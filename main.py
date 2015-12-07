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
for eachline in alllines:
    term = eachline
    dirname = savedir + "/" + ("%04d" % countdir)
    if not os.path.exists(dirname):

        os.makedirs(dirname)
    countdir += 1
    #capturing web
    #print u'capturing web'
    print "search: %s" % term
    myspider = webspider.webspider()
    try:
        res = myspider.querythisword(term, n_images)
        jsonres = json.loads(res)
        allreturn = []
        allreturn.extend(jsonres['responseData']['results'])
        countfile = 0
        for i,aret in enumerate(allreturn):
            #print aret
            filename = dirname + "/" + ("%04d" % countfile) + ".jpg"
            print filename
            print aret["tbUrl"]
            #print "\n"
            #urllib.urlretrieve(aret["tbUrl"],filename)
            data = urllib.urlopen(aret["tbUrl"]).read()
            f = open(filename, 'wb')
            f.write(data)  
            f.close()  
            
    except Exception, e:
        print 'Caught exception %s, so sleeping for a bit' % (e)

    
