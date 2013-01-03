# ssl_xmlrpc.py
#
# An example of an SSL-XMLRPC Server

# Internal dictionary that stores the actual data
_store = {}

# Functions that save, load, and delete contents
def save(key,value):
    _store[key] = value

def load(key):
    return _store.get(key,None)

def delete(key):
    if key in _store:
        del _store[key]


if __name__ == '__main__':
    KEYFILE="../../../Data/cert.pem"
    CERTFILE="../../../Data/cert.pem"

    from SimpleXMLRPCServer import SimpleXMLRPCServer
    import ssl

    # To incorporate SSL into the server, it needs to be subclasses and certain
    # methods redefined.  The get_request() method is a low-level method that
    # accepts client connections.  It's been modified to receive a client
    # a connection and immediately wrap it with an SSL layer.   This isn't
    # the only way to do this, but illustrates some of the difficulty involved
    class SSLSimpleXMLRPCServer(SimpleXMLRPCServer):
        def get_request(self):
            client, addr = SimpleXMLRPCServer.get_request(self)
            # Wrap the client in an SSL layer
            client_ssl = ssl.wrap_socket(client, keyfile=KEYFILE, certfile=CERTFILE, server_side=True, ssl_version=ssl.PROTOCOL_SSLv23)
            return client_ssl, addr

    serv = SSLSimpleXMLRPCServer(("",15000),allow_none=True)
    serv.register_function(save)
    serv.register_function(load)
    serv.register_function(delete)
    serv.serve_forever()
