from statistics import median as median

def quickSort(toSort):
    listLen = len(toSort)
    sorted = toSort
    if listLen == 2:
        first = toSort[0]
        second = toSort[1]
        if first > second:
            sorted = [second, first]
    elif listLen > 2:
        medianVal = median(toSort)
        firstHalf = []
        secondHalf = []
        for item in toSort:
            if item < medianVal:
                firstHalf.append(item)
            else:
                secondHalf.append(item)
        firstSorted = quickSort(firstHalf)
        secondSorted = quickSort(secondHalf)
        sorted = firstSorted + secondSorted
    return sorted


def formatList(toSort):
    toSortLen = len(toSort)
    for index in range(toSortLen):
        currentItem = toSort[index]
        currentStr = str(currentItem)
        toSort[index] = currentStr
    return toSort

def main():
    testList = ["apple", "jelly", "banana", "animal", 3]
    formattedTestList = formatList(testList)
    quickSorted = quickSort(formattedTestList)
    print(quickSorted)

main()