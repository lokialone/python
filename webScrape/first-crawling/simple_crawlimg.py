#!/usr/bin/env python2.7

import urllib2

def download(url):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Downloading error:', e.reason
        html = None
    print html
    return html

if __name__ == '__main__':
    url = input("Input begin url: ")
    download(url)