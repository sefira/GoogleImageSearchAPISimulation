# -*- coding: utf-8 -*-
#######################################
#   project：Google Image Search Spider
#   author：Xingyuan Bu: sefira32@gmail.com
#   date：2015-12
#   language：Python 2.7
#######################################

import webspider

print u"""
--------------------------------------- 
   project：Google Image Search Spider
   author：Xingyuan Bu: sefira32@gmail.com
   date：2015-12
   language：Python 2.7
--------------------------------------- 
"""

print u'start project：'

#capturing web
print u'capturing web'
myspider = webspider.webspider()
try:
    term = 'pantheon 1.2 m around the oculus'
    n_images = 20
    i = 1
    res = myspider.querythisword(term, n_images)
    print res
except Exception, e:
    print 'Caught exception %s, so sleeping for a bit' % (e)
    
