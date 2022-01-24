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


def calculate_total_score(candidates: dict) -> list:
    """
    Функция обрабатывает данные студентов и возвращает имя список с колчичеством баллом отсортированными по убыванию
    :param candidates словарь с данными студентов:
    :return отсортированый список 21 студента: :
    """
    total_score = []
    for candidate in candidates:
        name = candidate.get("name", "")
        math = candidate.get("scores", 0).get("math", 0)
        russian_language = candidate.get("scores", 0).get("russian_language", 0)
        computer_science = candidate.get("scores", 0).get("computer_science", 0)
        extra_scores = candidate.get("extra_scores", 0)
        total_score.append((name, math + russian_language + computer_science + extra_scores))
    return sorted(total_score, key=lambda x: x[1], reverse=True)


def find_top_20(candidates: dict) -> list:
    """
    Функция поверки результатов отбора если 20 и 21 студент имеют одинаковое количества баллов то проходит проверка
    на профильные предменты
    :return отсортированый список студентов:
    """
    total_score = calculate_total_score(candidates)
    conflicated_condidate = None

    if total_score[20] and total_score[21] and total_score[20][1] == total_score[21][1]:
        conflicated_candidates = [candidate for candidate in total_score[20:] if candidate[1] == total_score[20][1]]
        for candiate in conflicated_candidates:
            name = candiate[0]
            math = candidates[name]["scores"]["math"]
            computer_science = candidates[name]["scores"]["computer_science"]
            if not conflicated_condidate or conflicated_condidate[1] < math + computer_science:
                conflicated_condidate = (name, math + computer_science, candiate[1])

    if conflicated_condidate:
        total_score[20] = (conflicated_condidate[0], conflicated_condidate[1])
    return total_score[:20]



if __name__ == '__main__':
    i = 1
    sor_data = find_top_20(candidates)
    for data in sor_data:
        print(f'Студент {i} : Имя {data[0]}  с результатом {data[1]}')
        i += 1