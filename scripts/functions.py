#!/usr/bin/env python

def readFile(dataFile, modification=float):
    lines=[]
    f = open(dataFile, "r")
    with f as tempFile:
        for line in tempFile:
            line = line.strip()
            line = modification(line)
            lines.append(line)
            
    return lines