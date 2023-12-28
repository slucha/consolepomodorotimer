import time

def start_timer(duration_in_minutes):
    duration_in_seconds = int(duration_in_minutes * 60)  # Convert to integer
    try:
        for remaining in range(duration_in_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
        print("\nTime's up!")
    except KeyboardInterrupt:
        print("\nTimer cancelled.")

def main():
    try:
        user_input = input("Enter the desired length of the timer in minutes: ")
        duration_in_minutes = float(user_input)
        print(f"Timer is set for {duration_in_minutes} minutes.")
        start_timer(duration_in_minutes)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()