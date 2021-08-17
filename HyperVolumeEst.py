# Programming Assignment 1, Circle "Hyper-Volumes"
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
    randt = 2 * random.random() - 1
    x = randx
    y = randy
    z = randz
    t = randt
    freddistance = x**2 + y**2 + z**2 + t**2
    #for statement

    if freddistance <= 1:
        insideCount = insideCount + 1
        #if statement

area = (insideCount / numdarts) * 16
print("Hyper Volume of the 4D Sphere is:", area)
rhvolume = (1 / 2) * (math.pi ** 2)
print(rhvolume, "Is the actual volume of the hyper sphere.")

#Dimension Names:HS4D) S3 R4
#Equation: X^2 + y^2 + z^2 + t^2 < 1
#EHVS: V1 = (1/2)(pi^2)(r^4)
#Program intentions: Estimating the hyper-volume in hyper sphere.
#Monte Carlo Method, pi is not given.

# Result 1) Darts(1000)Hyper Volume of the 4D Sphere is: 4.848 - 4.934802200544679 Is the actual volume of the hyper sphere.
# The estimated and the correct answer aren't very close, they are around .11 off.

# Result 2) Darts(100000)Hyper Volume of the 4D Sphere is: 4.95712 - 4.934802200544679 Is the actual volume of the hyper sphere.
# The estimated and the correct answer very close, they become none symmetric by the second decimal spot. And they are only off by .02,
# the pattern shown is that the more darts thrown it improves the perdiction.

# Result 3) Darts(10)Hyper Volume of the 4D Sphere is: 3.2 - 4.934802200544679 Is the actual volume of the hyper sphere.
# The estimated and the correct answer are not similar at all, the estimate is off by 1.7, the pattern shown is that the
# less darts thrown it worsens the perdiction.
