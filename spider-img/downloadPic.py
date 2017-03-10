#-*- coding:utf-8 -*-
import re
import requests
import os

root_path = '/Users/lokalone/code/tech/python/python/assets/'
def downloadPic(html,path):
    pic_urls = re.findall('"image":"(.*?)",',html,re.S)
    i = 0
    os.chdir(path)
    for each in pic_urls:
        pic_url = 'http://dynasty-scans.com/' + each
        pic= requests.get(pic_url)
        string = '_' + str(i) + '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

def createDir(url):
    file_name = url.split("/")[-1]
    file_path = root_path + file_name
    os.mkdir(file_path)
    return file_path

if __name__ == '__main__':
    url = raw_input("Input begin url: ")
    file_path = createDir(url)
    result = requests.get(url)
    downloadPic(result.text,file_path)
