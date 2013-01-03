# ssl_server1.py
#
# An example of a simple SSL server.  To test, run ssl_client1.py

import socket
import ssl

KEYFILE = "privkeys/acme_rsa"           # The private key
CERTFILE = "certs/acme.crt"      # The certificate file

def run_server(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(address)
    s.listen(1)
    
    # Wrap with an SSL layer
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True, ssl_version=ssl.PROTOCOL_SSLv23)

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



