# k-nearest neighbors

### Input Parameters ###
trainingFile = "zip.train"
testFile = "zip.test"
k = 3

### Global Variables ###
trainingPoints = []

# Read files and split data by line
def readFile (filename):
    info = []
    with open(filename, 'r') as openFile:
        data = openFile.readlines()
        for line in data:
            info.append(line.split())
    return info

def extractTraining(info):
    for line in info:
        pixels = []
        for pixel in line:
            pixels.append(pixel)
        trainingPoints.append(pixels)

def printPoints(start, end):
    for i in range(start, end):
        print trainingPoints[i]

extractTraining(readFile(trainingFile))
