#!/usr/bin/env python2.7

import urllib2
import re
import itertools
import urlparse
import robotparser
import datetime
import time

#simple
def download(url,user_agent= 'wswp', proxy=None, num_retries=2):
    print 'Downloading:', url
    request = urllib2.Request(url, headers = {'User-agent': user_agent})
    opener = urllib2.build_opener()

    #add proxy
    if proxy:
        proxy_pramas = { urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_pramas))
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

# add a delay betweet downloads to the same domain
class Throttle:
    def __init__(self, delay):
        self.delay =  delay
        self.domains = {}

    def wait (self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        if (self.delay > 0 and last_accessed is not None):
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()

# link crawling
def link_crawler(seed_url, link_regex, max_depth=2):
    crawl_queue = [seed_url]
    # crawl_queue = Queue.deque([seed_url])
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    throttle = Throttle(1)
    while crawl_queue:
        url = crawl_queue.pop()
        throttle.wait(url)
        html = download(url)
        depth = seen[url]
        if depth != max_depth:
            for link in get_links(html):
                if re.search(link_regex, link):
                    link = urlparse.urljoin(seed_url, link)
                    if link not in seen:
                        seen[link] = depth + 1
                        crawl_queue.append(link)

    

# crawling on the basic of robot.txt
# it's not normal that every web site have robot.txt or sitemap
def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp



if __name__ == '__main__':
    # url = input("Input begin url: ")
    # crawl_sitemap('http://example.webscraping.com/sitemap.xml')
    # crawling_id();
    link_crawler('http://example.webscraping.com', '/(index|view)', 1)