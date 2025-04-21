from datetime import datetime, time

SCHEDULE = [
    {"start": time(8, 30), "end": time(9, 15)},  # 1 урок
    {"start": time(9, 25), "end": time(10, 10)}, # 2 урок
    {"start": time(10, 25), "end": time(11, 10)},# 3 урок
    {"start": time(11, 25), "end": time(12, 10)},# 4 урок
    {"start": time(12, 30), "end": time(13, 15)},# 5 урок
    {"start": time(13, 35), "end": time(14, 20)},# 6 урок
    {"start": time(14, 40), "end": time(15, 25)},# 7 урок
    # Дополнительные уроки...
]

def get_number_declension(number, one, few, many):
    """Возвращает правильную форму слова в зависимости от числа."""
    if number % 10 == 1 and number % 100 != 11:
        return one
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        return few
    else:
        return many

def get_lesson_time():
    now = datetime.now().time()
    for i, lesson in enumerate(SCHEDULE, 1):
        start = lesson["start"]
        end = lesson["end"]
        if start <= now <= end:
            # Время до конца урока
            remaining_seconds = (datetime.combine(datetime.today(), end) - 
                                datetime.combine(datetime.today(), now)).seconds
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            minute_word = get_number_declension(minutes, "минута", "минуты", "минут")
            second_word = get_number_declension(seconds, "секунда", "секунды", "секунд")
            if minutes == 0:
                return f"До конца {i}-го урока осталось {seconds} {second_word}."
            return f"До конца {i}-го урока осталось {minutes} {minute_word} {seconds} {second_word}."
        elif now < start:
            # Время до начала урока
            remaining_seconds = (datetime.combine(datetime.today(), start) - 
                                datetime.combine(datetime.today(), now)).seconds
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            minute_word = get_number_declension(minutes, "минута", "минуты", "минут")
            second_word = get_number_declension(seconds, "секунда", "секунды", "секунд")
            if minutes == 0:
                return f"До начала {i}-го урока осталось {seconds} {second_word}."
            return f"До начала {i}-го урока осталось {minutes} {minute_word} {seconds} {second_word}."
    return "Уроки закончились или ещё не начались."
