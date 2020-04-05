import sqlite3
import os
import inspect
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventmanage.settings')

import django
django.setup()

import inventapp.models as models

modelNames = list()
for name, obj in inspect.getmembers(models, inspect.isclass):
    modelNames.append(name.lower())

# Show Objects list
def show_objects_list(modelClass):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query = '''select * from {}'''.format(modelClass)
    queryh = '''select name from pragma_table_info("{}")'''.format(modelClass)

    cur.execute(query)
    r = cur.fetchall()
    cur.execute(queryh)
    h = cur.fetchall()
    print(h)
    conn.commit()
    cur.close()
    conn.close()
    return (r, h)

def show_object_details(modelClass, objectID):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query = '''select * from {} where id = {}'''.format(modelClass, objectID)
    queryh = '''select name from pragma_table_info("{}")'''.format(modelClass)
    cur.execute(query)
    r = cur.fetchall()
    cur.execute(queryh)
    h = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return (r, h)

def model_objects(modelClass, objectID):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query = '''select * from {} where id = {}'''.format(modelClass, objectID)
    queryh = '''select name from pragma_table_info("{}")'''.format(modelClass)
    cur.execute(query)
    r = cur.fetchall()
    cur.execute(queryh)
    h = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return (r, h)

def save_object(modelClass, values):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    values = tuple(values)
    query = '''insert into {} values{}'''.format(modelClass, values)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def update_object(modelClass, values, objectId):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    values = ', '.join(values)
    print(values)
    query = '''update {} set {} where id = {}'''.format(modelClass, values, objectId)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def delete_object(modelClass, objectId):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    query = '''delete from {} where id = {}'''.format(modelClass, objectId)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
