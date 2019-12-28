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
        foods_sorted = foods.sort("sugar_g_per_serving")
    
    food_groups = mongo.db.food_groups.find()

    return render_template('searchcatalog.html', food_group_select=food_group
                                                , sugar_measure_select=sugar_measure
                                                , sort_by_select=sort_by
                                                , food_groups=food_groups
                                                , foods=foods_sorted)

@app.route('/add_to_catalog')
def add_to_catalog():
    food_groups = mongo.db.food_groups.find()
    return render_template('addtocatalog.html', food_groups=food_groups)

@app.route('/insert_food', methods=['POST'])
def insert_food():
    foods_collection = mongo.db.foods
    food = request.form.to_dict()
    food.pop('action')
    food['sugar_g_per_100g'] = float(food['sugar_g_per_100g'])
    food['sugar_g_per_serving'] = float(food['sugar_g_per_serving'])
    food['reviewed'] = False
    foods_collection.insert_one(food)
    return redirect(url_for('search_catalog'))

@app.route('/edit_catalog')
def edit_catalog():
    foods = mongo.db.foods.find()
    foods_sorted = foods.sort("sugar_g_per_serving")
    food_groups = mongo.db.food_groups.find()
    return render_template('editcatalog.html', food_group_select='All'
                                              , sugar_measure_select='serving'
                                              , sort_by_select='H-L'
                                              , food_groups=food_groups
                                              , foods=foods_sorted)

@app.route('/search_edit_catalog', methods=['POST'])
def search_edit_catalog():
    food_group = request.form.get('food_group_select')
    
    if food_group == 'All':
        foods = mongo.db.foods.find()
    else:
        foods = mongo.db.foods.find({'group': food_group})

    sugar_measure = request.form.get('sugar_measure_select')
    sort_by = request.form.get('sort_by_select')

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
        foods_sorted = foods.sort("sugar_g_per_serving")
    
    food_groups = mongo.db.food_groups.find()

    return render_template('editcatalog.html', food_group_select=food_group
                                                , sugar_measure_select=sugar_measure
                                                , sort_by_select=sort_by
                                                , food_groups=food_groups
                                                , foods=foods_sorted)

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
                          'name': request.form.get('name'),
                          'group': request.form.get('group'),
                          'sugar_g_per_100g': float(request.form.get('sugar_g_per_100g')),
                          'sugar_g_per_serving': float(request.form.get('sugar_g_per_serving')),
                          'serving_description': request.form.get('serving_description'),
                          'reviewed': (request.form.get('reviewed') == "on"),
                      }
                      })
    return redirect(url_for('search_catalog'))

@app.route('/add_group')
def add_group():
    return render_template('addgroup.html')

@app.route('/insert_group', methods=['POST'])
def insert_group():
    food_groups_collection = mongo.db.food_groups
    food_group = request.form.to_dict()
    food_group.pop('action')
    food_groups_collection.insert_one(food_group)
    return redirect(url_for('add_to_catalog'))

if __name__ == '__main__':
    #app.run(host=os.environ.get('IP'),
    #        port=int(os.environ.get('PORT')),
    #        debug=False)
    app.run(debug=True)
