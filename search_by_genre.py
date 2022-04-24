import sqlite3


def get_genre(genre):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        query = f"""
                SELECT title, description
                FROM netflix   
                WHERE listed_in = '{genre}'  
                AND release_year > 2010
                LIMIT 10
                """
        cursor.execute(query)
        result = cursor.fetchall()
        range_in = []
        for i in result:
            range_in.append({
                'title': i[0],
                'description': i[1],
            })
        return range_in
