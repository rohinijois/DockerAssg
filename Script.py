import os
import socket
from collections import Counter

Counter = Counter()

def getMyIPAdress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

def getNumberOfWords(file):
    wordcount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                wordcount = wordcount + len(line.replace("Â", "").split())
    return wordcount

FilesWordCounts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
outputString="File at location: /home/data: \n"

for eachFile in os.listdir(path):
    if eachFile.endswith(".txt"):
        outputString=outputString+eachFile+"\n"
        FilesWordCounts[eachFile] = getNumberOfWords(path + "/" + eachFile)
        
outputString=outputString+"\n"

TotalWordCount = 0
AllFilesNames = ""
for eachkey in FilesWordCounts.keys():
    AllFilesNames = AllFilesNames + eachkey + ","
    TotalWordCount = TotalWordCount + FilesWordCounts.get(eachkey)
    outputString = outputString +"total number of words in [" + eachkey + "] is : " + str(FilesWordCounts.get(eachkey))+"\n"
    
outputString = outputString +"\n"

outputString = outputString +"Total number of words in both files [" + AllFilesNames[0:len(AllFilesNames) - 1] + "] is: " + str(TotalWordCount)+"\n"
outputString = outputString +"\n"

outputString = outputString +"Top 3 words with maximum number of counts in IF.txt: \n"
outputString = outputString +str(Counter.most_common(3))+"\n"

outputString = outputString +"\n"
outputString = outputString +"IP Address is:" + getMyIPAdress()

resultFile = open(path + "/" +"result.txt","w")
resultFile.write(outputString)
resultFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))
