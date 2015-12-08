import urllib,urllib2 
url   = "http://www.google.com/" 
proxy = "127.0.0.1:8087"

imageurl = "http://images.google.com/images?q=tbn:mbqFtcbw1fkOBM"
filename = "1.jpg"
opener = urllib2.build_opener( urllib2.ProxyHandler({"http":proxy}) ) 
urllib2.install_opener( opener )
#sContent = urllib2.urlopen(url) 
#print sContent.read()#data = urllib.urlopen(aret["tbUrl"]).read()
data = urllib2.urlopen(imageurl).read()
f = open(filename, 'wb')
f.write(data)  
f.close()
