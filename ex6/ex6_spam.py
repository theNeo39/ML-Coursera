## Machine Learning Online Class
#  Exercise 6 | Spam Classification with SVMs
#
#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  exercise. You will need to complete the following functions:
#
#     gaussianKernel.m
#     dataset3Params.m
#     processEmail.m
#     emailFeatures.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
import numpy as np
import scipy.io
from sklearn import svm
from processEmail import processEmail
from emailFeatures import emailFeatures
from getVocabList import getVocabList
from collections import OrderedDict

## ==================== Part 1: Email Preprocessing ====================
print('Preprocessing sample email (emailSample1.txt)')

# Extract Features
file = open('emailSample1.txt', 'r')
file_contents = file.readlines()
word_indices  = processEmail(''.join(file_contents))
# Print Stats
print('Word Indices: ')
print(word_indices)

## ==================== Part 2: Feature Extraction ====================
#  Now, you will convert each email into a vector of features in R^n.
#  You should complete the code in emailFeatures.m to produce a feature
#  vector for a given email.
print('Extracting features from sample email (emailSample1.txt)')
features = emailFeatures(word_indices)

# Print Stats
print('Length of feature vector: %d'% features.size)
print('Number of non-zero entries: %d'% sum(features > 0))

## =========== Part 3: Train Linear SVM for Spam Classification ========
#  In this section, you will train a linear classifier to determine if an
#  email is Spam or Not-Spam.
# Load the Spam Email dataset
# You will have X, y in your environment
dt = scipy.io.loadmat('spamTrain.mat')
X = dt['X']
y = dt['y'].flatten()

print('Training Linear SVM (Spam Classification)')

C =0.1
clf = svm.SVC(C=C, kernel='linear')
model = clf.fit(X, y)
pred = model.predict(X)

print('Training Accuracy: %f', np.mean(pred == y) * 100)

## =================== Part 4: Test Spam Classification ================

dat = scipy.io.loadmat('spamTest.mat')
Xtest = dat['Xtest']
ytest = dat['ytest']


print('Evaluating the trained Linear SVM on a test set ...')
p = model.predict(Xtest)
print('Test Accuracy: %f', np.mean(p == ytest) * 100)

"""
## ================= Part 5: Top Predictors of Spam ====================
#  Since the model we are training is a linear SVM, we can inspect the
#  weights learned by the model to understand better how it is determining
#  whether an email is spam or not. The following code finds the words with
#  the highest weights in the classifier. Informally, the classifier
#  'thinks' that these words are the most likely indicators of spam.
#

# Sort the weights and obtain the vocabulary list

t = sorted(list(enumerate(model.coef_[0])),key=lambda e: e[1], reverse=True)
d = OrderedDict(t)
idx = d.keys()
weight = d.values()
vocabList = getVocabList()
print('Top predictors of spam: ')
for i in range(15):
    print(' %s %f' % (vocabList[idx[i]], weight[i]))
print 'Program paused. Press enter to continue.'

## =================== Part 6: Try Your Own Emails =====================
#  Now that you've trained the spam classifier, you can use it on your own
#  emails! In the starter code, we have included spamSample1.txt,
#  spamSample2.txt, emailSample1.txt and emailSample2.txt as examples.
#  The following code reads in one of these emails and then uses your
#  learned SVM classifier to determine whether the email is Spam or
#  Not Spam

# Set the file to be read in (change this to spamSample2.txt,
# emailSample1.txt or emailSample2.txt to see different predictions on
# different emails types). Try your own emails as well!
filename = 'spamSample1.txt'

# Read and predict

file = open(filename)
file_contents = file.readlines()
word_indices = processEmail(''.join(file_contents))
x = emailFeatures(word_indices)
p = model.predict(x)

print 'Processed %s\n\nSpam Classification: %d' % (filename, p)
print(1 indicates spam, 0 indicates not spam)
"""