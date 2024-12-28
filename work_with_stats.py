import matplotlib.pyplot as plt
from work_with_words import DoneTest

class StatsManager:
    def __init__(self, user_id, user_done_tests: list[DoneTest]):
        self.user_id = user_id
        self.done_tests = user_done_tests

    # Создаёт и сохраняет график по пройденным тестам по пути.
    # Путь всегда находится в папке temp, и после отправки графика пользователю он оттуда удаляется.
    # Возвращает кортеж с двумя элементами: 0 - путь к графику, 1 - marks_count
    # Если тестов вообще нет, возвращает False
    def create_and_save_plot(self):
        if not self.done_tests: return False
        data = dict()
        marks_count = {5: 0,
                 4: 0,
                 3: 0,
                 2: 0}
        for test in self.done_tests:
            print(test.__dict__)
            day = test.day
            month = test.month
            try:
                data[f"{day}.{month}"] += test.mark
            except:
                data[f"{day}.{month}"] = test.mark
            marks_count[test.mark] += 1
        scores = list(data.values())
        dates = list(data.keys())

        plt.plot(dates, scores, color='black', marker='o', markersize=5)
        plt.xlabel("Даты")
        plt.ylabel("Оценки (их сумма)")
        path = f'temp/temp_stat_for_{self.user_id}.png'
        plt.savefig(path)
        plt.close()
        return (path, marks_count)