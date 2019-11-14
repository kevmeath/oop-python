number_word_dict = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

number = input("Enter numbers: ")

for digit in number:
    print(number_word_dict.get(digit))
