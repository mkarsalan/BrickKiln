import cv2
import os

pictures = []

zoomLevels = [20,19,18,17,16,15]

for zoom in zoomLevels:
	dim = 256/(2 ** (20 - zoom))
	print(int(dim))
	directory = 'zoomLevel_' + str(zoom)
	if not os.path.exists(directory):
	    os.makedirs(directory)

	for root, dirs, files in os.walk("."):  
		for filename in files:
			if filename.endswith(".png"):
				pictures.append(filename)
				image = cv2.imread(filename)
				crop_img = image[0:480, 0:480]
				resized = cv2.resize(crop_img, (int(dim), int(dim)))
				resized = cv2.resize(resized, (256, 256))
				filenamejpg = filename[:-3] + 'jpg'
				cv2.imwrite(directory + "/" + filenamejpg, resized)
