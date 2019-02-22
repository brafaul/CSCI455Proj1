#Name: proj1.py
#Project: Project 1 CSCI 455
#Authors: Brayden Faulkner and Christina Hinton

import os, fnmatch, bs4, string, nltk

def filter(toFilter):
    for i in toFilter:
        if i == ".DS_Store":
            toFilter.remove(i)
    return toFilter

class wordTrack:
    def __init__(self, wordAdd, wordNum):
        self.word = wordAdd
        self.num = int(wordNum)
    def __lt__(self, other):
        return self.num < other.num
    def __repr__(self):
        return (self.word + " : " + str(self.num))
    def __str__(self):
        return (self.word+ " : " + str(self.num))


tokens = []
porter = nltk.stem.PorterStemmer()
dirs1 = filter(os.listdir("webkb"))
allText = ""
if os.path.isdir('./noTags') == False:
    os.mkdir('./noTags')
stopFile = open("stopWords.txt", 'r')
tempStop = stopFile.read()
stopWords = set(tempStop.split())
stopFile.close()
table = str.maketrans({key: " " for key in string.punctuation})
for i in dirs1:
    pathPt1 = "./noTags/" + i
    if os.path.isdir(pathPt1) == False:
        os.mkdir(pathPt1)
    foldName1 = "webkb/" + i
    dirs2 = filter(os.listdir(foldName1))
    for j in dirs2:
        pathPt2 = pathPt1 + '/' + j
        if os.path.isdir(pathPt2) == False:
            os.mkdir(pathPt2)
        foldName2 = foldName1 + '/' + j
        fileList = filter(os.listdir(foldName2))
        pattern = "*.html"
        for k in fileList:
            if fnmatch.fnmatch(k, pattern):
                pathPt3 = pathPt2 + '/' + k
                f = open(foldName2 + '/' + k, "rb")
                tempCon = f.read().decode(errors='replace')
                soup = bs4.BeautifulSoup(tempCon, features="html.parser")
                text = soup.get_text()
                allText += ( " " + text)
                f.close()
                w = open(pathPt3, "w")
                w.write(text)
                w.close()
allText = allText.translate(table)
allText = allText.lower()
tokens = nltk.tokenize.word_tokenize(allText)
filteredTokens = []
for x in tokens:
    if x not in stopWords and x.isdigit() == False :
        x = porter.stem(x)
        filteredTokens.append(x)
freq = nltk.FreqDist(filteredTokens)
wordList = []
for key,val in freq.items():
    wordList.append(wordTrack(str(key), str(val)))
wordList = sorted(wordList)
for x in wordList:
    print(x)
