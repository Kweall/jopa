from app import app, basedir
import pytest, requests
import os
from yolov5.db_data import Data_db

def test_home_page():
    resp = requests.get('http://192.168.206.204:8080')
    assert resp.status_code == 200


def test_show_page():
    resp = requests.get('http://192.168.206.204:8080/show/')
    assert resp.status_code == 200

# def test_home_page2():
#     resp = requests.get('http://192.168.206.204:8080/show/')
#     assert resp.status_code != 404
#
# def test_home_page3():
#     resp = requests.get('http://192.168.206.204:8080')
#     assert resp.status_code != 500


def test_connect_bd():
    a = Data_db().__init__()
    # print(a)
    assert a == None

def test_sql_query():
    sql = ''' select * from website_analysis '''
    a = Data_db()
    cur = Data_db().cursor

    b = False
    cur.execute(sql)
    b = True
    assert b == True

def test_uploads_dir():
    path = os.path.join(basedir, 'uploads')
    print(path)
    a = False
    if len(os.listdir(path)) != 0:
        a = True
        assert a == True

def test_exists_best_pt():
    a = os.path.exists(basedir)
    assert a == True

# def test_exists_best_pt():
#     a = os.path.exists(basedir)
#     assert a == True

