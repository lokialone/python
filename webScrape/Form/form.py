import urllib, urllib2, lxml.html, pprint
import cookielib
import glob
import os
import json

LOGIN_URL = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'

def parse_form(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data
    

def login_cookies():
    cj = cookielib.CookieJar()
    # add cookies
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    html = opener.open(LOGIN_URL).read()
    data = parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data = urllib.urlencode(data)
    print encoded_data
    request = urllib2.Request(LOGIN_URL, encoded_data)
    response = opener.open(request)
    print response.geturl()
    return opener

#load firefox cookies
def load_ff_sessions(session_filename):
    cj = cookielib.CookieJar()
    if os.path.exists(session_filename):
        try: 
            json_data = json.loads(open(session_filename, 'rb').read())
        except ValueError as e:
            print 'Error parsing session JSON:', str(e)
        else:
            print json_data 
    else:
        print 'Session filename does not exist:', session_filename

#can't use
def find_ff_sessions():
    #win mac win visita
    paths = [
        '~/.mozilla/firefox/*.default',
        '~/Library/Application Support/Firefox/Profiles/*.default',
        '%APPDATA%/Roaming/Mozilla/Firefox/Profiles/*.default'
    ]

    for path in paths:
        filename = os.path.join(path, 'sessionstore.js')
        print os.path.expanduser(filename)
        matches = glob.glob(os.path.expanduser(filename))
        # matches = glob.glob(filename)
        print matches
        if matches:
            print matches[0]
            return matches[0]


def login_firfox():
    session_filename = find_ff_sessions()
    # load_ff_sessions(session_filename)

if __name__ == '__main__':
    # login_cookies()
    # login_firfox()
