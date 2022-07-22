
#Return if the text has all the words in the list
import os


def textHasAllWords(text, words):
    for word in words:
        if word.lower() not in text.lower():
            return False
    return True

#REturn if the text has any of the words in the list
def textHasAnyWords(text, words):
    for word in words:
        if word.lower() in text.lower():
            return True
    return False

'''
    Function: textHasFilter
    Description: Return if the text had the filter passed
    Parameters:
        text: The text to check
        hasWords: The words to check for
        hasNotWords: The words to check for
    Returns: True if the text had the filter, False if not
'''
def textHasFilter(text, hasWords, hasNotWords):
    if textHasAllWords(text, hasWords):
        if textHasAnyWords(text, hasNotWords):
            return False
        return True
    return False

'''
    Function: textHasStringFilter
    Description: Return if the text had the filter passed. Filter is a string in a format of "has;this;and;this#hasnot;this;and;this"
    Parameters:
        text: The text to check
        filter: The filter to check for
    Returns: True if the text had the filter, False if not
'''
def textHasStringFilter(text, filter):
    #replace all spaces with ; to make it easier to split
    filter = filter.replace(" ", ";")

    #Split one time the filter into has and hasnot by the #
    split = filter.split("#", 1)
    
    #Has words is the first part of the split, and hasnot words is the second part of the split or empty array if there is no #
    hasWords = split[0].split(";")
    hasNotWords = split[1].split(";") if len(split) > 1 else []

    #Remove all empty words
    hasWords = [word for word in hasWords if len(word) > 0]
    hasNotWords = [word for word in hasNotWords if len(word) > 0]
        
    return textHasFilter(text, hasWords, hasNotWords)

'''
    Function: findFiles
    Description: Find all the files in the directory that match the filter
    Parameters:
        directory: The directory to search
        filter: The filter to check for
        limiter: The number of files to return, -1 for all, default is -1
    Returns: A list of all the files that match the filter
'''
def findFiles(directory, filter, limiter=-1):
    try:
        #Get all the files in the directory
        files = os.listdir(directory)
        #Create a list to store the files that match the filter
        filteredFiles = []
        #Loop through all the files
        for file in files:
            #Check if the file matches the filter
            if textHasStringFilter(file, filter):
                #Add the file to the list
                filteredFiles.append(file)
                #Check if the limiter is reached
                if limiter != -1 and len(filteredFiles) >= limiter:
                    #Return the list
                    return filteredFiles
        #Return the list
        return filteredFiles
    except:
        #Return an empty list
        return []

#Find file in the directory that match the filter
def findFile(directory, filter):
    return findFiles(directory, filter, 1)[0]