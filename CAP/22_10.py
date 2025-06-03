def remove_empty_columns(input_table):
    num_rows = len(input_table)
    num_cols = len(input_table[0]) if num_rows > 0 else 0
    columns_to_remove = [col for col in range(num_cols)
                         if all(row[col] is None for row in input_table)]
    return [[row[col] for col in range(num_cols)
             if col not in columns_to_remove] for row in input_table]


def remove_duplicate_rows(input_table):
    seen_rows = set()
    return [row for row in input_table if tuple(row)
            not in seen_rows and not seen_rows.add(tuple(row))]


def process_row(row):
    new_row = []
    for i, value in enumerate(row):
        if i == 0:
            new_row.append(value[-2:] + "/" + value[3:5] + "/" + value[:2])
        elif i == 1:
            new_row.append("Y" if value == "Выполнено" else "N")
        elif i == 3:
            new_row.append(value.replace('@', '[at]'))
        elif value is not None:
            new_row.append(value.split()[-1])
    return new_row


def process_table(input_table):
    output_table = []
    for row in input_table:
        output_table.append(process_row(row))
    return output_table


def main(input_table):
    input_table = remove_empty_columns(input_table)
    input_table = remove_duplicate_rows(input_table)
    output_table = process_table(input_table)
    return output_table


print(main([[None, '01/10/02', 'Выполнено', None, 'Макар З. Зовеций', 'zovezij75@rambler.ru'],
            [None, '23/03/01', 'Не выполнено', None, 'Одиссей Ц. Чумидук', 'odissej10@gmail.com'],
            [None, '16/04/01', 'Не выполнено', None, 'Тамерлан Р. Тувберг', 'tamerlan69@mail.ru'],
            [None, '16/04/01', 'Не выполнено', None, 'Тамерлан Р. Тувберг', 'tamerlan69@mail.ru'],
            [None, '16/04/01', 'Не выполнено', None, 'Тамерлан Р. Тувберг', 'tamerlan69@mail.ru']]))
