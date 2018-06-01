import json
import cv2, random
import matplotlib.pyplot as plt
import numpy as np

def negCropping():
    # open the json file
    # this should be coordinate relative to the big picture
    jsonData = json.load(open("../name_and_box.json","r"))
    names = jsonData.keys()
    # declare how many photo you wanna test out here
    count = 1
    for name in names:
        if count == 5000:
            break
        count +=1
        if name[-2:] == "_L":
            # this image is a left, get the right image
            left = name
            right = str(name[:-2]) + "_R"
        else:
            left = str(name[:-2]) + "_L"
            right = name
        # have to check if we have info on both hands here
        if left not in jsonData or right not in jsonData:
            continue
        else: # this mean that we have info on both hand, use this image to do random crops
            img = cv2.imread("../Color/" + name[:-2] + ".jpg")
            left = (int(jsonData[left][0]), int(jsonData[left][1]))
            right =  (int(jsonData[right][0]), int(jsonData[right][1]))
            # now left and right are a tuple of x and y center, need to avoid this
            listOfPoints = []
            countImages=1
            for i in xrange(10):
                # samle a random point within the possible range
                point = (int(random.randint(0,(img.shape[1])-170)), int(random.randint(0,(img.shape[0])-170)))
                # now need to check if the point over lap with any of the region
                # boolean condition
                alreadyPick = point in listOfPoints
                toAvoidLeft = (point[1] in range(left[1]-85, left[1]+85)) or (point[0] in range(left[0]-85, left[0]+85))
                toAvoidRight = (point[1] in range(right[1]-85, right[1]+85)) or (point[0] in range(right[0]-85, right[0]+85))
                toAvoidLeftEnd = (point[1]+170 in range(left[1]-85, left[1]+85)) or (point[0]+170 in range(left[0]-85, left[0]+85))
                toAvoidRightEnd = (point[1]+170 in range(right[1]-85, right[1]+85)) or (point[0]+170 in range(right[0]-85, right[0]+85))
                while toAvoidLeft or toAvoidRight or toAvoidLeftEnd or toAvoidRightEnd or alreadyPick:
                    # while any of the condition is true above, sample a new point
                    point = (int(random.randint(0,(img.shape[1])-170)), int(random.randint(0,(img.shape[0])-170)))
                    # reset the condition
                    alreadyPick = point in listOfPoints
                    toAvoidLeft = (point[1] in range(left[1]-85, left[1]+85)) or (point[0] in range(left[0]-85, left[0]+85))
                    toAvoidRight = (point[1] in range(right[1]-85, right[1]+85)) or (point[0] in range(right[0]-85, right[0]+85))
                    toAvoidLeftEnd = (point[1]+170 in range(left[1]-85, left[1]+85)) or (point[0]+170 in range(left[0]-85, left[0]+85))
                    toAvoidRightEnd = (point[1]+170 in range(right[1]-85, right[1]+85)) or (point[0]+170 in range(right[0]-85, right[0]+85))
                listOfPoints.append(point) # if we get thru, append the point here
                countImages+=1
                row = point[1]
                col = point[0]
                crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
                cv2.imwrite("../neg_processed_data/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)
# call the method we wrote to plot the box!
negCropping();
print "Done!"

            # # grab the center of the box of the hand to avoid
            # centerColLeft = int(jsonData[left][0])
            # centerRowLeft = int(jsonData[left][1])
            # centerColRight = int(jsonData[right][0])
            # centerRowRight = int(jsonData[right][1])
            # dimension = img.shape
            # endCol = dimension[1]-170 # the last column
            # endRow = dimension[0]-170 # the last row
            # countImages =0
            # # so the range that we're picking from is from 0 to endCol
            # # and also 0 to endRow, but we need a square, so something
            # # from 0 to endCol and 0 to endRow
            # # this will be precisely the range of the box in training set
            # # left hand
            # colToAvoidLowerLeft = centerColLeft - 85
            # colToAvoidHigherLeft = centerColLeft + 85
            # rowToAvoidLowerLeft = centerRowLeft - 85
            # rowToAvoidHigherLeft = centerRowLeft + 85
            # # right hand
            # colToAvoidLowerRight = centerColRight - 85
            # colToAvoidHigherRight = centerColRight + 85
            # rowToAvoidLowerRight = centerRowRight - 85
            # rowToAvoidHigherRight= centerRowRight + 85
            # # keep track of the points we have been sampling
            # listOfPoints = []
            # for i in xrange(20):# create 10 different patches
            #     # randomly sample a row and col and store these 2 points as a tuple
            #     countImages+=1
            #     point = (random.randint(0,endCol), random.randint(0,endRow))
            #     # check if we have already pick any of these point
            #     condition0 = point in listOfPoints
            #     # check if point lies inside the to avoid range
            #     condition1 = point[0] >= colToAvoidLowerLeft and point[0] <= colToAvoidHigherLeft
            #     condition2 = point[1] >= rowToAvoidLowerLeft and point[1] <= rowToAvoidHigherLeft
            #     condition3 = point[0] >= colToAvoidLowerRight and point[0] <= colToAvoidHigherRight
            #     condition4 = point[1] >= rowToAvoidLowerRight and point[1] <= rowToAvoidHigherRight
            #     # also need to check if the end points lies within the avoid range or not
            #     condition6 = point[0]+170 >= colToAvoidLowerLeft and point[0]+170 <= colToAvoidHigherLeft
            #     condition7 = point[1]+170 >= rowToAvoidLowerLeft and point[1]+170 <= rowToAvoidHigherLeft
            #     condition8 = point[0]+170 >= colToAvoidLowerRight and point[0]+170 <= colToAvoidHigherRight
            #     condition9 = point[1]+170 >= rowToAvoidLowerRight and point[1]+170 <= rowToAvoidHigherRight
            #     # join the 4 condition above for simplicity
            #     condition5 = ((condition1 == True) and (condition2 == True)) or ((condition3 == True) and (condition4 == True))
            #     condition10 = ((condition5 == True) and (condition6 == True)) or ((condition7 == True) and (condition8 == True))
            #     while (condition0 == True) or (condition5 == True) or (condition10 == True):
            #         point = (random.randint(0,endCol), random.randint(0,endRow))
            #         condition0 = point in listOfPoints
            #         condition1 = point[0] >= colToAvoidLowerLeft and point[0] <= colToAvoidHigherLeft
            #         condition2 = point[1] >= rowToAvoidLowerLeft and point[1] <= rowToAvoidHigherLeft
            #         condition3 = point[0] >= colToAvoidLowerRight and point[0] <= colToAvoidHigherRight
            #         condition4 = point[1] >= rowToAvoidLowerRight and point[1] <= rowToAvoidHigherRight
            #         condition5 = ((condition1 == True) and (condition2 == True)) or ((condition3 == True) and (condition4 == True))
            #         condition6 = point[0]+170 >= colToAvoidLowerLeft and point[0]+170 <= colToAvoidHigherLeft
            #         condition7 = point[1]+170 >= rowToAvoidLowerLeft and point[1]+170 <= rowToAvoidHigherLeft
            #         condition8 = point[0]+170 >= colToAvoidLowerRight and point[0]+170 <= colToAvoidHigherRight
            #         condition9 = point[1]+170 >= rowToAvoidLowerRight and point[1]+170 <= rowToAvoidHigherRight
            #         condition10 = ((condition5 == True) and (condition6 == True)) or ((condition7 == True) and (condition8 == True))
            #     # save the points here if it doesn't satisfy all of the condition
            #     # in the while loop
            #     listOfPoints.append(point)
                # row = point[1]
                # col = point[0]
                # crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
                # # plt.imshow(crop_img[:,:,::-1])
                # # plt.pause(0.05) # pause for 3 secs
                # cv2.imwrite("../neg_processed_data/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)



# this approach is too systematic, will create bias to the learner
# need something else!
# sliding window with same stride of 170
# for row in xrange(0,endRow-170,170):
#     for col in xrange(0,endCol-170,170):
#         # need to add a check that even if the col is wihin the range of the
#         # box that contains the hand, don't crop
#         #
#         crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
    	# plt.imshow(crop_img[:,:,::-1])
    	# plt.pause(0.05) # pause for 3 secs
#         countImages +=1
#
#         # save the image in a folder
#         # need to decide how to name the negative patches as well!
    # cv2.imwrite("neg_processed_data/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)
