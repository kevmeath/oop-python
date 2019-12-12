from math import sqrt
from math import pow


# vector class
class Vector3D:
    def __init__(self, x, y, z):  # create vector with x, y, z coordinates
        self.x = x  # set x
        self.y = y  # set y
        self.z = z  # set z

    def __add__(self, vector):  # vector + vector. (x+x1, y+y1, z+z1). Returns a new vector
        return Vector3D(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):  # vector - vector. (x-x1, y-y1, z-z1) Returns a new vector
        return Vector3D(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __mul__(self, n):  # vector * n. (x*n, y*n, z*n). Returns a new vector
        try:
            int(n)  # check if argument given is an integer
            return Vector3D(self.x * n, self.y * n, self.z * n)  # Return a new vector
        except TypeError:
            return Vector3D(self.x * n.x, self.y * n.y, self.z * n.z)  # Return a new vector

    def magnitude(self):  # print magnitude. Square root of x^2 + y^2 + z^2 . Returns a float
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)


# Creat vectors
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(2, 2, 2)

# Print v1 and v2
print("v1: ", v1)
print("v2: ", v2)

# Test vector functions
print("v1 + v2: ", v1 + v2)  # add vector to another vector
print("v1 - v2: ", v1 - v2)  # subtract vectors from another vector
print("v1 * v2: ", v1 * v2)  # multiply vector by another vector
print("v1 * 4: ", v1 * 4)  # multiply vector by integer
print("magnitude: ", v1.magnitude())  # print vector magnitude
