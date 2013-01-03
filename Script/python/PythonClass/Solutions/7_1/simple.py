# simple.py

def add(x,y):
    """Adds x and y together.  For example:

       >>> add(2,3)
       5
       >>> add("Hello","World")
       'HelloWorld'
       >>> add(2.1,3.4)
       5.5
       >>>
    """
    return x+y

def sub(x,y):
    """Subtracts y from x.  For example:

       >>> sub(3,2)
       1
       >>> sub(2.6,1.1)
       1.5
       >>>
    """
    return x-y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
