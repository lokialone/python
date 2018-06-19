import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        print banner
        return banner
    except Exception, e:
        print "[-] Error = " + str(e)
        return

def main():
    ip = '192.168.1.9'
    port = 21
    retBanner(ip, port)

if __name__ == '__main__':
    main()
