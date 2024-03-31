def main():
    text = input("Please input a text with smile or frown emojis: ")
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

print(main()) 
