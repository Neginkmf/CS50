def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:
        if s.isalnum():  
            if s[-1].isdigit() and s[:-1].isalpha():
                    return True
    return False

main()
