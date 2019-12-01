import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__,
            template_folder='templates')
app.config['MONGO_DBNAME'] = 'sugar_app'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route('/get_foods')
def get_foods():
    return render_template('foods.html', foods=mongo.db.foods.find())

# @app.route('/get_drinks')
# def get_drink():
#     return render_template('drinks.html', drinks=mongo.db.drinks.find())

@app.route('/add_food')
def add_food():
    food_groups = mongo.db.food_group.find()
    return render_template('addfood.html', food_groups=food_groups)

# @app.route('/add_drink')
# def add_drink():
#     return render_template('adddrink.html', categories=mongo.db.drink_categories.find())

@app.route('/insert_food', methods=['POST'])
def insert_food():
    foods_collection = mongo.db.foods
    food = request.form.to_dict()
    food.pop('action')
    food['sugar_g_per_100g'] = float(food['sugar_g_per_100g'])
    food['sugar_g_per_serving'] = float(food['sugar_g_per_serving'])
    food['reviewed'] = False
    foods_collection.insert_one(food)
    return redirect(url_for('get_foods'))

if __name__ == '__main__':
    #app.run(host=os.environ.get('IP'),
    #        port=int(os.environ.get('PORT')),
    #        debug=False)
    app.run(debug=True)