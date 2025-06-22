import numpy as np
import pandas as pd
from numpy.linalg import svd
from numpy.linalg import norm
from sklearn.metrics import accuracy_score

#read the matrices and digits and assign them to a variable
traindig = np.load('HandwrittenDigits/TrainDigits.npy')
testdig = np.load('HandwrittenDigits/TestDigits.npy')

trainlab = np.load('HandwrittenDigits/TrainLabels.npy')
testlab = np.load('HandwrittenDigits/TestLabels.npy')

r, c = trainlab.shape

#function that outputs the index of a given digit with given number of integers wanted from train labels
def imdig(dig, num):
    count = []
    for i in range(c):
        if trainlab[:, i][0] == dig:
            count.append(i)
        elif len(count) > num - 1:
            break
    return count

#matrices with the index from label set
matrices = {}
for i in range(10):
    matrices.update({i: traindig[:, imdig(i, 300)]})

#svd for the matrices from the train digits
lsing = {}
singmat = {}
rsing = {}
for i in range(10):
    u, s, v = svd(matrices[i], full_matrices=False)
    lsing[i] = u
    singmat[i] = s
    rsing[i] = v

#calculate the residual and find the minimum residual
Identity = np.eye(testdig.shape[0])
predictions = np.empty((testlab.shape[1], 0))
ks = np.arange(1, 15)
for k in list(ks):
    prediction = []
    for i in range(testlab.shape[1]):
        residuals = []
        for j in range(10):
            u = lsing[j][:, 0:k]
            residuals.append(norm(np.dot(Identity-np.dot(u, u.T), testdig[:, i])))
        indexm = np.argmin(residuals)
        prediction.append(indexm)
    prediction = np.array(prediction)
    predictions = np.hstack((predictions, prediction.reshape(-1, 1)))

scores = []
for i in list(ks):
    score = accuracy_score(testlab[0, :], predictions[:, i])
    scores.append(score)

datt = {"Number of k": list(ks), "Accuracy": scores}
data = pd.DataFrame(datt).set_index("Number of k")
print(data)