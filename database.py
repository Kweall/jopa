from re import X
import psycopg2
from psycopg2 import Error
import time

X = str(round(time.time()))[7:]

class Data_db:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="1",
            host="localhost",
            port="5432",
            connect_timeout=5)

        self.cursor = self.conn.cursor()
        # self.table_create()

    def __del__(self):
        pass

    def table_create(self):
        b = f'CREATE SCHEMA b{X}'
        print(b)
        self.cursor.execute(b)
        # self.cursor.execute(f'CREATE SCHEMA b{X}')
        self.cursor.execute(f'CREATE TABLE b{X}.b{X}\
                    (\
                    frame varchar(32),\
                    id varchar(32),\
                    bbox_left varchar(32),\
                    bbox_top varchar(32),\
                    bbox_w varchar(32),\
                    bbox_h varchar(32)\
                    );')
        self.conn.commit()
        # self.cursor.close()
        # self.conn.close()
        print("Соединение с PostgreSQL закрыто")

    def insert_data(self, frame_idx, id, bbox_left, bbox_top, bbox_w, bbox_h):
        self.cursor.execute(
            f'INSERT INTO b{X}.b{X} ("frame", "id", "bbox_left", "bbox_top", "bbox_w", "bbox_h") VALUES (%s, %s, %s, %s, %s, %s);',
            (int(frame_idx), int(id), int(bbox_left), int(bbox_top), int(bbox_w), int(bbox_h)))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        print("ЗАПИСИ ДОБАВЛЕНЫ В ТАБЛИЦУ b{X}.b{X}")

# a = Data_db()
# a.table_create()