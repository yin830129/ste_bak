# kvstore_webob.py
#
# An example of a simple key-value store implemented using WSGI/WebOb

from webob import Request, Response
from webob.exc import HTTPNotFound

class KVStore(object):
    def __init__(self):
        self.store = {}

    def __call__(self, environ, start_response):
        req = Request(environ)
        if req.method == 'GET':
            res = self.do_get(req)
        else:
            res = self.do_post(req)
        return res(environ, start_response)

    def do_get(self, req):
        '''
        Return the value associated with a key.
        '''
        keyname = req.params['name']
        if keyname in self.store:
            return Response(content_type="text/plain",
                           text=self.store[keyname])
        else:
            return HTTPNotFound()

    def do_post(self, req):
        '''
        Store a value associated with a key.
        '''
        keyname = req.params['name']
        value   = req.params['value']
        self.store[keyname] = value
        return Response(content_type='text/plain',body="Success")

def test_kvstore(app):
    req = Request.blank("/?name=foo&value=bar")
    req.method = "POST"
    resp = req.get_response(app)
    print resp.status
    print resp.body

    req = Request.blank("/?name=foo")
    resp = req.get_response(app)
    print resp.status
    print resp.body
               
# Run a reference implementation (for testing)
if __name__ == '__main__':
    kvstore = KVStore()         
    test_kvstore(kvstore)

    # Run a simple server
    from wsgiref import simple_server
    serv = simple_server.make_server("",8080,kvstore)
    serv.serve_forever()

    
