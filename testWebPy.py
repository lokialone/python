import web

urls = (
    '/index','index'
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index:
    def GET(self, name):
        return open('index.html','r').read()
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
