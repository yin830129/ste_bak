# kvstore.py
#
# A simple key-value store using XML-RPC

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
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    serv = SimpleXMLRPCServer(("",15000),allow_none=True)
    serv.register_function(save)
    serv.register_function(load)
    serv.register_function(delete)
    serv.serve_forever()
