#Name: proj2.py
#Project CSCI 455
#Authors: Brayden Faulkner and Christinia Hinton

import os, fnmatch, bs4, string, nltk, numpy

import fileRead


f = open('topThou.txt', 'r')
text = f.read()
f.close()
words = text.split()
print(words)
fileList = fileRead.readFiles()
fileList = [" "] + fileList 
matrix = []
matrix.append(fileList)
for i in words:
    matrix.append([i])
print(numpy.matrix(matrix))
