# ssl_client1.py
#
# An example of an SSL client that authenticates the server

CA_CERTS = "ca/ca.crt"         # Certificate of CA authority

# CA_CERTS = "certs/acme.crt"  # An untrusted certificate.  Uncomment and watch it fail

from socket import *
import ssl

s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost",10000))

# Wrap with an SSL layer and required the server to be authenticated
ssl_s = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs=CA_CERTS)

# Read the greeting back
data = ssl_s.recv(8192)
print data

