decimal = int(input("Enter a decimal number: "))
binary = ""

def reverse(s):
    reverse = ""
    for i in range(len(s), 0, -1):
        reverse = reverse + str(s[i-1])
    return reverse

while decimal != 0:
    binary = binary + str(decimal % 2)
    decimal = int(decimal / 2)

print("Binary: ", reverse(binary))
