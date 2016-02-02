import logging

logging.debug("Contents of x: ".format(5))
logging.info("File saved successfully")
logging.warning("Missing required field 'age' - ignoring the person")
logging.error("Unable to load data file")
logging.critical("Unable to start the program! Aboring execution")