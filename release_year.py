import sqlite3


def rel_yaer(beginning,finish):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        query = f"""
                SELECT title, release_year
                FROM netflix     
                WHERE release_year BETWEEN {beginning} AND {finish}
                LIMIT 100       
                """
        cursor.execute(query)
        result = cursor.fetchall()
        range_in = []
        for i in result:
            range_in.append({
                'title': i[0],
                'release_year': i[1],
            })
        return range_in










