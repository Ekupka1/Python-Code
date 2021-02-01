# Programming Assignment 1, Circle "Volume"
# Ethan Kupka
# Sept 27th, 2019

import random
import math

dart = int(input("How many darts are you throwing?"))
numdarts = dart
insideCount = 0

for i in range(numdarts):
    randx = 2 * random.random() - 1
    randy = 2 * random.random() - 1
    randz = 2 * random.random() - 1
    x = randx
    y = randy
    z = randz
    freddistance = x**2 + y**2 + z**2
    #for statement

    if freddistance <= 1:
        insideCount = insideCount + 1
        #if statement

area = (insideCount / numdarts) * 8
print("Volume of the 3D Sphere is:", area)
rvolume = (4/3) * math.pi
print("This is the actual volume is", rvolume)

#Dimension Names: S3D) S2 R3
#EVS: V = (4/3)*pi*r^3
#Equation: X^2 + y^2 + z^2 < 1
#Program intentions: Estimating the volume in the sphere
#Monte Carlo Method, pi is not given.

# Result 1) Darts(1000)Volume of the 3D Sphere is: 3.968 - This is the actual volume is 4.1887902047863905
# The estimated and the correct answer aren't very close, they are around .2 off

# Result 2) Darts(1000000)Volume of the 3D Sphere is: 4.184368 - This is the actual volume is 4.1887902047863905
# The estimated and the correct answer very close, they become none symmetric by the third decimal spot. The more darts thrown improved the comparison a lot.

# Result 3) Darts(10)Volume of the 3D Sphere is: 3.2 - This is the actual volume is 4.1887902047863905
# The estimated and the correct answer aren't close, it's .9 off.
