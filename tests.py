from fileManager.fileManager import *


filters = [
    "has this;and that#not those",
    "has this",
    "has that",
    "has those"
]

testStrings = [
    "string with this and that with has",
    "string with this and that with has not",
    "string with this and that with has those",
]

#tests
for string in testStrings:
    print("String: " + string)
    for filter in filters:
        print("     (" + str(textHasStringFilter(string, filter)) + ") " + filter)
    print("")

