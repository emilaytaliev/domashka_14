import sqlite3

with sqlite3.connect("netflix.db") as connect:
    cursor = connect.cursor()
    query = """
        SELECT title, country, release_year, listed_in, description
        FROM netflix
        """
    cursor.execute(query)
    result = cursor.fetchall()


    # поиск по названию фильма
    def get_tat(name):

        for i in result:
            if name in i[0]:
                return {
                    'title': i[0],
                    'country': i[1],
                    'release_year': i[2],
                    'listed_in': i[3],
                    'description': i[4],
                }








