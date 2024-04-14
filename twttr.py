def vowel():
    vowels = "aAeEiIoOuU"
    name = input("Input: ")
    result = ''.join(text for text in name if text not in vowels)
    return result

print(vowel())
