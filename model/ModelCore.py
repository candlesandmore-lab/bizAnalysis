from BaseEntities.LoggingEntity import LoggingEntity

class ModelCore(LoggingEntity):

    def __init__(self, runDir, version="0.1"):
        
        super().__init__(runDir=runDir, name="model", version=version)
        return
    

