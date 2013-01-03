# findgen.py
#
# An example of setting up a processing pipeline with coroutines


def findstr(text,substr,target):
    '''
    Emit the locations of a substring to a target
    '''
    index = 0
    while index >= 0:
        index = text.find(substr,index)
        if index > 0:
            target.send(index)
            index += len(substr)

def replacestr(text,substr,repstr,target):
    '''
    Emit chunks of text with a replaced substring.
    '''
    index = 0
    while True:
        n = yield
        target.send(text[index:n])
        target.send(repstr)
        index = n + len(substr)
    target.send(text[index:])

def write_chunks(outf):
    '''
    Write chunks of text to a file object
    '''
    while True:
        chunk = yield
        outf.write(chunk)

if __name__ == '__main__':
    import sys

    text = '''
Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes,
not around the eyes, 
don't look around the eyes,
look into my eyes, you're under.
'''

    writer = write_chunks(sys.stdout)
    writer.next()
    replacer = replacestr(text,"eyes","nose",writer)
    replacer.next()
    findstr(text,"eyes",replacer)
