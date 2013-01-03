# ssl_server.py
#
# An example of an SSL server

import socket
import ssl

def run_server(address,certfile):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(("",8080))
    s.listen(1)
    
    # Wrap with an SSL layer
    s_ssl = ssl.wrap_socket(s, certfile=certfile, server_side=True, ssl_version=ssl.PROTOCOL_SSLv23)

    # Wait for connections
    while True:
        try:
            c,a = s_ssl.accept()
            print "Got connection", c, a
            request = c.recv(8192)
            print request
            c.send(b"""HTTP/1.0 200 OK\r
Content-type: text/html\r\n\r

<HTML>
<BODY>
<H1>Hello World</H1>
</BODY>
</HTML>""")
            c.close()
        except Exception as e:
            print "%s: %s" % (e.__class__.__name__, e)


run_server(("",8080),"../../../Data/cert.pem")



