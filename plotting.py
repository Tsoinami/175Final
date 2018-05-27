import json
import cv2, random
import matplotlib.pyplot as plt


def drawing():

    # open the json file
    jsonData = json.load(open("./name_and_box.json","r"))
    names = jsonData.keys()

    # declare how many photo you wanna plot here
    count = 1
    for name in names:
        if count == 10:
            break
        count +=1

        # background will be the picture in the folder
    	canvas = cv2.imread("./Color/" + name[:-2] + ".jpg")

        # draw the box here
    	for x_y in jsonData[name]:
            x = int(x_y[0])
            y = int(x_y[1])
            # draw the four corners of the box with a circle
            cv2.circle(canvas, tuple([x,y]) ,5, (0,255,0),-1)

    	plt.imshow(canvas[:,:,::-1])
    	plt.pause(10)

# call the method we wrote to plot the box!
drawing();
