def main():
    text = input("please input a text with smile or frown emojies: ")
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

print(main()) 
