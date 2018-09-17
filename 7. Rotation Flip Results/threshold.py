f=open("results.txt","w")
# f2=open("brickKilns(Lat+Lng).txt","w")

flipHorizontally = open("flipHorizontally.txt").readlines()
flipVertically = open("flipVertically.txt").readlines()
rotate_90 = open("rotate_90.txt").readlines()
rotate_180 = open("rotate_180.txt").readlines()

counter = 0

for line in flipHorizontally:
    a,b,c = line.split()

    if (float(c)>0.8) and (float(c)<=1):
        f.write(a + " " + b + " " + c + "\n")
        f2.write(b + "," + a + "\n")
        counter = counter + 1 

f.close()
print(counter)