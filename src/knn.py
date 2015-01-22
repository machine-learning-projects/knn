# k-nearest neighbors
# tailored to work on numbers represented by 256 values

import math

### Input Parameters ###
trainingFile = "zip.train"
testFile = "zip.test"
k = 3

### Global Variables ###
trainingPoints = []
testPoints = []

# Read files and split data by line
def readFile (filename):
    info = []
    with open(filename, 'r') as openFile:
        data = openFile.readlines()
        for line in data:
            info.append(line.split())
    return info

# Extract each number
def extractData(info):
    data = []
    for line in info:
        pixels = []
        # Each number is represented by a set of 256 values
        for pixel in line:
            pixels.append(pixel)
        data.append(pixels)
    return data

def printPoints(start, end):
    for i in range(start, end):
        print trainingPoints[i]

# Similarity given by ||x_test - x_train||
def euclideanDistance(a, b, start, end):
    d = 0
    for i in range(start, end):
        d += pow((a[i] - b[i]), 2)
    d = math.sqrt(d)
    return d



trainingPoints = extractData(readFile(trainingFile))
testPoints = extractData(readFile(testFile))
