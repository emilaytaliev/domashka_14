import sqlite3


def get_tat(name):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        query = f"""
            SELECT title, country, release_year, listed_in, description
            FROM netflix
            WHERE title = '{name}'
            ORDER BY release_year DESC
            LIMIT 1
            """
        cursor.execute(query)
        result = cursor.fetchall()

        for i in result:
                return {
                    'title': i[0],
                    'country': i[1],
                    'release_year': i[2],
                    'listed_in': i[3],
                    'description': i[4],
                }










