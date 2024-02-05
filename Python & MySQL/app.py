from database import cursor, db

def add_logs(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


# add_logs('This is log one', 'Brian')
# add_logs('This is log two', 'Ngoya')
# add_logs('This is log three', 'Smith')

def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)
        # print(row[1])

# get_logs()

def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)
        # print(row[1])

# get_log(2)


def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log Updated")

# update_log(2, "Updated log")
# get_logs()


def delete_log(id, text):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log Removed")

# delete_log(2, "Log Deleted")
# get_logs()