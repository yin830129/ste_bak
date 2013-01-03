# ssl_http_serv.py
#
# An example of an SSL HTTP server that requires clients to present certificates
# signed by a trusted certificate authority.   Run ssl_urllib.py to test.

import socket
import ssl

KEYFILE = "privkeys/acme_rsa"    # The private key of the server
CERTFILE = "certs/acme.crt"      # The certificate file of the server
CA_CERTS = "ca/ca.crt"           # Certificate of the certificate authority

# To incorporate SSL into the server, it needs to be subclasses and certain
# methods redefined.  The get_request() method is a low-level method that
# accepts client connections.  It's been modified to receive a client
# a connection and immediately wrap it with an SSL layer.   This isn't
# the only way to do this, but illustrates some of the difficulty involved

from BaseHTTPServer import HTTPServer
class SSLHTTPServer(HTTPServer):
    def get_request(self):
        client, addr = HTTPServer.get_request(self)
            # Wrap the client in an SSL layer
        client_ssl = ssl.wrap_socket(client, 
                                     keyfile=KEYFILE, 
                                     certfile=CERTFILE, 
                                     server_side=True, 
                                     ssl_version=ssl.PROTOCOL_SSLv23,
                                     cert_reqs=ssl.CERT_REQUIRED,
                                     ca_certs=CA_CERTS)
        return client_ssl, addr

from SimpleHTTPServer import SimpleHTTPRequestHandler

serv = SSLHTTPServer(("",8080),SimpleHTTPRequestHandler)
print "Secure Web running on port 8080"
serv.serve_forever()



