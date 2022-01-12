import os
import time
 
source = ["C:\users\APALON\OneDrive\Документы\projects\backupfiles\Storage"]
target_dir = ['C:\Users\APALON\OneDrive\Документы\projects\backupfiles\Archive'] 

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip' # создаем название и путь для архива

zip_command = 'zip -qr {0} {1}'.format(target, ''.join(source))  # -qr это параметры quitely and recursive 

if os.system(zip_command) == 0:
	print('Данные успешно скопированы в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')
