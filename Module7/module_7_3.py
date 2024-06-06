# функция для определения победителя
def res(sc_1, tt_1, sc_2, tt_2):
    if sc_1 > sc_2 or sc_1 == sc_2 and tt_1 > tt_2:
        result = 'Победа команды Мастера кода!'
    elif sc_1 < sc_2 or sc_1 == sc_2 and tt_1 < tt_2:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


# входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
challenge_result = res(score_1, team1_time, score_2, team2_time)


# Использование %
result_1 = "В команде Мастера кода участников: %d !" % team1_num
result_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

print(result_1)
print(result_2)


# Использование format()
result_3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result_4 = "Волшебники данных решили задачи за {:.1f} с !".format(team1_time)

print(result_3)
print(result_4)


# Использование f-строк
result_5 = f"Команды решили {score_1} и {score_2} задач."
result_6 = f"Результат битвы: {challenge_result}"
result_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

print(result_5)
print(result_6)
print(result_7)
