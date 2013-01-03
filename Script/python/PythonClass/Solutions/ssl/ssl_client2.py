# ssl_client2.py
#
# An example of an SSL client that authenticates the server and presents
# the server with a signed user certificate

KEYFILE = "privkeys/guido_rsa"    # User private key
CERTFILE = "certs/guido.crt"      # User signed certificate
CA_CERTS = "ca/ca.crt"            # Certificate of CA authority

#CERTFILE = "certs/larry.crt"     # Uncomment to see a bad authentication

from socket import *
import ssl

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost",10000))

# Wrap with an SSL layer and required the server to be authenticated
ssl_s = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE,
                        cert_reqs=ssl.CERT_REQUIRED, ca_certs=CA_CERTS)

# Read the greeting back
data = ssl_s.recv(8192)
print data

