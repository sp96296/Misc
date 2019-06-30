# follow https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
# and maybe https://cloud.google.com/translate/docs/quickstart-client-libraries
from google.cloud import translate


OUTPUT_LANGUAGE = "en"
FILE_IN_TXT = ""
FILE_OUT_TXT = "translated.txt"

print("launching")

def translateItem(details):
    client, item = details
    print("translating", item, "|", end="")
    translatedResult = client.translate(item, target_language=OUTPUT_LANGUAGE)
    translated = translatedResult["translatedText"]
    print("result:",translated)
    return translated

def translateFromList(details):
    client, strList= details
    translation = []
    i = 0
    for line in strList:
        status_remainder = i%4
        print("translating", "."*status_remainder)
        lineDetails = client, line
        translated = translateItem(lineDetails)
        translation.append(translated)
        i += 1
    return translation

def saveToFile(lines):
    with open(FILE_OUT_TXT, "w+", encoding='utf-8') as file:
        data = file.readlines()
        lineMax = len(lines)
        lineNum = 1
        for line in lines:
            modified = line + "\n"
            data.append(modified)
            print("appended {} of {}".format(lineNum, lineMax))
            lineNum += 1
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