import inspect
import logging
class LogGenerator:
    @staticmethod
    def custom_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(".\\Logs\\automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        #logging.basicConfig(filename="automation.log",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger


