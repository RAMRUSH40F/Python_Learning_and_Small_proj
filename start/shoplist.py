print('Расскуждения зумера в 2030=х :)')
shoplist = ['майонез','хлеб','яйца','молоко']   # На этом моменте мы создали список
print('Я должен сделать', len(shoplist), 'покупок.')

print('Покупки:', end=' ') #end = штука после фразы
for item in shoplist:
	print(item, end= ' ')

print('\n Также надо купить риса.')
shoplist.append('Рис')

print('Отсортирую-ка я свой список:')
shoplist.sort()
print('Отсортируемый список покупок выглядит так', shoplist)

print('Первое, что мне надо купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я вчера уже купил ', olditem)
print('Теперь мой список покупок  выглядит так:', shoplist)