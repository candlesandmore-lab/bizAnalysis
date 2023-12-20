from BaseEntities.LoggingEntity import LoggingEntity

class SimulatorCore(LoggingEntity):

    def __init__(self, runDir, version="0.1"):
        
        super().__init__(runDir=runDir, name="simulator", version=version)
        return
    

