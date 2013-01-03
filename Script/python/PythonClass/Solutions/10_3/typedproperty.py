# typedproperty.py

def typedproperty(name,expected_type):
    storage_name = "_" + name
    @property
    def prop(self):
        return getattr(self,storage_name)

    @prop.setter
    def prop(self,value):
        if not isinstance(value, expected_type):
            raise TypeError("Expected %s" % expected_type)
        setattr(self,storage_name,value)

    return prop

# Example
if __name__ == '__main__':
    class Stock(object):
        name = typedproperty("name",str)
        shares = typedproperty("shares",int)
        price = typedproperty("price", float)

        def __init__(self,name,shares,price):
            self.name = name
            self.shares = shares
            self.price = price

    

