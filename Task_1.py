"""
Подходило 1 сентября, университет готовился к наплыву абитуриентов. Так вышло, что Вы, как программист, должны были
помочь в отборе тех абитуриентов, кто поступит в университет на конкурсной основе на специальность программиста.
Схема была проста: есть абитуриент, у него есть результаты сданных экзаменов по математике, русскому и информатике.
Соответственно, у каждого потенциального студента есть сумма баллов по этим экзаменам. Также есть дополнительные
(extra_scores) аллы: за волонтерство, участие в олимпиадах и другие активности.
Вам нужно отобрать 20 человек, у которых суммарный балл выше, чем у других. В случае, если не получается однозначно
определить 20 человек (например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют на 20 место в
списке, стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""

candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Igor", "scores": {"math": 59, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Saha", "scores": {"math": 39, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Ivan", "scores": {"math": 99, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "artem", "scores": {"math": 58, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Renat", "scores": {"math": 38, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 98, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Kiril", "scores": {"math": 57, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Azamat", "scores": {"math": 73, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Sergei", "scores": {"math": 62, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Andrei", "scores": {"math": 48, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Yra", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Nikita", "scores": {"math": 12, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Dima", "scores": {"math": 58, "russian_language": 62, "computer_science": 40}, "extra_scores": 0},
    {"name": "Vladimir", "scores": {"math": 33, "russian_language": 65, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petia", "scores": {"math": 92, "russian_language": 43, "computer_science": 34}, "extra_scores": 1},
    {"name": "Oleg", "scores": {"math": 58, "russian_language": 22, "computer_science": 40}, "extra_scores": 0},
    {"name": "Stepa", "scores": {"math": 33, "russian_language": 95, "computer_science": 42}, "extra_scores": 2},
    {"name": "Viktor", "scores": {"math": 92, "russian_language": 83, "computer_science": 34}, "extra_scores": 1},
    {"name": "Ilia", "scores": {"math": 58, "russian_language": 12, "computer_science": 50}, "extra_scores": 0},
]


def find_top_20(candidates: dict):
    """
    Функция обрабатывает данные студентов и возвращает имя список с колчичеством баллом отсортированными по убыванию
    :param candidates словарь с данными студентов:
    :return отсортированый список 21 студента: :
    """
    lens = 0
    total_score = []
    for candidate in candidates:
        lens += 1
        name = candidate["name"]
        math = candidate["scores"]["math"]
        russian_language = candidate["scores"]["russian_language"]
        computer_science = candidate["scores"]["computer_science"]
        extra_scores = candidate["extra_scores"]
        total_score.append((name, math + russian_language + computer_science + extra_scores))
        total_score = sorted(total_score, key=lambda x: x[1], reverse=True)
    return total_score[:21:]


def validation():
    """
    Функция поверки результатов отбора если 20 и 21 студент имеют одинаковое количества баллов то проходит проверка
    на профильные предменты
    :return отсортированый список студентов:
    """
    # Получение списка облаботанного функцией find_top_20
    data = find_top_20(candidates)
    # Сравнение результатов 20 и 21 студентов
    if data[19][1] == data[20][1]:
        # Если значение равны получаем имена и результаты профильных предметов
        for candidats in candidates:
            if candidats["name"] == data[19][0]:
                name_studen1 = candidats["name"]
                math = candidats["scores"]["math"]
                computer_science = candidats["scores"]["computer_science"]
                student1_profil = math + computer_science
            elif candidats["name"] == data[20][0]:
                name_studen2 = candidats["name"]
                math = candidats["scores"]["math"]
                computer_science = candidats["scores"]["computer_science"]
                student2_profil = math + computer_science
        # Сравниваеи результаты по  профильным предметам
        if student1_profil < student2_profil:
            # Если студент 21 из списка набрал больше баллов по профильныи предметам меняем его с 20
            result = []
            result.append(data[20])
            data.pop(20)
            data.pop(19)
            data.extend(result)
            # Выводим сообщение о замене
            print(
                f'ВАЖНО!!!!!!!Студент  {name_studen1} был заменен студентом {name_studen2} так как '
                f'по профильным предметам набрал меньше баллов')
            return data
    else:
        return data[:20:]


if __name__ == '__main__':
    i = 1
    sor_data = validation()
    for data in sor_data:
        print(f'Студент {i} : Имя {data[0]}  с результатом {data[1]}')
        i += 1
