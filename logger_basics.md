import logging
import logging.config

logging.config.fileConfig('logging.conf')

# IMP, ROOT logger gets set at module level and if you import then it won't get overwritten.
# hence it's not a good practice to share the root logger. To get new logger for each module
# get better config with the logger name.
# this creates a new logger for the module with the name of the module '__name__'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# get the formatter in place
formatter = logging.Formatter('%(asctime)s: %(levelname)s >> %(message)s')
# to specify and log to a file you have to use a "file handler"
file_handler = logging.FileHandler("logs/sandbox.log")
file_handler.setLevel(logging.ERROR)
# then we add the formatting to the file handler and not the logger
file_handler.setFormatter(formatter)
# then add the file handler to the logger:
logger.addHandler(file_handler)