# Programming Assignment 1, Circle "Volumes and Area"
# Ethan Kupka
# Sept 27th, 2019

#Program intentions: Estimating the area in the circle, volume in the sphere, hyper-volume in hyper sphere.
#Monte Carlo Method, pi is not given.

import random
import math

numdarts = 100000
insideCount = 0

for i in range(numdarts):
    randx = random.random() * random.randrange(-1, 2, 2)
    randy = random.random() * random.randrange(-1, 2, 2)
    #randz = random.random() * random.randrange(-1, 2, 2)
    x = randx
    y = randy
    #z = randz
    #t.goto(x,y)
    freddistance = x**2 + y**2 #+ z**2
    #for statement

    if freddistance <= 1:
        #fred.color("green")
        #print("yes")
        insideCount = insideCount + 1
    else:
        #fred.color("red")
        #print("no")
        insideCount = insideCount
    #fred.stamp()
    #end of if statement

print("The number of darts that inside the circle was:", insideCount)
pi = (insideCount / 100000) *4
print("PI is:", pi)

#Estimating Area of Circle
area = pi * (.5 ** 2)
print(area, "Is the estemated area of the circle.")

#Estimating Volume of Sphere
volume = (4/3) * pi * (.5 ** 3)
print(volume, "Is the estimated volume of the 3D sphere.")
rvolume = (4/3) * math.pi * (.5 ** 3)
print(rvolume, "Is the actual volume of the 3D sphere.")

#Estimating Hyper Volume of Hyper-Sphere
hvolume = (1 / 2) * (pi ** 2) * (.5 ** 4)
print(hvolume, "Is the estimated hyper volume of the hyper sphere.")
rhvolume = (1 / 2) * (math.pi ** 2) * (.5 ** 4)
print(rhvolume, "Is the actual volume of the 3D sphere.")

#wn.exitonclick()

#Dimension Names: C2D) S1 R2 - S3D) S2 R3 - HS4D) S3 R4
#Equation: X^2 + y^2 < 1
#EC: A = pi*r^2
#EVS: V = (4/3)*pi*r^3
#EHVS: V1 = (1/2)(pi^2)(r^4) ###V2 = 2(pi^2)(r^3)
