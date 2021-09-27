#Task1

print(type(15*3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#Task2

my_l = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_l = []
for elem in my_l:
    if elem.isdigit():
        new_l.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_l.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_l.append(elem)

out_info = ' '.join(new_l)
print(out_info)

sym_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        sym_idxs.append(idx)

for idx in range(len(sym_idxs)):
    if idx % 2 == 0:
        sym_idxs[idx] = sym_idxs[idx] + 1
    else:
        sym_idxs[idx] = sym_idxs[idx] - 1

for del_idx in reversed(sym_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx+1:]

#Task4

incorrect_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                  'директор аэлита']
for position in incorrect_list:
    print('Привет', position.split()[-1].title())

#Task5

goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')

goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1, 23.7]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')

print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])

