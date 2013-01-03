# ctime_webob.py
#
# An example of a simple time server

import time
from webob import Response

def time_application(environ, start_response):
    res = Response(content_type="text/plain", body = time.ctime())
    return res(environ, start_response)

# Run a reference implementation (for testing)
if __name__ == '__main__':
    # Run a simple server
    from wsgiref import simple_server
    serv = simple_server.make_server("",8080,time_application)
    serv.serve_forever()

    
