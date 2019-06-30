# follow https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
# and maybe https://cloud.google.com/translate/docs/quickstart-client-libraries
from google.cloud import translate


OUTPUT_LANGUAGE = "en"
FILE_IN_TXT = "SH21.txt"
FILE_OUT_TXT = "translated.txt"

print("launching")

def translateItem(details):
    client, item = details
    translatedResult = client.translate(item, target_language=OUTPUT_LANGUAGE)
    translated = translatedResult["translatedText"]
    return translated

def translateFromList(details):
    client, strList= details
    translation = []
    i = 0
    for line in strList:
        status_remainder = i%4
        print("translating", "."*status_remainder)
        translated = translateItem(client, line)
        translation.append(translated)
        i += 1
    return translation

def saveToFile(lines):
    with open(FILE_OUT_TXT, "w+", encoding='utf-8') as file:
        data = file.readlines()
        lineMax = len(lines)
        lineNum = 1
        for line in lines:
            print("appended {} of {}".format(lineNum, lineMax))
            data.append(line)
        file.writelines(data)
        file.close()
        print("saved to", FILE_OUT_TXT)

def getFile():
    with open(FILE_IN_TXT, "r", encoding="utf-8") as readfile:
        lines = readfile.readlines()
    return lines

def main():
    print("main")
    client = translate.Client()
    lines = getFile()
    details = client, lines
    translatedLines = translateFromList(details)
    saveToFile(translatedLines)

main()