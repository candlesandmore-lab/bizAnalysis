

from model.ModelCore import ModelCore
from simulator.SimulatorCore import SimulatorCore


def main():

    bizModel = {
        "runDir" : "C:/Users/Frank/SynologyDrive/Drive/LaptopOnly/github/bizAnalysis"
    }

    simulator = SimulatorCore(runDir=bizModel['runDir'])
    model = ModelCore(runDir=bizModel['runDir'])

if __name__ == "__main__":
    main()