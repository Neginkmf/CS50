def main():
    while True:
        try:
            fraction = input("Enter fuel fraction (X/Y): ")
            x, y = map(int, fraction.split('/'))
            if x > y:
                raise ValueError
            percentage = (x / y) * 100
            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(str(round(percentage)) + '%')
            break
        except ValueError:
            print("Invalid input. Please enter a valid fraction.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a valid fraction.")

main()
