#!/usr/bin/env python

import functions
import config as config
import math 

def intCodeProcess(opCodeString):
    opCodeRawList=opCodeString[0].split(",")
    opCodeList = []
    
    for i in range(len(opCodeRawList)):
        opCodeList.append(int(opCodeRawList[i]))

    return opCodeList

def intCodeRun(opCodeList):
    for i in range(0, len(opCodeList), 4): 
                
        if opCodeList[i] == 1:
            first_int = opCodeList[opCodeList[i+1]]
            second_int = opCodeList[opCodeList[i+2]]
            pos = opCodeList[i+3]
            
            opCodeList[pos]=first_int + second_int
            
        elif opCodeList[i] == 2: 
            first_int = opCodeList[opCodeList[i+1]]
            second_int = opCodeList[opCodeList[i+2]]
            pos = opCodeList[i+3]
            
            opCodeList[pos]=first_int * second_int

        elif opCodeList[i] == 99: 
            print("99 detected, exiting now.")
            break

    return opCodeList[0]

opCodeRawList = functions.readFile(config.dataPath + "day2-1Data", str)
opCodeList = intCodeProcess(opCodeRawList)
result = intCodeRun(opCodeList)
print(result)
