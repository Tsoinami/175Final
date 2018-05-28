


import json
import cv2, random
import matplotlib.pyplot as plt
import numpy as np

def negCropping():

    # open the json file
    jsonData = json.load(open("./name_and_box.json","r"))
    names = jsonData.keys()

    # declare how many photo you wanna check out here
    count = 1
    for name in names:
        if count == 2:
            break
        count +=1

        # load in the image
    	img = cv2.imread("./Color/" + name[:-2] + ".jpg")

        # grab the center of the box of the hand to avoid
        centerX = int(jsonData[name][0])
        centerY = int(jsonData[name][1])
        # now just need to start sliding the window little by litte
        # maybe do a for loop here !!
        dimension = img.shape
        endCol = dimension[1] # the last column
        endRow = dimension[0] # the last row

        countImages =0

        for row in xrange(0,endRow-170,170):
            for col in xrange(0,endCol-170,170):
                # need to add a check that even if the col is wihin the range of the
                # box that contains the hand, don't crop
                #
                crop_img = img[ row :row+170  , col : col+170] # crop a window of 170x170 pixels
            	plt.imshow(crop_img[:,:,::-1])
            	plt.pause(0.05) # pause for 3 secs
                countImages +=1

                # save the image in a folder
                # need to decide how to name the negative patches as well!
                cv2.imwrite("neg_processed_data/" + str(name[:-2]) +"_"+ str(countImages)+".jpg", crop_img)

        print countImages

# call the method we wrote to plot the box!
negCropping();
print "Done!"
