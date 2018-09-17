import cv2
import os

# dim = 256/(2 ** (20 - zoom))
# print(int(dim))
directory = 'flipHorizontally'
if not os.path.exists(directory):
    os.makedirs(directory)

for root, dirs, files in os.walk("."):  
	for filename in files:
		if filename.endswith(".jpg"):
			img = cv2.imread(filename)
			
			# rotate
			# rows,cols,alpha = img.shape
			# M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)	# 180 is the degree to rotate
			# dst = cv2.warpAffine(img,M,(cols,rows))
			
			# flip 
			dst = cv2.flip(img, 1);	# change 1 to 0 for vertical flip

			cv2.imwrite(directory + "/" + filename, dst)
