# ssl_server1.py
#
# An example of an SSL server that requires clients to present certificates
# signed by a trusted certificate authority.   Run ssl_client2.py to test.

import socket
import ssl

KEYFILE = "privkeys/acme_rsa"    # The private key of the server
CERTFILE = "certs/acme.crt"      # The certificate file of the server
CA_CERTS = "ca/ca.crt"           # Certificate of the certificate authority

def run_server(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(address)
    s.listen(1)
    
    # Wrap with an SSL layer requiring client certs
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, 
                            server_side=True, ssl_version=ssl.PROTOCOL_SSLv23,
                            cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs=CA_CERTS)

    print "Listening for connections on", address
    # Wait for connections
    while True:
        try:
            c,a = s_ssl.accept()
            print "Got connection", c, a
            # Send a greeting back
            c.send("Hello World")
            c.close()
        except Exception as e:
            print "%s: %s" % (e.__class__.__name__, e)

run_server(("",10000))



