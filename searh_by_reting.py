import sqlite3


def by_rating(group):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        categories = {'children': ['G'],
                      'family': ['G', 'PG', 'PG-13'],
                      'adult': ['R', 'NC-17'],
                      }
        if group in categories:
            level = '\", \"'.join(categories[group])
            level = f'\"{level}\"'

        query = f"""
                            SELECT title, rating, description
                            FROM netflix     
                            WHERE rating IN ({level})  
                    """

        cursor.execute(query)
        result = cursor.fetchall()
        r = []
        for i in result:
            r.append({
                'title': i[0],
                'rating': i[1],
                'description': i[2],
            })
        return r
