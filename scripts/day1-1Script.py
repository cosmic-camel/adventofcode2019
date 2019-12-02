#!/usr/bin/env python
import functions
import config as config
import math 

def massCalculate(moduleMass): 
    moduleMass = float(moduleMass)
    fuelMass=math.trunc(moduleMass/3) - 2 
    return fuelMass
    
massList = functions.readFile(config.dataPath + "day1Data", massCalculate)
massTotal= sum(massList)
print(massTotal)
