from datetime import datetime as dt


def Les_time():
    second_now = dt.now().hour * 3600 + dt.now().minute * 60 + dt.now().second

    courrt1 = (30600,
               33300,
               33900,
               36600,
               37500,
               40200,
               41100,
               43800,
               45000,
               47700,
               48900,
               51600,
               117000)

    for i in range(len(courrt1) - 1):
        if second_now > courrt1[i - 2] or second_now < 2 * 3600:
            return "Уроки кончились"
        elif second_now > courrt1[i] and second_now < courrt1[i + 1]:
            secs = (courrt1[i + 1] - second_now)
            hours = (secs // 3600)
            minutes = ((secs - hours * 3600) // 60)
            second = ((secs - 3600 * 3600) % 60)
            full_time = (hours, minutes, second, i)

            return full_time


def make_text_for_time():
    full_time = Les_time()
    if full_time == 'Уроки кончились':
        return 'Уроки кончились'
    if full_time[3] % 2 == 0:
        prefix = 'До звонка на урок осталось'
    else:
        prefix = 'До звонка с урока осталось'
    if full_time[1] == 1:
        trin = 'Час'
    elif full_time[1] <= 4:
        trin = 'Часа'
    elif full_time[1] <= 12:
        trin = 'Часов'
    if full_time[2] % 10 == 1 and full_time[2] % 100 != 11:
        minut = 'Минута'
    elif 2 <= full_time[2] % 10 <= 4 and (full_time[2] % 100 < 10 or full_time[2] % 100 >= 20):
        minut = 'Минуты'
    else:
        minut = 'Минут'
    if full_time[2] % 10 == 1 and full_time[2] % 100 != 11:
        seconds = 'Секунда'
    elif 2 <= full_time[2] % 10 <= 4 and (full_time[2] % 100 < 10 or full_time[2] % 100 >= 20):
        seconds = 'Секунды'
    else:
        seconds = 'Секунд'
    return f'{prefix} {full_time[0]} {trin} {full_time[1]} {minut} {full_time[2]} {seconds}'

