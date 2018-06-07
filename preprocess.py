# Usage: this script is used to find the center of the hand and store them in
#        a json file

from __future__ import division
import json


toDump = {}

def processData():

    # count = 1  # this is only for debugging

    #bleh
    global jsonData
    global offset

    # open the json file
    jsonData = json.load(open("./annotation.json","r"))

    # this is the name of the file we're inspecting, loop thru these
    names = jsonData.keys()
    for name in names:
        # print name
        # store all X and Y coords
        listOfX = []
        listOfY = []
        for coordinate in jsonData[name]:
            # coordinate is a list of 22 points (smaller list)
            listOfX.append(coordinate[0])
            listOfY.append(coordinate[1])

        # get the center X and center Y
        centerX = sum(listOfX) / len(listOfX)
        centerY = sum(listOfY) / len(listOfY)

        # store the center of X and Y for cropping
        box = []
        box.append(centerX)
        box.append(centerY)

        # store the name of the file and the list of 4 corners into a dict
        # for dumping into a json file!!
        toDump[name] = box

        # testing with first 10 images using debuggin variable count
        # if count == 10000:
        #     break
        # count +=1

# method to do json dumpping
def dumpShit():
    # dump everything in to a json file here
    with open('name_and_box.json', 'w') as filePointer:
        json.dump(toDump, filePointer)

# call the shit you wrote fam
processData()

# call the json writing file here once you're done !!
dumpShit()

print "Done!"
