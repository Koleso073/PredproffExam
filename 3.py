import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter='$'))

    check = True

    while check:
        c = 0
        s = []
        char = input('>>> ')
        if char != 'game':
            for row in reader:
                if char == row["characters"]:
                    s.append(row['GameName'])
                    c += 1
            if c == 0:
                print('Этого персонажа не существует')
            else:
                print(f'Персонаж {char} встречается в играх:')
                if len(s) > 5:
                    for i in range(5):
                        print(s[i])
                    print('и др.')
                else:
                    for i in range(len(s)):
                        print(s[i])
        else:
            check = False
