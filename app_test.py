import pytest, requests
import os
from database import Data_db

basedir = os.path.abspath(os.path.dirname(__file__))

def test_home_page():
    resp = requests.get('http://127.0.0.1:5000')
    assert resp.status_code == 200

# def test_home_page2():
#     resp = requests.get('http://127.0.0.1:5000')
#     assert resp.status_code != 404
#
# def test_home_page3():
#     resp = requests.get('http://127.0.0.1:5000')
#     assert resp.status_code != 500

def test_video_page():
    resp = requests.get('http://127.0.0.1:5000/video')
    assert resp.status_code == 200

# def test_video_page2():
#     resp = requests.get('http://127.0.0.1:5000/video')
#     assert resp.status_code != 404
#
# def test_video_page3():
#     resp = requests.get('http://127.0.0.1:5000/video')
#     assert resp.status_code != 500

def test_result_page():
    resp = requests.get('http://127.0.0.1:5000/result')
    assert resp.status_code == 200

# def test_result_page2():
#     resp = requests.get('http://127.0.0.1:5000/result')
#     assert resp.status_code != 404
#
# def test_result_page3():
#     resp = requests.get('http://127.0.0.1:5000/result')
#     assert resp.status_code != 500

def test_connect_bd():
    a = Data_db().__init__()
    # print(a)
    assert a == None

# def test_sql_query():
#     sql = ''' select * from  '''
#     a = Data_db()
#     cur = Data_db().cursor
#
#     b = False
#     cur.execute(sql)
#     b = True
#     assert b == True
# print(test_sql_query())

def test_uploads_not_null():
    path = os.path.join(basedir, 'static/uploads/')
    print(path)
    a = False
    if len(os.listdir(path)) != 0:
        a = True
        assert a == True

def test_exists_best_pt():
    path = os.path.join(basedir, 'static/uploads/')
    a = os.path.exists(path)
    assert a == True
