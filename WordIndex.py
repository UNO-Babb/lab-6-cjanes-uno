#WordIndex.py
#Name: Colton Janes
#Date: 03/02/2025
#Assignment: Lab 6 - WordIndex

def main():
  while True:
    fileName = input("Enter a file name (i.e. gettysberg.txt, fish.txt) to locate words by line: ").lower()
    if fileName in ["gettysberg.txt", "fish.txt"]:
      break
    else:
      print("Ope, looks like that's not in my library. Only available files are 'gettysberg.txt' and 'fish.txt'")

  textFile = open(fileName, 'r')
  words = {} #create an empty dictionary
  lineNum = 0
  
  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    
    for w in wordList:
      w = w.lower()
      w = w.replace("," , "")
      w = w.replace("." , "")
      w = w.replace("!" , "")
      w = w.replace("-" , " ")
      
      #I had A HECK of a time trying to reconcile the hyphenated words from the gettysberg.txt file.
      #The below #rows are my attempt at separating the "dedicate-we", "consecrate-we" and so on without manipulating the source.
      #Any guidance you can provide would be greatly appreciated.

      #splitHyphenWords = w.split()

      #for word in splitHyphenWords:
        #if word in words:
          #if lineNum not in words[word]:
            #words[word].append(lineNum)
        #else:
          #words[word] = [lineNum]

      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]
  
  for word in words:
    print(word, words[word])

if __name__ == '__main__':
  main()
