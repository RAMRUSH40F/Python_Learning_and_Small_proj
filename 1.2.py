
objects = [1, 2, 1, 5, True, False, True, 'false', [], [1, 2], [1, 2]]
print(len(set(map(id, objects))))
#---------------------------------

fin = []

fin.append(objects[0])
print(objects[0], 'добавлен', fin)

k = 1;

for i in range(k, len(objects)):
    k = i + 1
    print('Проверяем объект', objects[i])

    t: int = 0;
    res = 0;

    while (len(fin) > t) & (res == 0):
        # print('длина fin =',len(fin), 't=', t)
        if objects[i] is fin[t]:
            res += 1
            print(objects[i], 'не добавлен, он совпадает с ', fin[t])

        t += 1
    if (res==0):
        fin.append(objects[i]);
        print(objects[i], 'добавлен, новый ряд: ', fin, 't=', t)
print(len(fin))
#-------------------------------------------------
spisok = set()
for i in objects:
    spisok.add(id(i))

print(len(y))