import csv


def hash_f(s: str):
    """
    Описание функции hash_f

    alp - алфавит
    m, p - выбранные числа
    """
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp += alp.upper() + "1234567890:-'. "
    d = {l: i for i, l in enumerate(alp, 1)}
    m = 10 ** 9 + 9
    p = 68
    hash_val = 0
    p_pow = 1
    for c in s:
        hash_val = (hash_val + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_val)


s = []
with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))
    for row in reader:
        row = str(hash_f(row[0] + row[1])) + '$' + row[0] + '$' + row[1] + '$' + row[2] + '$' + row[3]
        s.append(row.split('$'))

with open('game_with_hash.csv', 'w', newline='', encoding='utf8') as file:
    w = csv.writer(file, delimiter='$')
    w.writerow(['hash', 'GameName', 'characters', 'nameError', 'date'])
    w.writerows(s)
