import os, fnmatch

"""def filter(toFilter):
    for i in toFilter:
        if i == ".DS_Store":
            print("here")
            toFilter.remove(i)
        return toFilter
"""

def readFiles():
    allText = ""
    fileList = []
    dirs1 = os.listdir("noTags")
    for i in dirs1:
        pathPt1 = i
        foldName1 = "./noTags/" + i
        if os.path.isdir(foldName1):
            dirs2 = os.listdir(foldName1)
            for j in dirs2:
                pathPt2 = pathPt1 + '/' + j
                foldName2 = foldName1 + '/' + j
                if os.path.isdir(foldName2):
                    dirs3 = os.listdir(foldName2)
                    pattern = "*.txt"
                    for k in dirs3:
                        if fnmatch.fnmatch(k, pattern):
                            pathPt3 = pathPt2 + '/' + k
                            fileList.append(pathPt3)
    return fileList
