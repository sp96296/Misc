import random

NOUNS = "91K nouns.txt"
ADJECTIVES = "28K adjectives.txt"
SENTENCE = "The {} {} {}."

def getWord(file):
    lineCollection = file.readlines()
    length = len(lineCollection)-1
    lineNum = random.randint(0,length)
    line = lineCollection[lineNum].strip()
    return line

def main():
    nouns = open(NOUNS, "r")
    adjectives = open(ADJECTIVES, "r")
    noun = getWord(nouns)
    if noun[-1] == "s":
        plur = "are"
    else:
        plur = "is"
    adjective = getWord(adjectives)
    print(SENTENCE.format(noun,plur,adjective))
    
main()
