def main():
    grocery_list = {}
    
    while True:
        try:
            item = input()
            if item == "":
                continue
            
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
                
        except EOFError:
            break

    print("")
    for item, count in sorted(grocery_list.items(), key=lambda x: x[0]):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
