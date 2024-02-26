import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))

    s = []

    for row in reader:
        s.append(row['GameName'])

    sg = []

    for row in reader:
        count = 0
        for g in range(len(s)):
            if row['GameName'] == s[g]:
                count += 1
        sg.append(count)

    nr = []
    count = 0
    for row in reader:
        row['counter'] = str(sg[count])
        nr.append(row)
        count += 1

with open('game_counter.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['GameName', 'characters', 'nameError', 'date', 'counter'], delimiter='$')
    w.writeheader()
    w.writerows(nr)

