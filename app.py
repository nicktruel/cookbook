import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbookRecipe'
app.config["MONGO_URI"] = 'mongodb+srv://nickTruel:CamronLouis@myfirstcluster-i1crt.mongodb.net/cookbookRecipe?retryWrites=true'
                            
mongo = PyMongo(app)


# Direct to home.page
@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("home.html")
 
 
 
# Display recipes by country of origin in recipes.html 
@app.route('/french_recipes')
def french_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "France"}))

@app.route('/american_recipes')
def american_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "America"}))
  
@app.route('/thai_recipes')
def thai_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "Thailand"}))
    
@app.route('/english_recipes')
def english_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "England"}))
    
@app.route('/italian_recipes')
def italian_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "Italy"}))
    
@app.route('/indian_recipes')
def indian_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "India"}))
  


# Display recipes by price in recipes.html
@app.route('/cheap_recipes')
def cheap_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "€"}))
    
@app.route('/medium_recipes')
def medium_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "€€"}))

@app.route('/expensive_recipes')
def expensive_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "€€€"}))


# Dispaly recipes by type of course in recipes.html
@app.route('/breakfast_recipes')
def breakfast_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "breakfast"}))
    
@app.route('/starter_recipes')
def starter_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "starter"}))
    
@app.route('/main_recipes')
def main_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "main"}))

@app.route('/desert_recipes')
def desert_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "desert"}))




# Disaply recipes weither vegetarian or not in recipes.html
@app.route('/veg_recipes')
def veg_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"vegetarian_recipe": True}))
    
@app.route('/non_veg_recipes')
def non_veg_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"vegetarian_recipe": False}))




# Display recipe in details in recipe_details.html
@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=the_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=the_recipe)





#@app.route('/get_recipes')
#def get_recipes():
#    return render_template("recipes.html", recipes=mongo.db.recipes.find())


# Brings user to page to add a recipe, add_recipe.html
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html",
    recipes=mongo.db.recipes.find())



# Function to insert a new recipe, then brings user back to home.html
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one({
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_img': request.form.get('recipe_img'),
        'recipe_country': request.form.get('recipe_country'),
        'course_type': request.form.get('course_type'),
        'vegetarian_recipe': request.form.get('vegetarian_recipe'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_instruction': request.form.get('recipe_instruction'),
        'price_tag': request.form.get('price_tag')
    })
    return redirect(url_for('home_page'))






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)