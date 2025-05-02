import datetime
import playsound
import os
import time

def get_alarm_time():
    while True:
        alarm_input = input("Enter alarm time (HH:MM - 24 hour format): ")
        try:
            alarm_time = datetime.datetime.strptime(alarm_input, "%H:%M")
            return alarm_time.replace(
                year=datetime.datetime.now().year,
                month=datetime.datetime.now().month,
                day=datetime.datetime.now().day
            )
        except ValueError:
            print("Invalid format! Please use HH:MM (e.g., 14:30 for 2:30 PM).")

def play_sound():
    sound_file = "file.wav"
    try:
        if os.path.exists(sound_file):
            playsound.playsound(sound_file)
        else:
            print("\a" * 3)
    except Exception as e:
        print(f"Error playing sound: {e}. Using system beep instead.")
        print("\a" * 3)

def alarm_clock():
    print("WELCOME TO THE ALARM CLOCK ⏰ ")

    alarm_time = get_alarm_time()

    now = datetime.datetime.now()
    if alarm_time < now:
        alarm_time = alarm_time.replace(day=now.day + 1)
    
    print(f"Alarm set for {alarm_time.strftime('%H:%M')} "
          f"on {alarm_time.strftime('%Y-%m-%d')}.")
    
    while True:
        now = datetime.datetime.now()
        if now >= alarm_time:
            print(f"\n🚨 Alarm! time to wake up 🚨")
            play_sound()
            break
        time_remaining = (alarm_time - now).total_seconds()
        print(f"\rTime until alarm {int(time_remaining // 60)} minutes "
              f"{int(time_remaining % 60)} seconds.", end="")
        time.sleep(1)

        return input("Would you like to set another alarm? (yes/no): ").lower() == "yes"
    
def main():
    while True:
        if not alarm_clock:
            print("Thanks for using my alarm clock 😊")
            break

if __name__ == "__main__":
    main()