from math import sqrt
from math import pow


# vector class
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vector):  # vector + vector. (x+x1, y+y1, z+z1). Returns a new vector
        return Vector3D(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):  # vector - vector. (x-x1, y-y1, z-z1) Returns a new vector
        return Vector3D(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, n):  # vector * n. (x*n, y*n, z*n). Returns a new vector
        return Vector3D(self.x * n, self.y * n, self.z * n)

    def magnitude(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

# Creat vectors
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(2, 2, 2)

# Test vector functions
print("v1 + v2: ", v1 + v2)
print("v1 - v2: ", v1 - v2)
#print("v1 * v2: ", v1 * v2)
print("v1 * 4: ", v1 * 4)
print("magnitude: ", v1.magnitude())
