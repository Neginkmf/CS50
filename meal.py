def main():
    time = input("Enter the current time in 24-hour format (e.g., 07:30): ")
    time_in_hours = convert(time)
    if 7.0 <= time_in_hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= time_in_hours <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= time_in_hours <= 19.0:
        print("It's dinner time!")

def convert(time):
    hours, minutes = map(int, time.split(':'))
    total_hours = hours + minutes / 60
    return total_hours

if __name__ == "__main__":
    main()
