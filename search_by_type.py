import sqlite3
import json

def get_type(type, year, genre):
    with sqlite3.connect("netflix.db") as connect:
        cursor = connect.cursor()
        query = f"""
                SELECT title, description
                FROM netflix   
                WHERE type = '{type}'  
                AND release_year = '{year}'
                AND listed_in = '{genre}'
                   
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



with open('type.json', 'w') as file:
    json.dump(get_type('Movie', 2014, 'Action & Adventure'), file)