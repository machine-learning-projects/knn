# k-nearest neighbors
# tailored to work on numbers represented by 256 values

import time
from operator import itemgetter

### Input Parameters ###
trainingFile = "zip.train"
testFile = "zip.test"

# Start / End dimensions
dimS = 1
dimE = 257

# Start / End training points
trainS = 0
trainE = 7292 # max of 7291 points for zip.train

# Start / End test points
testS = 0
testE = 2008 # max of 2007 for zip.test

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
    openFile.close()
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
        # find distance from test point to each training point
        distances.append([euclideanDistance(testValue, trainValue), trainValue[0], trainValue[dimS:dimE]])
    
    # sort to get nearest neighbors
    distances.sort(key = itemgetter(0))
    
    # return k nearest neighbors
    return distances[:k]

# Find closest match by majority
# params: testValue - value to search for
# returns: closest match 
def byMajority(testValue, k):
    count = dict()
    neighbors = kNeighbors(testValue, k)
    
    # Find count of neighbors with each value
    for neighbor in neighbors:
        # if already present, increment count
        if neighbor[1] in count:
            count[neighbor[1]] += 1
        else:
            # not present, add to dictionary
            count[neighbor[1]] = 1

    # return value with highest count            
    return max(count.iteritems(), key = itemgetter(1))[0]

# Find the percentage error of knn
# returns: percentage error
def checkError(k):
    incorrect = 0.0
    
    # subset of testpoints
    testSet = testPoints[testS:testE]
    
    # compare each test point value against its expected value
    for testPoint in testSet:
        if testPoint[0] != byMajority(testPoint, k):
            incorrect += 1
 
    # return (incorrect guesses / total number of trials)
    return (incorrect / len(testSet)) * 100

# Check error over a range of k's
# params: start, end - range of k
#        interval, every nth number is checked for k
# returns: list of error percentages [k, percentage]
def checkErrorRange(start, end, interval):
    errorRate = []
    ks = []
    
    print "k\tError(%)\tTime(s)"
    
    # select every nth k
    for i in range(start, end + 1):
        if i % interval != 0:
            ks.append(i);
    
    # for every value of k, check error %
    for k in ks:  
        intervalStart = time.clock()
        error = checkError(k)
        intervalEnd = time.clock()
        timeInterval = intervalEnd - intervalStart        
        
        print k, "\t", error, "\t\t", timeInterval
        errorRate.append([i, error, timeInterval])
     
    return errorRate

# read files
trainingPoints = extractData(readFile(trainingFile))
testPoints = extractData(readFile(testFile))

# Check Error for given: start/end k's, for every n k's
checkErrorRange(1, 1, 2)
