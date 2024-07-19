import logging
from utilities.readProperties import ReadConfig

class LogGen:
    @staticmethod
    def loggen():
        basePath = ReadConfig.basePath()
        file = basePath + "/Logs/TestStepLog.log"
        print("############# " + file)
        logging.basicConfig(filename=file,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
