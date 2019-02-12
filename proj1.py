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
        self.num = wordNum
    def __lt__(self, other):
        return self.num < other.num
    def __repr__(self):
        return (self.word + " : " + self.num)
    def __str__(self):
        return (self.word+ " : " + self.num)

class wordList:
    def __init__(self):
        self.words = []
    def add(self, word2Check):
        if len(self.words) == 0:
            self.words.append(wordTrack(word2Check))
        else:
            found = False
            for i in self.words:
                if i.word == word2Check:
                    i.increase()
                    found = True
            if found == False:
                self.words.append(wordTrack(word2Check))
    def print(self):
        for i in self.words:
            print(i.word, i.num)
tokens = []
porter = nltk.stem.PorterStemmer()
dirs1 = filter(os.listdir("webkb"))
allWords = wordList()
allText = ""
#allWords = []
seperators = [' ', ',', '.', '?', '!', ':', '(', ')', '[', ']', ';', '@', '+', '-','"']
stopFile = open("stopWords.txt", 'r')
tempStop = stopFile.read()
stopWords = tempStop.split()
stopFile.close()
#print(stopWords)
table = str.maketrans({key: " " for key in string.punctuation})
for i in dirs1:
    pathPt1 = i
    foldName1 = "webkb/" + i
    dirs2 = filter(os.listdir(foldName1))
    for j in dirs2:
        pathPt2 = pathPt1 + '/' + j
        foldName2 = foldName1 + '/' + j
        fileList = filter(os.listdir(foldName2))
        pattern = "*.html"
        for k in fileList:
            if fnmatch.fnmatch(k, pattern):
                pathPt3 = pathPt2 + '/' + k
                #print(pathPt3)
                #print()
                f = open(foldName2 + '/' + k, "rb")
                tempCon = f.read().decode(errors='replace')
                soup = bs4.BeautifulSoup(tempCon)
                text = soup.get_text()
                allText += ( " " + text)
                #tokens += nltk.tokenize.word_tokenize(text)
                #for x in tempTokens:
                #    if x in stopWords:
                #        tempTokens.remove(x)
                #freq = nltk.FreqDist(tempTokens)
                #for key,val in freq.items():
                    #print(str(key) + ':' + str(val))
                #noPunct = text.translate(table)
                #allLower = noPunct.lower()
                #tempWords = allLower.split()
                #for x in tempWords:
                    #tempStem = porter.stem(x)
                    #print(tempStem)
                    #if tempStem not in stopWords:
                        #allWords.add(tempStem)
                f.close()
#tokens.sort()
allText = allText.translate(table)
allText = allText.lower()
tokens = nltk.tokenize.word_tokenize(allText)
for x in tokens:
    #if x in stopWords or x in string.punctuation:
    #    tokens.remove(x)
    #else:
    #    x = porter.stem(x)
    #    x = x.lower()
    #    print(x)
    x = porter.stem(x)
freq = nltk.FreqDist(tokens)
wordList = []
for key,val in freq.items():
    wordList.append(wordTrack(str(key), str(val)))
    #print(str(key) + ':' + str(val)
for x in wordList:
    print(x)
wordList.sort()
#print(wordList)
#for x in wordList
#allWords.print()
#for i in allWords:
    #print(i)
