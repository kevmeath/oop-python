binary = str(input("Enter a binary number: "))
decimal = 0

for i in range(len(binary), 0, -1):
    if binary[i-1] == "1":
        decimal = decimal + 2**(len(binary)-i)

print("Decimal: ", decimal)
