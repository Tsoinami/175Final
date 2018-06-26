# Usage: this script is used to crop the image according to info in
#        a json file and store as .jpeg file, optional plotting is available


import json
import cv2, random
import matplotlib.pyplot as plt

offset = 85 # if we wanna change the offset

def cropping():

	print "Wadduppppppp!!"

    # global offset
    # open the json file
    jsonData = json.load(open("./name_and_box.json","r"))
    names = jsonData.keys()

    # declare how many photo you wanna check out here
    # count = 1
    for name in names:
        # if count == 10000:
        #     break
        # count +=1

        # load in the image
    	img = cv2.imread("./Color/" + name[:-2] + ".jpg")

        # crop image and plot
        centerX = int(jsonData[name][0])
        centerY = int(jsonData[name][1])
        crop_img = img[ centerY-offset :centerY + offset  , centerX - offset: centerX + offset]
        cv2.imwrite("processed_data/" + str(name)+".jpg", crop_img)

        # optional plotting
    	# plt.imshow(crop_img[:,:,::-1])
    	# plt.pause(3) # pause for 3 secs

        # save the image in a folder


# call the method we wrote to plot the box!
cropping();
print "Done!"
