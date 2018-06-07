import json
import cv2, random
import matplotlib.pyplot as plt
import numpy as np

def test():
    jsonData = json.load(open("../name_and_box.json","r"))
    names = jsonData.keys()
    # this approach is too systematic, will create bias to the learner
    # need something else!
    # sliding window with same stride of 170
    debuggingVar = 1
    for name in names:
        if debuggingVar == 10000:
            break
        else:
            img = cv2.imread("../Color/" + name[:-2] + ".jpg")
            endCol = img.shape[1]-170 # the last column
            endRow = img.shape[0]-170 # the last row
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
            else:
                # need to figure out the center of the hand, then replace that patch
                # with a patch that you know for sure doesn't have the hand
                # here i choose the first window
                centerXL = int(jsonData[left][0])
                centerYL = int(jsonData[left][1])
                centerXR = int(jsonData[right][0])
                centerYR = int(jsonData[right][1])
                # need to replace the window below with the first window!!
                img[ centerYL-85 :centerYL + 85  , centerXL - 85: centerXL + 85] = img[0:170,0:170]
                img[ centerYR-85 :centerYR + 85  , centerXR - 85: centerXR + 85] = img[0:170,0:170]
                # try to save down the image here
                # cv2.imwrite("../wellnt/" + str(name)+".jpg", img)
                debuggingVar += 1 # increment to break

                # this integer is only used for the two for loops down below
                countImages = 0 # this is to save each individual patches we're going to cut

                for row in xrange(0,endRow-170,170):
                    for col in xrange(0,endCol-170,170):
                        # need to add a check that even if the col is wihin the range of the
                        # box that contains the hand, don't crop
                        #
                        crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
                    	# plt.imshow(crop_img[:,:,::-1])
                    	# plt.pause(0.05) # pause for 3 secs
                        countImages +=1

                        # save the image in a folder
                        # need to decide how to name the negative patches as well!
                        cv2.imwrite("../wellnt/" + str(name[:-2]) + "_" + str(countImages)+".jpg", crop_img)
test()
print "Done"