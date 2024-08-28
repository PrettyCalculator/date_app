import sqlite3


def check_userid(user_number):
    con = sqlite3.connect('db/db')
    if con.cursor().execute(f'SELECT user_number FROM users WHERE user_number = {user_number}').fetchall():
        return True
    return False
