# fieldparse.py

def parse(lines,types,names=None,sep=None):
    '''
    Parse a line of column oriented data into a list of dictionaries
    or tuples with type conversion.
    '''
    records = []
    for lineno, line in enumerate(lines,1):
        # Strip whitespace and ignore blank lines
        line = line.strip()
        if line == '':
            continue

        fields = line.split(sep)
        
        # Get rid of double quotes
        fields = [f.strip('"') for f in fields]
        
        try:
            # Apply type conversion to the fields 
            cfields = [converter(value) for converter,value in zip(types,fields)]
        except ValueError as e:
            print "Line %d: Couldn't parse: %s" % (lineno, line)
            print "Line %d: Reason %s" % (lineno, e)
            continue

        # Optionally turn into a dictionary of named fields
        if names is not None:
            record = dict(zip(names,cfields))
        else:
            record = tuple(cfields)

        # Save the record
        records.append(record)

    return records