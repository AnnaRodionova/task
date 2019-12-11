from connection import cur, conn


def execute_sql(query, data):
    try:
        cur.executemany(query, data)
        conn.commit()
        print('Success')
    except Exception as e:
        print(str(e))
        print('Failure')
    finally:
        conn.close()
