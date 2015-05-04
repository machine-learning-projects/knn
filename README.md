# knn

kNN classifier for recognizing handwritten numerals.

Data is from the [Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/).
zip.train is used to train the classifier, zip.test is to test its performance.
Each contains 16x16-pixel grayscale images of the digits 0-9. There is one digit per row: the column corresponds to the number, the next 256 are the grayscale values.

For each given test point, the k training points with the smallest Euclidean distance are used as its nearest neighbors.
