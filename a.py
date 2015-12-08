import urllib

def download_file(url, filename):
  print "Downloading file: %s and saving as %s" % (url, filename)
  file = urllib.URLopener()
  try:
    file.retrieve(url, filename)
  except IOError as (errno, strerror):
    print "Error: could not download file. %s, %s" % (errno, strerror)

download_file("http://img4.duitang.com/uploads/item/201209/04/20120904031734_wvXyK.thumb.600_0.jpeg", "2.jpg")
