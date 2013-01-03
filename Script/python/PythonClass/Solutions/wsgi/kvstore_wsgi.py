# kvstore_wsgi.py
#
# An example of a simple key-value store implemented using WSGI

import cgi

class KVStore(object):
    def __init__(self):
        self.store = {}

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'GET':
            return self.do_get(environ, start_response)
        else:
            return self.do_post(environ, start_response)

    def do_get(self, environ, start_response):
        '''
        Return the value associated with a key.
        '''
        fields = cgi.FieldStorage(environ['wsgi.input'],
                              environ=environ)
        keyname = fields.getvalue('name')
        headers = [ ('Content-type','text/plain') ]
        if keyname in self.store:
            start_response("200 OK", headers)
            return [self.store[keyname]]
        else:
            start_response("404 NOT FOUND", headers)
            return [ "Not Found" ]

    def do_post(self, environ, start_response):
        '''
        Store a value associated with a key.
        '''
        fields = cgi.FieldStorage(environ['wsgi.input'],
                              environ=environ)
        keyname = fields.getvalue("name")
        value = fields.getvalue("value")
        self.store[keyname] = value
        headers = [ ('Content-type','text/plain') ]
        start_response("200 OK", headers)
        return ["Success"]
               
# Run a reference implementation (for testing)
if __name__ == '__main__':
    kvstore = KVStore()     

    import webbrowser
    import os
    webbrowser.open("file://"+os.path.abspath("kvstore_wsgi.html"))

    # Run a simple server
    from wsgiref import simple_server
    serv = simple_server.make_server("",8080,kvstore)
    serv.serve_forever()

    
