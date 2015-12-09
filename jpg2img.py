# -*- coding: cp936 -*-
import os
target = 'image_search'

def renamethefile(filename):
    renamedflag = 0
    if os.path.isfile(filename)==True:
        if filename.find('.jpg') > 0:
            newfilename=filename.replace(".jpg",".img")
            os.rename(filename,newfilename)
            renamedflag = 1
    return renamedflag

def thoughtdir(dirname):
    #print dirname
    renamecount = 0
    for resultname in os.listdir(dirname):
        #print resultname
        resultname = os.path.join(dirname,resultname)
        if os.path.isdir(resultname) == True:
            thoughtdir(resultname)
        if os.path.isfile(resultname) == True:
            renamecount += renamethefile(resultname)
    print "In %s renamed %d imagefile " % (resultname,renamecount)

                      
thoughtdir(target)
