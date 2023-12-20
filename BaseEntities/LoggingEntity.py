import os
import logging

class LoggingEntity:

    def __init__(self, runDir, name, version="0.1"):
        
        self.runDir = runDir
        self.name = name
        self.logDir = "{}/logs".format(
            self.runDir
        )

        if not os.path.exists(self.logDir):
            os.mkdir(self.logDir)

        self.setupLogger()

        return
    

    def setupLogger(self):
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)

        # configure the handler and formatter for self.logger
        self.handler = logging.FileHandler(
            "{}/{}.log".format(
                self.logDir,
                self.name
            ), 
            mode='w')
        self.formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

        # add formatter to the handler
        self.handler.setFormatter(self.formatter)
        # add handler to the logger
        self.logger.addHandler(self.handler)

        self.logger.info("Initialized [{}].".format(
            self.name
        ))