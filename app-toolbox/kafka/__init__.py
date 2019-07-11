
try:
	from KafkaAgent import *
except ImportError: # python3 support
	from .KafkaAgent import *
    
