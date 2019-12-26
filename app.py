import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId

app = Flask(__name__,
            template_folder='templates')
app.config['MONGO_DBNAME'] = 'sugar_app'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route("/")
def home():
    food_groups = mongo.db.food_groups.find()
    foods = mongo.db.foods.find()
    return render_template('home.html', food_groups=food_groups, foods=foods)

@app.route('/get_foods')
def get_foods():
    return render_template('foods.html', foods=mongo.db.foods.find())

# @app.route('/get_drinks')
# def get_drink():
#     return render_template('drinks.html', drinks=mongo.db.drinks.find())

@app.route('/add_food')
def add_food():
    food_groups = mongo.db.food_groups.find()
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

@app.route('/edit_food/<food_id>')
def edit_food(food_id):
    food = mongo.db.foods.find_one({'_id': ObjectId(food_id)})
    food_groups = mongo.db.food_groups.find()
    return render_template('editfood.html', food=food, food_groups=food_groups)

@app.route('/update_food/<food_id>', methods=['POST'])
def update_food(food_id):
    foods_collection = mongo.db.foods
    foods_collection.update_one({'_id': ObjectId(food_id)},
                     {'$set':
                      {
                          'name': request.form.get('food_name'),
                          'group': request.form.get('food_group'),
                          'sugar_g_per_100g': float(request.form.get('sugar_g_per_100g')),
                          'sugar_g_per_serving': float(request.form.get('sugar_g_per_serving')),
                          'serving_description': request.form.get('serving_description'),
                          'reviewed': (request.form.get('reviewed') == "on"),
                      }
                      })
    return redirect(url_for('get_foods'))

#@app.route('/dbstats')
#def get_dbstats():
#    return "<h1>DB Stats</h1>"

#@app.route('/sort/<int:sort_id>')
#def sort(sort_id):
#    html = ""
#    if sort_id == 1:
#        html = "<h1>Sort id is Sugar: High to Low</h1>"
#    elif sort_id == 2:
#        html = "<h1>Sort id is Sugar: Low to High</h1>"
#    elif sort_id == 3:
#        html = "<h1>Sort id is A - Z</h1>"
#    elif sort_id == 4:
#        html = "<h1>Sort id is Z - A</h1>"
#    else:
#        html = "<h1>Error</h1>"
#    return html

@app.route('/search_catalog', methods=['POST', 'GET'])
def search_catalog():
    if request.method == "POST":
        food_group = request.form.get('food_group_select')
    else:
        food_group = 'All'
    
    if food_group == 'All':
        foods = mongo.db.foods.find()
    else:
        foods = mongo.db.foods.find({'group': food_group})

    if request.method == "POST":
        sugar_measure = request.form.get('sugar_measure_select')
        sort_by = request.form.get('sort_by_select')
    else:
        sugar_measure = 'serving'
        sort_by = 'H-L'
    
    if (sort_by == 'H-L') or (sort_by == 'L-H'):
        if sugar_measure == 'serving':
            if sort_by == 'H-L':
                foods_sorted = foods.sort("sugar_g_per_serving", DESCENDING)
            else:
                foods_sorted = foods.sort("sugar_g_per_serving")
        elif sugar_measure == '100g':
            if sort_by == 'H-L':
                foods_sorted = foods.sort("sugar_g_per_100g", DESCENDING)
            else:
                foods_sorted = foods.sort("sugar_g_per_100g")
    elif sort_by == 'A-Z':
        foods_sorted = foods.sort("name")
    elif sort_by == 'Z-A':
        foods_sorted = foods.sort("name", DESCENDING)
    else:
        foods_sorted = foods.sort("name")
    
    food_groups = mongo.db.food_groups.find()

    #return "<h1>Category {0}, Sugar Per {1}, Sort by {2}</h1>".format(food_group,sugar_measure,sort_by)
    return render_template('searchcatalog.html', food_group_select=food_group
                                                , sugar_measure_select=sugar_measure
                                                , sort_by_select=sort_by
                                                , food_groups=food_groups
                                                , foods=foods_sorted)

if __name__ == '__main__':
    #app.run(host=os.environ.get('IP'),
    #        port=int(os.environ.get('PORT')),
    #        debug=False)
    app.run(debug=True)
