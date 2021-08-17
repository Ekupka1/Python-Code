# Programming Assignment 1, Circle "Area"
# Ethan Kupka
# Sept 27th, 2019

# Programming Assignment 1, Circle "Area"
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

    x = randx
    y = randy

    freddistance = x**2 + y**2
    #for statement

    if freddistance <= 1:
        insideCount = insideCount + 1
        #if statement

pi = (insideCount / numdarts) * 4
print("Estimated Area of the circle is:", pi)
print("This is the actual area is", math.pi)

#Dimension Names: C2D) S1 R2
#Equation: X^2 + y^2 < 1
#EC: A = pi*r^2
#Program intentions: Estimating the area in the circle
#Monte Carlo Method, pi is not given.

# Result 1) Darts(10000000)Estimated Area of the circle is: 3.1420512 - This is the actual area is 3.141592653589793
# The estimated and the correct answer are very close, the more darts thrown the more accurate it will be.

# Result 2) Darts(100)Estimated Area of the circle is: 3.48 - This is the actual area is 3.141592653589793
# The estimated and the correct answer are wildly off, the less darts thrown the less accurate it will be.

# Result 3) Darts(5000)Estimated Area of the circle is: 3.1688 - This is the actual area is 3.141592653589793
# The estimated and the correct answer are becoming closer, the more darts thrown closer they get.
