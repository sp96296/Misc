# follow https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
# and maybe https://cloud.google.com/translate/docs/quickstart-client-libraries
from google.cloud import translate


OUTPUT_LANGUAGE = "en"
FILE_IN_TXT = input("file path?")
FILE_OUT_TXT = "translated.txt"

print("launching")

def translateItem(details):
    client, item = details
    translatedResult = client.translate(item, target_language=OUTPUT_LANGUAGE)
    translated = translatedResult["translatedText"]
    return translated

def translateFromList(details):
    client, strList= details
    i = 0
    for line in strList:
        status_remainder = i%3
        print("translating", "."*(status_remainder+1))
        lineDetails = client, line
        translated = translateItem(lineDetails)
        saveToFile(translated)
        i += 1

def saveToFile(line):
    with open(FILE_OUT_TXT, "a", encoding='utf-8') as file:
        modified = line + "\n"
        file.write(modified)
        file.close()

def getFile():
    with open(FILE_IN_TXT, "r", encoding="utf-8") as readfile:
        lines = readfile.readlines()
    return lines

def main():
    client = translate.Client()
    lines = getFile()
    details = client, lines
    translateFromList(details)

main()