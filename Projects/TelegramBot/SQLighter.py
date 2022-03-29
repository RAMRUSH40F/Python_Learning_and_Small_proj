import sqlite3

class SQLighter:

    def __init__(self, database,message):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.message = message

    # def get_scores(self):
    #     """ Получаем все строки """
    #     with self.connection:
    #         return self.cursor.execute('SELECT * FROM scores').fetchall()

    #  [('397596258', 'Рамиль', 0, '.', '.'), ('1008715504', 'Эльмира', 0, '.', '.'), ('1914578771', 'Камила', 0, '.', '.')]
    def get_all_scores(self):
        """ Получаем все строки """
        with self.connection:
            base = self.cursor.execute('SELECT name,score,place,time FROM scores').fetchall()
            res = []
            for row in base :
                res.append(f'{row[0]} - {row[1]} балл(-ов). В последний раз {row[2]} он убирал {row[3]}')
            return res

    # db.commit

    # def get_your_score(self):
    #     """ Получаем одну строку с номером rownum """
    #     with self.connection:
    #         return self.cursor.execute('SELECT * FROM scores WHERE id = ?', self.message.chat.id).fetchall()


    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()


