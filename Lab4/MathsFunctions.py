def createTuple(tupleString):
    for i in range(len(tupleString)):
        if tupleString[i] == ',':
            return int(tupleString[:i]), int(tupleString[i + 1:])

# def gcd(large, small):

# def lcm(num1, num2):

# def addFrac(fraction1, fraction2):

# def subFrac(fraction1, fraction2):

# def simplify(fraction):

tuple1 = createTuple(input("Enter tuple 1: "))
tuple2 = createTuple(input("Enter tuple 2: "))
print(tuple1, tuple2)