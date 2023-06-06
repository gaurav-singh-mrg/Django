from django.db import connection


def customsql(self, qry, fetchall=False):
    cursor = connection.cursor()
    cursor.execute(qry)
    if fetchall:
        row = cursor.fetchall()
    else:
        row = cursor.fetchone()
    return row
