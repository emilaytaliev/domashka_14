import sqlite3


def search_two_actors(name, name_two):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        query = f"""
                               SELECT "cast"
                               FROM netflix     
                               WHERE "cast" LIKE '%{name}%'  
                               AND "cast" LIKE '%{name_two}%'
                       """

        cursor.execute(query)
        result_in = cursor.fetchall()
        actors = []
        for i in result_in:
            actors.extend(i[0].split(', '))
        result = []
        for a in actors:
            if a not in [name, name_two]:
                if actors.count(a) > 2:
                    result.append(a)
        result = set(result)
        return result
print(search_two_actors('Jack Black', 'Dustin Hoffman'))



