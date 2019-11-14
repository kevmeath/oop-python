# def gcd(large, small):

# def lcm(num1, num2):

# def addFrac(fraction1, fraction2):

# def subFrac(fraction1, fraction2):

# def simplify(fraction):

tuple1_str = input("Enter tuple 1: ")

while True:
    try:
        tuple1 = tuple(tuple1_str)
    except ValueError:
        tuple1_str = input("Enter tuple 1 as 2 integer separated by a comma (1,2): ")
    else:
        break

print(tuple1)