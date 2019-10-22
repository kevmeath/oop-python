from string import ascii_letters
vowels = "AaEeIiOoUu"


def vowel_consonant(sentence):
    vowel_count = 0
    consonant_count = 0

    for c in sentence:
        if c in vowels:
            vowel_count += 1
        elif c in ascii_letters:
            consonant_count += 1

    print("This sentence has", vowel_count, "vowels and", consonant_count, "consonants.")


sentence_input = input("Enter a sentence: ")
vowel_consonant(sentence_input)