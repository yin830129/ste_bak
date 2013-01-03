# ssl_xmlrpc_server.py
#
# An example of an SSL-XMLRPC Server. The server presents a certficate
# signed by a trusted CA and requires all clients to present certificates
# signed by the same CA.

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
    KEYFILE="privkeys/acme_rsa"         # Private key of the server
    CERTFILE="certs/acme.crt"           # Signed certificate of server
    CA_CERTS = "ca/ca.crt"              # Certificate of trusted CA

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
            client_ssl = ssl.wrap_socket(client, 
                                         keyfile=KEYFILE, 
                                         certfile=CERTFILE, 
                                         server_side=True, 
                                         ssl_version=ssl.PROTOCOL_SSLv23,
                                         cert_reqs=ssl.CERT_REQUIRED,
                                         ca_certs=CA_CERTS)
            return client_ssl, addr

    serv = SSLSimpleXMLRPCServer(("",15000),allow_none=True)
    serv.register_function(save)
    serv.register_function(load)
    serv.register_function(delete)
    serv.serve_forever()
