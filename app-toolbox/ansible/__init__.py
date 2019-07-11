
try:
	from AnsibleAgent import *
except ImportError: # python3 support
	from .AnsibleAgent import *
    
