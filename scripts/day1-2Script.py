#!/usr/bin/env python
import functions
import config as config
import math 

def massCalculate(moduleMass): 
    moduleMass = float(moduleMass)
    fuelMass=math.trunc(moduleMass/3) - 2
    if fuelMass > 0.0000000001: 
        fuelMass += massCalculate(fuelMass)
        print(fuelMass)
    else:
        fuelMass=0

    return fuelMass
    
massList = functions.readFile(config.dataPath + "day1Data", massCalculate)
#massTest = functions.readFile(config.dataPath + "day1-2Test", massCalculate)
massTotal= sum(massList)
print(massTotal)
#print(massTest)
