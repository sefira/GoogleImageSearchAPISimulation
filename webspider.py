# -*- coding: utf-8 -*-
#######################################
#   project：Google Image Search Spider
#   author：Xingyuan Bu: sefira32@gmail.com
#   date：2015-12
#   language：Python 2.7
#######################################

import urllib2
import re
import json

class webspider:
    
    def __init__(self):
        #https://www.google.com/search?q=pantheon+1.2+m+around+the+oculus&newwindow=1&source=lnms&tbm=isch
        self.mainweb_head = 'https://www.google.com/search?q='
        self.mainweb_tail = '&newwindow=1&source=lnms&tbm=isch'
        self.imageweblist = []
        self.imagejsonlist = []
        self.imageurllist = []
        self.imageContexturllist = []
        self.jsonresult = ''
        
    #open url
    def openurl(self,myurl):
        #mask
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        req = urllib2.Request(myurl, headers = headers)
        myresponse = urllib2.urlopen(req)
        #print myresponse
        mypage = myresponse.read()
        #print mypage
        return mypage

    #get image list from main web query
    def getimagelist(self,term,n_images):
        queryurl = self.mainweb_head + term + self.mainweb_tail
        print queryurl
        content = self.openurl(queryurl)
        #print content
        self.imageweblist = re.findall('\"rg_di rg_el ivg-i\"(.*?)<div class="rg_meta">(.*?)</div></div><!--n-->',content,re.S)
        print len(self.imageweblist)
        self.imageweblist = self.imageweblist[0:n_images]
        for imagecontent in self.imageweblist:
            #print len(imagecontent)
            self.imagejsonlist.append(imagecontent[1])
            #print imagecontent[0]
            moreurl = re.findall('<a href=\"/imgres\?imgurl=(.*?)&amp;imgrefurl=(.*?)&amp;h',imagecontent[0],re.S)
            #print moreurl
            self.imageurllist.append(moreurl[0][0])
            self.imageContexturllist.append(moreurl[0][1])

    #deal with a single image json
    def dealwithsingleimage(self,n_images):
        GsearchResultClassstr = '   \"GsearchResultClass\": \"GimageSearch\",\n'
        widthstr = '   \"width\": \"%s\",\n'
        heightstr = '   \"height\": \"%s\",\n'
        imageIdstr = '   \"imageId\": \"%s\",\n'
        tbWidthstr = '   \"tbWidth\": \"%s\",\n'
        tbHeightstr = '   \"tbHeight\": \"%s\",\n'
        unescapedUrlstr = '   \"unescapedUrl\": \"%s\",\n'
        urlstr = '   \"url\": \"%s\",\n'
        visibleUrlstr = '   \"visibleUrl\": \"%s\",\n'
        titlestr = '   \"title\": \"%s\",\n'
        titleNoFormattingstr = '   \"titleNoFormatting\": \"%s\",\n'
        originalContextUrlstr = '   \"originalContextUrl\": \"%s\",\n'
        contentstr = '   \"content\": \"%s\",\n'
        contentNoFormattingstr = '   \"contentNoFormatting\": \"%s\",\n'
        tbUrlstr = '   \"tbUrl\": \"%s\"\n'
        i = 0
        for imagejsonstr in self.imagejsonlist:
            #print imagejson
            imagejson = json.loads(imagejsonstr)
            self.jsonresult += '  {\n'
            self.jsonresult += GsearchResultClassstr
            self.jsonresult += widthstr % imagejson['ow']
            self.jsonresult += heightstr % imagejson['oh']
            self.jsonresult += imageIdstr % imagejson['id'].replace(":","")
            self.jsonresult += tbWidthstr % imagejson['tw']
            self.jsonresult += tbHeightstr % imagejson['th']
            self.jsonresult += unescapedUrlstr % self.imageurllist[i]
            self.jsonresult += urlstr % self.imageurllist[i]
            self.jsonresult += visibleUrlstr % ('www.'+imagejson['isu'])
            self.jsonresult += titlestr % imagejson['pt']
            self.jsonresult += titleNoFormattingstr % imagejson['pt']
            self.jsonresult += originalContextUrlstr % self.imageContexturllist[i]
            self.jsonresult += contentstr % imagejson['pt']
            self.jsonresult += contentNoFormattingstr % imagejson['pt']
            #self.jsonresult += tbUrlstr % imagejson['tu']
            self.jsonresult += tbUrlstr % ('http://images.google.com/images?q=tbn:' + imagejson['id'].replace(":",""))
            self.jsonresult += '  }'
            i += 1
            #print i
            if(i != n_images):
                self.jsonresult += ',\n'
            else:
                self.jsonresult += '\n'    
            
    #start to write all json-like string
    def generatejsonstring(self,n_images):
        headstr = '{\"responseData\": {\n \"results\": [\n'
        tailstr = ' ]}\n}'
        self.jsonresult += headstr;
        self.dealwithsingleimage(n_images)
        self.jsonresult += tailstr;
        
    #entrance
    def querythisword(self, term, n_images):
        from urllib import quote_plus
        term=quote_plus(term)
        self.getimagelist(term,n_images)
        self.generatejsonstring(n_images)
        return self.jsonresult
    
