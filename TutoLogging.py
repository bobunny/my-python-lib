import logging

#logging.basicConfig(filename='testlog.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(threadName)s - %(levelname)s %(message)s')

#logging.basicConfig(filename='demo.log',
#                   level=logging.DEBUG,
#                    format='%(asctime)s - %(name)s - %(threadName)s -  %(levelname)s - %(message)s')
#if __name__ == "__main__":
#    logging.warning("I'm a warning!") 

#logging.info("test info")
#logging.debug("test debug")

# logging_example.py



# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(f_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
logger.error('This is an error1')
logger.error('This is an error2')
logger.error('This is an error3')
logger.error('This is an error4')