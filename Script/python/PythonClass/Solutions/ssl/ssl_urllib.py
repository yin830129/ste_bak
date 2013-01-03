# ssl_urllib.py
#
# Example of presenting client certificates to servers via urllib.
# Source:  http://stackoverflow.com/questions/1875052/using-paired-certificates-with-urllib2

KEYFILE = "privkeys/guido_rsa"      # Private client key
CERTFILE = "certs/guido.crt"        # Client certificate

import urllib2, httplib
class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def __init__(self, key, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        return httplib.HTTPSConnection(host, key_file=self.key, cert_file=self.cert)

opener = urllib2.build_opener(HTTPSClientAuthHandler(KEYFILE, CERTFILE))
response = opener.open("https://localhost:8080/index.html")
print response.read()
