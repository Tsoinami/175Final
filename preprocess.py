from __future__ import division
import json

toDump = {}
offset = 80;  # in case we wanna change the offset !

def processData():

    count = 1  # this is only for debugging

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

        # get max and min of X and Y
        maxX = centerX + offset
        maxY = centerY + offset
        minX = centerX - offset
        minY = centerY - offset

        # get 4 corners, store them in a tuple
        corner1 = (maxX, maxY)
        corner2 = (maxX, minY)
        corner3 = (minX, minY)
        corner4 = (minX, maxY)

        # store 4 corners tuple into a list
        box = []
        box.append(corner1)
        box.append(corner2)
        box.append(corner3)
        box.append(corner4)

        # store the name of the file and the list of 4 corners into a dict
        # for dumping into a json file!!
        toDump[name] = box

        # testing with first 10 images using debuggin variable count
        if count == 10:
            break
        count +=1

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
