import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))
    for row in reader:
        if '55' in row["nameError"]:
            print(
                f'У персонажа\t{row["characters"]}\tв игре\t{row["GameName"]}\t нашлась ошибка с кодом:\t {row["nameError"]}.\tДата фиксации:\t {row["date"]}')
    for row in reader:
        if '55' in row["nameError"]:
            row['nameError'] = 'Done'
            row['date'] = '0000-00-00'

with open('game_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['GameName', 'characters', 'nameError', 'date'], delimiter='$')
    w.writeheader()
    w.writerows(reader)
