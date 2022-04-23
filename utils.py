from search_title import get_tat
from release_year import rel_yaer
from searh_by_reting import by_rating
from flask import Flask, jsonify

app = Flask(__name__)

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



app.config['JSON_AS_ASCII'] = False





app.run()