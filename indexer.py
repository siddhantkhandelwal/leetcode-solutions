from os import listdir, makedirs, walk
from os.path import isfile, join, splitext, isdir
import shutil

indexes = []
topics = set()


def extractAttributes(filename):
    indexEntry = []
    with open(filename) as f:
        data = f.readlines()
        indexEntry.append(int(data[0][5:].split('\\')[0]))
        indexEntry.append(data[0].split('\\.')[1].split(']')[0].strip())
        indexEntry.append(data[2].split(' ')[1][2:-3])
        indexEntry.append(data[4][16:].split(',')[0][1:].split(']')[0])
        topics.add(''.join(data[4][16:].split(',')[
                   0][1:].split(']')[0].split(" ")))
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
        markdown += "[" + str(entry[0]).rstrip() + ". " + str(entry[1].rstrip()) + "]" + "(" + ''.join(
            entry[3].split(" ")) + "/" + str(entry[0]) + ".md" + ")" + str(" | ")
        markdown += str(entry[2].rstrip()) + str(" | ")
        markdown += "[" + str(entry[3]) + "]" + "(" + \
            str(''.join(entry[3].split(" "))) + "/" + ")" + str(" | ")
        markdown += "\n"

    return markdown + "\n"


def writeIndex(indexFileName):
    with open(indexFileName, "w", encoding="utf-8") as f:
        header = "<i>Star the Repository if it helps you :smile:</i>\n # Leetcode Solutions \n My solutions to leetcode problems solved during Placement Season \n ## Index"
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


def createDirectories():
    for topic in topics:
        if not isdir(topic):
            makedirs(topic)


def moveFiles():
    for index in indexes:
        topic = index[3]
        try:
            shutil.move(str(index[0]) + ".md",
                        join(''.join(index[3].split(" ")), str(index[0]) + ".md"))
        except:
            print("error in moving")
            print(index)


def driver():
    solutionFiles = getFilesCWD()
    for f in solutionFiles:
        extractAttributes(f)
    createDirectories()
    moveFiles()
    writeIndex("README.md")


if __name__ == "__main__":
    driver()
