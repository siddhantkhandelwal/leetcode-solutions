from os import listdir
from os.path import isfile, join, splitext

indexes = []


def extractAttributes(filename):
    indexEntry = []
    with open(filename) as f:
        data = f.readlines()
        indexEntry.append(int(data[0][5:].split('\\')[0]))
        indexEntry.append(data[0][4:])
        indexEntry.append(data[2].split(' ')[1])
        indexEntry.append(data[4][16:].split(',')[0])
    indexes.append(indexEntry)


def generateMarkDown():
    markdown = "\n" + str("| ")
    for e in ["Title", "Difficulty", "Related Topic"]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(["Title", "Difficulty", "Related Topic"])):
        markdown += str("-------------- | ")
    markdown += "\n"

    indexes.sort()

    for entry in indexes:
        markdown += str("| ")
        for e in entry[1:]:
            to_add = str(e.rstrip()) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"


def writeIndex(indexFileName):
    with open(indexFileName, "w", encoding="utf-8") as f:
        header = "<br><i>Star the Repository if it helps you :smile:</i>\n # Leetcode Solutions \n My solutions to leetcode problems solved during Placement Season \n ## Index"
        footer = "<br><br><br>Index created using indexer script"
        markdown = header
        markdown += generateMarkDown()
        markdown += footer
        f.write(markdown)


def checkValidSolFile(f):
    if isfile(f) and splitext(f)[1] == ".md" and splitext(f)[0] != "README":
        return True
    return False


def getFilesCWD():
    solutionsFiles = [f for f in listdir('.') if checkValidSolFile(f)]
    return solutionsFiles


def driver():
    solutionFiles = getFilesCWD()
    for f in solutionFiles:
        extractAttributes(f)
    writeIndex("README.md")


if __name__ == "__main__":
    driver()
