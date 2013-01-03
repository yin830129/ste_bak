# ctime_wsgi.py
#
# An example of a simple time server

import time

def time_application(environ, start_response):
    headers = [ ('Content-type', 'text/plain') ]
    start_response("200 OK", headers)
    return [ time.ctime() ]

# Run a reference implementation (for testing)
if __name__ == '__main__':
    # Run a simple server
    from wsgiref import simple_server
    serv = simple_server.make_server("",8080,time_application)
    serv.serve_forever()

    
