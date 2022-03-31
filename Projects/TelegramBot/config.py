token = '5232909795:AAGd7ddL0QP88PgoGUIvcCal6WnZTGWk6OU'
sayhi = 'Рад видеть и служить вам. Напишите либо старт либо начать либо привет, чтобы увидеть,что я могу'
family_chat_id = -1001601086563
admin_chat_id = 397596258
import pickle
#
# randomrandom22 = ['Помидоры', 'Огурцы']
# with open('shoplistfile.bin', 'wb') as file:
#     pickle.dump(randomrandom22, file)

if __name__ == '__main__':
    with open('shoplistfile.bin', 'wb') as file:
        pickle.dump([ 'Помидоры' ], file)

    with open('shoplistfile.bin', 'rb') as file:
         shoplist_info = pickle.load(file)
         print(shoplist_info)
