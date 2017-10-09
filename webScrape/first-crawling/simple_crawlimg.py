#!/usr/bin/env python2.7

import urllib2
import re
import itertools
import urlparse

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
    # print sitemap
    #extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # print links
    #download each link
    for link in links:
        html = download(link)
        print html


# download html according to id
def crawling_id():
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/%d' % page
        html = download(url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                break
        else:
            num_errors = 0

# return a list of links from html
def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)             


# link crawling
def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.search(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                print link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


if __name__ == '__main__':
    # url = input("Input begin url: ")
    # crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    # crawling_id();
    link_crawler('http://example.webscraping.com', '/(index|view)')