import time
import sys
# A basic cross-platform notification setup using standard print + bell
# In a real environment you might 'pip install plyer' or use 'osascript' on Mac

def pomodoro_timer(minutes):
    seconds = minutes * 60
    print(f"Starting Pomodoro timer for {minutes} minutes...")
    
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_format = f"{mins:02d}:{secs:02d}"
            # Print on the same line using carriage return
            print(timer_format, end='\r')
            time.sleep(1)
            seconds -= 1
            
        print("\nTime's up! Take a break.")
        # \a rings the terminal bell
        print("\a") 
        
    except KeyboardInterrupt:
        print("\nTimer stopped manually.")

if __name__ == "__main__":
    default_minutes = 25
    if len(sys.argv) > 1:
        try:
            default_minutes = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer for minutes.")
            sys.exit(1)
            
    pomodoro_timer(default_minutes)
