#WordCount.py
#Name: Colton Janes
#Date: 03/02/2025
#Assignment: Lab 6 - WordCount

def main():
  while True:
    fileName = input("Enter a file name (i.e. gettysberg.txt, fish.txt) to count its lines, words, and characters: ").lower()
    if fileName in ["gettysberg.txt", "fish.txt"]:
      break
    else:
      print("Ope, looks like that's not in my library. Only available files are 'gettysberg.txt' and 'fish.txt'")

  textFile = open(fileName, 'r')
  lineCount = 0
  wordCount = 0
  characterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    characterCount = characterCount + len(line)
      
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    
  print("You selected:", fileName)
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", characterCount)

if __name__ == '__main__':
  main()
