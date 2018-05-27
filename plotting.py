import json
import cv2, random
import matplotlib.pyplot as plt


def drawing():
	Joints = json.load(open("./name_and_box.json","r"))
	names = Joints.keys()

    for name in names:

        # read in the image for the background
		canvas = cv2.imread("./Color/" + name[:-2] + ".jpg")
		tmp = []

        # this is just pulling out all of the x and y from the json data 
		for i in xrange(len(Joints[name])):
			tmp.append([int(Joints[name][i][0]), int(Joints[name][i][1])])
		# print tmp
		canvas = draw_hand(canvas, tmp)
		plt.imshow(canvas[:,:,::-1])
		plt.pause(1)



# call the method we wrote to plot the box!
drawing();
