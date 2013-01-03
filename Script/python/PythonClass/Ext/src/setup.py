# This script uses distutils to build a DLL on Unix systems.
# Type 'python setup.py build_ext --inplace' to build an .so file

from distutils.core import setup,Extension
setup(name="libmandel",
      ext_modules=[Extension("libmandel",[
                                        "mandel.c"])]
     )


                    
