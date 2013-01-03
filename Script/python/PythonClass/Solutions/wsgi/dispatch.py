# dispatch.py

from paste.urlmap import URLMap
from kvstore_webob import KVStore
from ctime_webob import time_application

def make_application():
    dispatcher = URLMap()
    dispatcher['/ctime'] = time_application
    dispatcher['/kv'] = KVStore()
    return dispatcher

# Run a reference implementation (for testing)
if __name__ == '__main__':
    app = make_application()
    
    # Run a simple server
    from paste.httpserver import serve
    serve(app,host="localhost",port=8080)
