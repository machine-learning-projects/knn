# k-nearest neighbors
# tailored to work on numbers represented by 256 values

import math
from operator import itemgetter

### Input Parameters ###
trainingFile = "zip.train"
testFile = "zip.test"
k = 3

### Global Variables ###
trainingPoints = []
testPoints = []

# Read files and split data by line
# params:
# filename
# returns: list with each line in file
def readFile (filename):
    info = []
    with open(filename, 'r') as openFile:
        data = openFile.readlines()
        for line in data:
            info.append(line.split())
    return info

# Extract each number
# params:
# info - list of training point strings
# returns: list with training points
def extractData(info):
    data = []
    for line in info:
        pixels = []
        # Each number is represented by a set of 256 values
        for pixel in line:
            pixels.append(pixel)
        data.append(pixels)
    return data

# Print input training points
# params:
# start, end - indexes for range to print
def printPoints(start, end):
    for i in range(start, end):
        print trainingPoints[i]

# Similarity given by ||x_test - x_train||
# params:
# a, b data points to compare
# start, end - indexes for dimensions to compare
# returns: euclidean distance between two points
def euclideanDistance(a, b, start, end):
    d = 0
    for i in range(start, end):
        d += pow((a[i] - b[i]), 2)
    d = math.sqrt(d)
    
    return d

# Finds k nearest neighbors
# params:
# testValue - value to test for
# k - number of neighbors to find
# start, end - indexes for training point range
# r1, r2 - indexes for dimensions to compare (for euclidean distance)
# returns: k nearest neighbors
def kNeighbors(testValue, k, start, end, r1, r2):
    distances = []
    for trainValue in trainingPoints[start:end]:
        distances.append([euclideanDistance(testValue, trainValue, r1, r2), trainValue])
    
    distances.sort(key = itemgetter(0))
    
    neighbors = []
    for neighbor in range(0, k):
        neighbors.append(distances[neighbor])
    
    return neighbors

trainingPoints = extractData(readFile(trainingFile))
testPoints = extractData(readFile(testFile))
