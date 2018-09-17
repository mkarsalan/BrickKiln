import os

for root, dirs, files in os.walk("."):
		files.sort()
		for filename in files:
			if filename.endswith(".txt"):
				file = open(filename).readlines()
				count = 0
				avg = 0
				aboveThreshold1 = 0
				aboveThreshold2 = 0
				aboveThreshold3 = 0
				aboveThreshold4 = 0
				aboveThreshold5 = 0
				aboveThreshold6 = 0
				aboveThreshold7 = 0
				aboveThreshold8 = 0

				for line in file:
					a,b,c = line.split()

					if (float(c) > 0.8):
						aboveThreshold1 = aboveThreshold1 + 1
					if (float(c) > 0.7):
						aboveThreshold2 = aboveThreshold2 + 1
					if (float(c) > 0.6):
						aboveThreshold3 = aboveThreshold3 + 1
					if (float(c) > 0.5):
						aboveThreshold4 = aboveThreshold4 + 1
					if (float(c) > 0.4):
						aboveThreshold5 = aboveThreshold5 + 1
					if (float(c) > 0.3):
						aboveThreshold6 = aboveThreshold6 + 1
					if (float(c) > 0.2):
						aboveThreshold7 = aboveThreshold7 + 1
					if (float(c) > 0.1):
						aboveThreshold8 = aboveThreshold8 + 1

					avg = avg + float(c)
					count = count + 1

				results = avg / count

				print(" ")
				print("File:                   " + str(filename))
				print("Count:                  " + str(count))
				print("Above Threshold(>0.8):  " + str(aboveThreshold1))
				print("Above Threshold(>0.7):  " + str(aboveThreshold2))
				print("Above Threshold(>0.6):  " + str(aboveThreshold3))
				print("Above Threshold(>0.5):  " + str(aboveThreshold4))
				print("Above Threshold(>0.4):  " + str(aboveThreshold5))
				print("Above Threshold(>0.3):  " + str(aboveThreshold6))
				print("Above Threshold(>0.2):  " + str(aboveThreshold7))
				print("Above Threshold(>0.1):  " + str(aboveThreshold8))
				print("Average:                " + str(results))
				print(" ")
				print("True Positives:         " + str(aboveThreshold1))
				print("False Negatives:        " + str(count - aboveThreshold1))
				print("_______________________________________________")