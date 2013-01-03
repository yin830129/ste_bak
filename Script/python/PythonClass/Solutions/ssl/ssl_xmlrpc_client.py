# ssl_xmlrpc_client.py
#
# An XML-RPC client that presents the remote server with client
# certificates for authentication.

from xmlrpclib import SafeTransport, ServerProxy

KEYFILE = "privkeys/guido_rsa"        # Private key of the client
CERTFILE = "certs/guido.crt"          # Signed certificate of the client

# To present client certificates on the connect, you need to subclass
# SafeTransport and have it present addition arguments to the HTTPs
# constructor.   It somewhat obscure, but if you present a (host, dict)
# tuple to the make_connection() method, it treats the extra dictionary
# as keyword arguments to to the httplib.HTTPS() constructor.  We use
# this to pass the key and cert files.
class CertSafeTransport(SafeTransport):
    def __init__(self,keyfile,certfile):
        SafeTransport.__init__(self)
        # A dictionary of extra keyword arguments to pass to HTTPS
        self.__https_args = {
            'key_file' : keyfile,
            'cert_file' : certfile
            }
    def make_connection(self,host):
        # Calls the original method but passes a dictionary of other arguments
        # to set up the SSL credentials
        return SafeTransport.make_connection(self,(host,self.__https_args))

# Create the client proxy
proxy = ServerProxy("https://localhost:15000", 
                    transport=CertSafeTransport(KEYFILE,CERTFILE),
                    allow_none=True)

# Try some commands
print "Saving foo='bar'"
proxy.save("foo","bar")
print "Loading foo"
r = proxy.load("foo")
print "Got", repr(r)

