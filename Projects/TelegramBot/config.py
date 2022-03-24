token = '5232909795:AAGd7ddL0QP88PgoGUIvcCal6WnZTGWk6OU'
import pickle
with open('shoplistfile.bin', 'rb') as file:
    shoplist_info = pickle.load(file)
print(shoplist_info)