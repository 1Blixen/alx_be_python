from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Save current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Save future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()