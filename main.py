import datetime
import timeimport playsound  # Установите: pip install playsound

def set_alarm():
    while True:
        try:
            alarm_hour = int(input("Введите час будильника (0-23): "))
            alarm_minute = int(input("Введите минуты будильника (0-59): "))
            if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
                break
            else:
                print("Неверный формат времени. Попробуйте еще раз.")
        except ValueError:
            print("Неверный формат времени. Попробуйте еще раз.")

    alarm_time = datetime.time(alarm_hour, alarm_minute)
    print(f"Будильник установлен на {alarm_time.strftime('%H:%M')}")

    while True:
        now = datetime.datetime.now().time()
        if now.hour == alarm_hour and now.minute == alarm_minute:
            print("Время пришло!")
            playsound.playsound("alarm_sound.wav")  # Замените на свой звуковой файл или метод
            break
        time.sleep(1) # Проверяем каждую секунду

def main():
    print("Простой будильник на Python")
    set_alarm()

if __name__ == "__main__":
    main()
