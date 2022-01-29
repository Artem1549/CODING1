
from operator import truediv
import sys

print("Please enter the text file to be cheched, then the name of the file with the correct text, and the dictionary.")
print("Separate the file names with one space only.")

wrongText = sys.argv[1]
correctText = sys.argv[2]
dictionary = sys.argv[3]

dictionaryList = [] 
with open(str(dictionary),'r') as text:
    for line in text:
        for word in line.split():
            dictionaryList.append(word.lower())
           

wrongTextlist = []
name = wrongText
with open(name,'r') as text:
    for line in text:
        for word in line.split():
            word = word.replace(".","")
            word = word.replace(",","")
            wrongTextlist.append(word.lower())

found = 0
index = 0
wrongwords = []
for x in wrongTextlist:
    for y in dictionaryList:
        if(x == y):
            found = 1
    if (found == 0):        
        
        wrongwords.append([x,index])
    found = 0
    index += 1

       



    
def findwords(charlist, lenth,word):

    for dictword in dictionaryList:
        if len(dictword) == lenth:


        
            matched = [characters in charlist for characters in dictword]
            contAllChars = all(matched)
            if contAllChars == True:
                dictwordlist = list(dictword)

                dictwordmathed = [characters in dictwordlist for characters in word]
                contAllChars2 = all(dictwordmathed)
                if contAllChars2 == True:
                    return dictword
            

            



with open(wrongText, 'r') as file :
        filedata = file.read()


f = open(correctText, "a")

with open(correctText, "w") as file:
        file.write(filedata)

for word in wrongwords: 
  

    list(word[0])
    lenOflist = len(list(word[0])) 
   





    dictword = findwords( list(word[0]), lenOflist, word[0])




    with open(correctText, 'r') as file :
        filedata = file.read()
        


    try:
        filedata = filedata.replace(word[0], dictword)
        filedata = filedata.replace(word[0] + ",", dictword + ",")
        filedata = filedata.replace(word[0].capitalize(), dictword.capitalize())
        
    except:
        pass

    with open(correctText, 'w') as file:
        file.write(filedata)