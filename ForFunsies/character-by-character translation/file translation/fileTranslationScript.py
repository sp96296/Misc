# follow https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
# and maybe https://cloud.google.com/translate/docs/quickstart-client-libraries
from google.cloud import translate


OUTPUT_LANGUAGE = "en"
FILE_IN_TXT = ""
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
        saveToFile(line, translated)
        i += 1

def saveToFile(old, line):
    with open(FILE_OUT_TXT, "a", encoding='utf-8') as file:
        for part in [old,line]:
            modified = (part + "\n") if ("\n" not in part) else part
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