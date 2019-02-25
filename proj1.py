#Name: proj1.py
#Project: Project 1 CSCI 455
#Authors: Brayden Faulkner and Christina Hinton

import os, fnmatch, bs4, string, nltk

#remove .DS_Store from each directory
def filter(toFilter):
    for i in toFilter:
        if i == ".DS_Store":
            toFilter.remove(i)
    return toFilter

#update word frequency and add to wordList in correct format
class wordTrack:
    #param. constructor
    def __init__(self, wordAdd, wordNum):
        self.word = wordAdd
        self.num = int(wordNum)

    #sorting rule
    #return true if object's word frequency is less than rh object's
    def __lt__(self, other):
        return self.num < other.num

    #return object information
    def __repr__(self):
        return (self.word + " : " + str(self.num))
    
    def __str__(self):
        return (self.word+ " : " + str(self.num))

#list of words from file
tokens = []
#stemming method
porter = nltk.stem.PorterStemmer()

#remove .DS_Store from each directory
dirs1 = filter(os.listdir("webkb"))
allText = ""
if os.path.isdir('./noTags') == False:
    os.mkdir('./noTags')

#open stopwords.txt and get list of stop words
stopFile = open("stopWords.txt", 'r')
tempStop = stopFile.read()
stopWords = set(tempStop.split())
stopFile.close()
#establishes rule to translate all punctuation to whitespace
table = str.maketrans({key: " " for key in string.punctuation})

#go through directories
#remove html tags
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
        #establishes pattern to find all files that end in .html
        pattern = "*.html"
        for k in fileList:
            if fnmatch.fnmatch(k, pattern):
                pathPt3 = pathPt2 + '/' + k
                f = open(foldName2 + '/' + k, "rb")
                tempCon = f.read().decode(errors='replace')
                soup = bs4.BeautifulSoup(tempCon, features="html.parser")
                text = soup.get_text()
                allText += (text)
                f.close()
                #writes html free text to a file
                w = open(pathPt3, "w")
                w.write(text)
                w.close()

#separate each word from allText and move each to tokens[]               
allText = allText.translate(table)
allText = allText.lower()
tokens = nltk.tokenize.word_tokenize(allText)

#list of stemmed words
filteredTokens = []

#stem every word that is not a stop word
#add stemmed word to filteredTokens[]
for x in tokens:
    if x not in stopWords and x.isdigit() == False :
        x = porter.stem(x)
        filteredTokens.append(x)

#count frequency of each stemmed word       
freq = nltk.FreqDist(filteredTokens)
wordList = []

#for each pair in list of frequencies:
#add each pair to WordList[]
#this attaches the frequency (value) to the word (key)
for key,val in freq.items():
    wordList.append(wordTrack(str(key), str(val)))

#sort wordList[]
wordList = sorted(wordList)

#print results
for x in wordList:
   print(x)
#for x in range(-1,-200, -1):
#print(wordList[x])
print(len(wordList))
