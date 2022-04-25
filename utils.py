from search_title import get_tat
from release_year import rel_yaer
from searh_by_reting import by_rating
from search_by_genre import get_genre
from flask import Flask, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# поиск по названию фильма
@app.route("/movie/<title>")
def get_title(title):
    movie = get_tat(title)
    return jsonify(movie)


# поиск по диапазону лет выпуска
@app.route("/movie/<start>/to/<finish>")
def get_release(start, finish):
    years = rel_yaer(start, finish)
    return jsonify(years)


#поиск по категориям
@app.route("/rating/<type>")
def get_categories(type):
    catefor = by_rating(type)
    return jsonify(catefor)

# поиск по жанрам
@app.route("/genre/<genre>")
def by_get_genre(genre):
    genre_in = get_genre(genre)
    return jsonify(genre_in)




app.run()