import json
import cv2, random
import matplotlib.pyplot as plt
import numpy as np

def negCropping():

    # open the json file
    jsonData = json.load(open("./name_and_box.json","r"))
    names = jsonData.keys()

    # declare how many photo you wanna test out here
    count = 1
    for name in names:
        if count == 10:
            break
        count +=1

        # apparently not both the hand location are available... weird
        if name[-2:] == "_L":
            # this image is a left, get the right image
            left = name
            right = str(name[:-2]) + "_R"
        else:
            left = str(name[:-2]) + "_L"
            right = name


        # load in the image
    	img = cv2.imread("./Color/" + name[:-2] + ".jpg")

        # grab the center of the box of the hand to avoid
        centerColLeft = int(jsonData[left][0])
        centerRowLeft = int(jsonData[left][1])
        centerColRight = int(jsonData[right][0])
        centerRowRight = int(jsonData[right][1])
        dimension = img.shape
        endCol = dimension[1]-170 # the last column
        endRow = dimension[0]-170 # the last row

        countImages =0

        # so the range that we're picking from is from 0 to endCol
        # and also 0 to endRow, but we need a square, so something
        # from 0 to endCol and 0 to endRow

        # this will be precisely the range of the box in training set
        # left hand
        colToAvoidLowerLeft = centerColLeft - 85
        colToAvoidHigherLeft = centerColLeft + 85
        rowToAvoidLowerLeft = centerRowLeft - 85
        rowToAvoidHigherLeft = centerRowLeft + 85
        # right hand
        colToAvoidLowerRight = centerColRight - 85
        colToAvoidHigherRight = centerColRight + 85
        rowToAvoidLowerRight = centerRowRight - 85
        rowToAvoidHigherRight= centerRowRight + 85

        # keep track of the points we have been sampling
        listOfPoints = []

        for i in xrange(10):# create 10 different patches
            # randomly sample a row and col and store these 2 points as a tuple
            countImages+=1
            point = (random.randint(0,endCol), random.randint(0,endRow))
            # check if we have already pick any of these point
            condition0 = point in listOfPoints
            # check if point lies inside the to avoid range
            condition1 = point[0] >= colToAvoidLowerLeft and point[0] <= colToAvoidHigherLeft
            condition2 = point[1] >= rowToAvoidLowerLeft and point[1] <= rowToAvoidHigherLeft
            condition3 = point[0] >= colToAvoidLowerRight and point[0] <= colToAvoidHigherRight
            condition4 = point[1] >= rowToAvoidLowerRight and point[1] <= rowToAvoidHigherRight

            # join the 4 condition above for simplicity
            condition5 = ((condition1 == True) and (condition2 == True)) or ((condition3 == True) and (condition4 == True))

            while (condition0 == True) or (condition5 == True):
                point = (random.randint(0,endCol), random.randint(0,endRow))
                condition0 = point in listOfPoints
                condition1 = point[0] >= colToAvoidLower and point[0] <= colToAvoidHigher
                condition2 = point[1] >= rowToAvoidLower and point[1] <= rowToAvoidHigher
                condition3 = point[0] >= colToAvoidLowerRight and point[0] <= colToAvoidHigherRight
                condition4 = point[1] >= rowToAvoidLowerRight and point[1] <= rowToAvoidHigherRight
                condition5 = ((condition1 == True) and (condition2 == True)) or ((condition3 == True) and (condition4 == True))

            # save the points here if it doesn't satisfy all of the condition
            # in the while loop
            listOfPoints.append(point)
            row = point[1]
            col = point[0]
            crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
            # plt.imshow(crop_img[:,:,::-1])
            # plt.pause(0.05) # pause for 3 secs
            cv2.imwrite("neg_processed_data/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)

# call the method we wrote to plot the box!
negCropping();
print "Done!"



# this approach is too systematic, will create bias to the learner
# need something else!
# sliding window with same stride of 170
# for row in xrange(0,endRow-170,170):
#     for col in xrange(0,endCol-170,170):
#         # need to add a check that even if the col is wihin the range of the
#         # box that contains the hand, don't crop
#         #
#         crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
#     	plt.imshow(crop_img[:,:,::-1])
#     	plt.pause(0.05) # pause for 3 secs
#         countImages +=1
#
#         # save the image in a folder
#         # need to decide how to name the negative patches as well!
    # cv2.imwrite("neg_processed_data/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)
