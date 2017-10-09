#!/usr/bin/env python2.7

import urllib2
import re

#simple
def download(url,user_agent= 'wswp', num_retries=2):
    print 'Downloading:', url
    request = urllib2.Request(url, headers = {'User-agent': user_agent})
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Downloading error:', e.reason
        html = None
        if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    #recursively retry 5XX http errors
     
                   download(url, num_retries-1)
    # test
    # print html
    return html


#download html according to sitemap
def crawl_sitemap(url):
    #download the sitemap file
    sitemap = download(url)
    print sitemap
    #extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    print links
    #download each link
    for link in links:
        html = download(link)
        print html


if __name__ == '__main__':
    # url = input("Input begin url: ")
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')