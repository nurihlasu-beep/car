# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from datetime import date, datetime, time, timedelta

today = date.today() print("1.", today.strftime("%d.%m.%Y"))

now = datetime.now() print("2.", now.strftime("%H:%M"))

exam_date = date(2026, 12, 20) print("3.", exam_date)

date_string = "08.03.2027" parsed_date = datetime.strptime(date_string, "%d.%m.%Y") print("4.", parsed_date)

future_date = today + timedelta(days=30) print("5.", future_date.strftime("%d.%m.%Y"))

input_str = "01.09.2026" user_date = datetime.strptime(input_str, "%d.%m.%Y").date() diff = today - user_date if diff.days > 0: print(f"6. Прошло дней: {diff.days}") elif diff.days == 0: print("6. Это сегодня!") else: print(f"6. До даты осталось дней: {-diff.days}")

deadline = date(2026, 11, 15) delta_dl = deadline - today if delta_dl.days == 0: print("7. Дедлайн сегодня") elif delta_dl.days > 0: print(f"7. До дедлайна осталось дней: {delta_dl.days}") else: print(f"7. Дедлайн просрочен на дней: {-delta_dl.days}")

purchase_date = date(2026, 10, 1) sub_end = purchase_date + timedelta(days=90) print("8. Окончание подписки:", sub_end)

birth_date = datetime.strptime("15.05.2008", "%d.%m.%Y").date() age = today.year - birth_date.year if (today.month, today.day) < (birth_date.month, birth_date.day): age -= 1 print("9. Полный возраст:", age)

start_proj = date(2026, 10, 1) end_proj = date(2026, 10, 25) if end_proj < start_proj: print("10. Ошибка: конец раньше начала") else: print("10. Длительность проекта:", (end_proj - start_proj).days, "дней")

current_day = today added_work_days = 0 while added_work_days < 5: current_day += timedelta(days=1) if current_day.weekday() < 5: added_work_days += 1 print("11. Дата доставки:", current_day.strftime("%d.%m.%Y"))


tasks = [ {"title": "Лабораторная по физике", "deadline": date(2026, 10, 20)}, {"title": "Проект по Python", "deadline": date(2026, 11, 5)}, ] print("12. Планировщик задач:") for t in tasks: d_left = (t["deadline"] - today).days if d_left > 0: status = f"осталось {d_left} дн." elif d_left == 0: status = "сегодня" else: status = f"просрочено на {-d_left} дн."
 print(f" - {t['title']}: {status}")
