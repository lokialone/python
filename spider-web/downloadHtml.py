#-*- coding:utf-8 -*-
import urllib2,urllib

root_path = '/Users/lokalone/code/tech/python/assets'
url = 'http://www.koolearn.com/'
def downloadHtml():
    req = urllib2.Request(url)
    content = urllib2.urlopen(req).read()

def createDir(url):
    file_name = url.split("/")[-1]
    file_path = root_path + file_name
    os.mkdir(file_path)
    return file_path

if __name__ == '__main__':
    downloadHtml()
