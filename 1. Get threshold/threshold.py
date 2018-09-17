f=open("houses(Lat+Lng+Threshold).txt","w")
f2=open("houses(Lat+Lng).txt","w")

file = open("houses.txt").readlines()
counter = 0

for line in file:
    a,b,c = line.split()

    if (float(c)>0.8) and (float(c)<=1):
        f.write(a + " " + b + " " + c + "\n")
        f2.write(b + "," + a + "\n")
        counter = counter + 1 

f.close()
print(counter)