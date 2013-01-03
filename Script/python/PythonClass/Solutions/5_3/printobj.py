# printobj.py

def print_objects(objects,attrs):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    for aname in attrs:
        print "%10s" % aname,
    print
    print ("-"*10 + " ")*len(attrs)
    for obj in objects:
        for aname in attrs:
            print "%10s" % getattr(obj,aname,"UNDEF"),
        print
