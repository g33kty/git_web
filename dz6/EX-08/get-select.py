import sqlite3

def get_items():
    for i in range(1,11):

        with open(f'queries-sql/query-{i}.sql', 'r') as f:
            sql = f.read()
            # print(sql)
        with sqlite3.connect('salary.db') as con:
            cur = con.cursor()
            cur.execute(sql)
            x = cur.fetchall()
            print(x)
            cur.close()
if __name__ == "__main__":
    get_items()