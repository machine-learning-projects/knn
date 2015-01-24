# k-nearest neighbors
# tailored to work on numbers represented by 256 values

import time
from operator import itemgetter

### Input Parameters ###
trainingFile = "zip.train"
testFile = "zip.test"

dimS = 1
dimE = 257

trainS = 0
trainE = 7292

### Global Variables ###
trainingPoints = []
testPoints = []

# Read files and split data by line
# params: filename
# returns: list with each line in file
def readFile (filename):
    info = []
    with open(filename, 'r') as openFile:
        data = openFile.readlines()
        for line in data:
            info.append(line.split())
    return info

# Extract each number
# params: info - list of training point strings
# returns: list with training points
def extractData(info):
    data = []
    for line in info:
        pixels = []
        # Each number is represented by a set of 256 values
        for pixel in line:
            pixels.append(float(pixel))
        data.append(pixels)
    return data

# Print input training points
# params: start, end - indexes for range to print
def printPoints(start, end):
    for i in range(start, end):
        print trainingPoints[i]

# Similarity given by ||x_test - x_train||
# params: a, b data points to compare
# returns: euclidean distance between two points
def euclideanDistance(a, b):
    d = 0
    for i in range(dimS, dimE):
        d += abs(a[i] - b[i])

    return d

# Finds k nearest neighbors
# params: testValue - value to test for
# returns: k nearest neighbors [value, distance, [dimensions]
def kNeighbors(testValue, k):
    distances = []
    for trainValue in trainingPoints[trainS:trainE]:        
        distances.append([euclideanDistance(testValue, trainValue), trainValue[0], trainValue[dimS:dimE]])
    
    distances.sort(key = itemgetter(0))
    
    neighbors = []
    for neighbor in range(0, k):
        neighbors.append(distances[neighbor])
    
    return neighbors

# Find closest match by majority
# params: testValue - value to search for
# returns: closest match 
def byMajority(testValue, k):
    count = dict()
    neighbors = kNeighbors(testValue, k)
    
    # Find count of neighbors with each value
    for neighbor in neighbors:
        if neighbor[1] in count:
            count[neighbor[1]] += 1
        else:
            count[neighbor[1]] = 1
            
    return max(count.iteritems(), key = itemgetter(1))[0]

# Find the percentage error of knn
# returns: percentage error
def checkError(k):
    incorrect = 0.0
    
    for testPoint in testPoints:
        if testPoint[0] != byMajority(testPoint, k):
            incorrect += 1
 
    return (incorrect / len(testPoints)) * 100

# Check error over a range of k's
# params: start, end - range of k
#        interval, every nth number is checked for k
# returns: list of error percentages [k, percentage]
def checkErrorRange(start, end, interval):
    errorRate = []
    ks = []
    
    for i in range(start, end + 1):
        if i % interval != 0:
            ks.append(i);
    
    for k in ks:  
        intervalStart = time.clock()        
        error = checkError(k)
        intervalEnd = time.clock()
        timeInterval = intervalEnd - intervalStart
        
        print k, error, timeInterval
        errorRate.append([i, error, timeInterval])
     
    return errorRate

trainingPoints = extractData(readFile(trainingFile))
testPoints = extractData(readFile(testFile))

# print checkError()
print checkErrorRange(1, 25, 2)
