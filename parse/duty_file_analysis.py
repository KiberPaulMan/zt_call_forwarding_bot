from pathlib import Path
import pandas
import datetime as dt

from databook import phonebook

weekday = {
    dt.datetime(1900, 1, 1, 0, 0): 'Вс',
    dt.datetime(1900, 1, 2, 0, 0): 'Пн',
    dt.datetime(1900, 1, 3, 0, 0): 'Вт',
    dt.datetime(1900, 1, 4, 0, 0): 'Ср',
    dt.datetime(1900, 1, 5, 0, 0): 'Чт',
    dt.datetime(1900, 1, 6, 0, 0): 'Пт',
    dt.datetime(1900, 1, 7, 0, 0): 'Сб',
}


def get_excel_data(path: Path):
    excel_file = Path(path)
    return pandas.read_excel(excel_file, sheet_name='Дежурства')


def parse_excel_data(excel_data):
    parse_data = {
        'days_of_the_week': [],
        'numbers_of_the_month': [],
        list(phonebook.keys())[0]: [],
        list(phonebook.keys())[1]: [],
        list(phonebook.keys())[2]: [],
        list(phonebook.keys())[3]: [],
    }

    for out_index, out_data in enumerate(excel_data.iterrows()):
        if out_index == 4:  # дни недели (Сб, Вс, ...)
            for data in out_data[1][2:33]:
                if isinstance(data, dt.datetime):
                    parse_data['days_of_the_week'].append(weekday[data])

        if out_index == 5:  # числа месяца
            for data in out_data[1][2:33]:
                if isinstance(data, int):
                    parse_data['numbers_of_the_month'].append(data)

        if out_index == 6:  # Русаков Виктор
            for data in out_data[1][2:33]:
                data = data if isinstance(data, int) else 0
                parse_data[list(phonebook.keys())[0]].append(data)

        # if out_index == 7:  # Шайкамалов Александр
        #     for data in out_data[1][2:33]:
        #         data = data if isinstance(data, int) else 0
        #         parse_data[list(phonebook.keys())[3]].append(data)

        if out_index == 7:  # Кохан Антон
            for data in out_data[1][2:33]:
                data = data if isinstance(data, int) else 0
                parse_data[list(phonebook.keys())[2]].append(data)

        if out_index == 8:  # Эрднев Влад
            for data in out_data[1][2:33]:
                data = data if isinstance(data, int) else 0
                parse_data[list(phonebook.keys())[1]].append(data)

    return parse_data


def get_duty(parsed_data, username):
    current_day = dt.datetime.today().day
    result = f'{phonebook[username][1]}: \n'

    for idx, data in enumerate(parsed_data[username]):

        out_data = f"{parsed_data['numbers_of_the_month'][idx]} - {parsed_data['days_of_the_week'][idx]}"

        if data != 0:
            if parsed_data['numbers_of_the_month'][idx] < current_day:
                result += f"<s>{out_data}</s>\n"

            elif parsed_data['numbers_of_the_month'][idx] > current_day:
                result += f'{out_data}\n'

            else:
                result += out_data + '&#128526;\n'

    return result[:-1]
