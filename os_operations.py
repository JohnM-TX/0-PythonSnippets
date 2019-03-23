import os

os.listdir()
path = os.path.dirname(os.path.abspath(filename))

from glob import glob



# memory usage

import sys

# These are the usual ipython objects, including this one you are creating
ipython_vars = ['In', 'Out', 'exit', 'quit', 'get_ipython', 'ipython_vars']

# Get a sorted list of the objects and their sizes
sorted([(x, sys.getsizeof(globals().get(x))) for x in dir() if not 
    x.startswith('_') and x not in sys.modules and x 
    not in ipython_vars], key=lambda x: x[1], reverse=True)
    
    
    
 #enable local imports
 
import os, sys, inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"keras-deeplab-v3-plus")))
if cmd_subfolder not in sys.path:
     sys.path.insert(0, cmd_subfolder)



# easier imports 
import sys
sys.path.append('./keras-yolo3-master')



#


