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
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option1"}))

@app.route('/american_recipes')
def american_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option4"}))
  
@app.route('/thai_recipes')
def thai_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option2"}))
    
@app.route('/english_recipes')
def english_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option7"}))
    
@app.route('/italian_recipes')
def italian_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option6"}))
    
@app.route('/indian_recipes')
def indian_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option5"}))
  
@app.route('/other_country_recipes')
def other_country_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option3"}))


# Display recipes by price in recipes.html
@app.route('/cheap_recipes')
def cheap_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "option1"}))
    
@app.route('/medium_recipes')
def medium_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "option2"}))

@app.route('/expensive_recipes')
def expensive_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"price_tag": "option3"}))


# Dispaly recipes by type of course in recipes.html
@app.route('/breakfast_recipes')
def breakfast_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "option1"}))
    
@app.route('/starter_recipes')
def starter_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "option2"}))
    
@app.route('/main_recipes')
def main_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "option3"}))

@app.route('/desert_recipes')
def desert_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "option4"}))

@app.route('/other_course_recipes')
def other_course_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"course_type": "option5"}))


# Disaply recipes weither vegetarian or not in recipes.html
@app.route('/veg_recipes')
def veg_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"vegetarian_recipe": "option1"}))
    
@app.route('/non_veg_recipes')
def non_veg_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find({"vegetarian_recipe": "option2"}))




# Display recipe in details in recipe_details.html
@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=the_recipe)

# Display page to edit recipes, edit_recipe.html
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_country': request.form.get('recipe_country'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_ingredient0': request.form.get('recipe_ingredient.0'),
        'recipe_ingredient1': request.form.get('recipe_ingredient.1'),
        'recipe_ingredient2': request.form.get('recipe_ingredient.2'),
        'recipe_ingredient3': request.form.get('recipe_ingredient.3'),
        'recipe_ingredient4': request.form.get('recipe_ingredient.4'),
        'recipe_ingredient5': request.form.get('recipe_ingredient.5'),
        'recipe_ingredient6': request.form.get('recipe_ingredient.6'),
        'recipe_ingredient7': request.form.get('recipe_ingredient.7'),
        'recipe_ingredient8': request.form.get('recipe_ingredient.8'),
        'recipe_ingredient9': request.form.get('recipe_ingredient.9'),
        'recipe_ingredients_quantity0': request.form.get('recipe_ingredients_quantity.0'),
        'recipe_ingredients_quantity1': request.form.get('recipe_ingredients_quantity.1'),
        'recipe_ingredients_quantity2': request.form.get('recipe_ingredients_quantity.2'),
        'recipe_ingredients_quantity3': request.form.get('recipe_ingredients_quantity.3'),
        'recipe_ingredients_quantity4': request.form.get('recipe_ingredients_quantity.4'),
        'recipe_ingredients_quantity5': request.form.get('recipe_ingredients_quantity.5'),
        'recipe_ingredients_quantity6': request.form.get('recipe_ingredients_quantity.6'),
        'recipe_ingredients_quantity7': request.form.get('recipe_ingredients_quantity.7'),
        'recipe_ingredients_quantity8': request.form.get('recipe_ingredients_quantity.8'),
        'recipe_ingredients_quantity9': request.form.get('recipe_ingredients_quantity.9'),
        'recipe_instruction0': request.form.get('recipe_instruction.0'),
        'recipe_instruction1': request.form.get('recipe_instruction.1'),
        'recipe_instruction2': request.form.get('recipe_instruction.2'),
        'recipe_instruction3': request.form.get('recipe_instruction.3'),
        'recipe_instruction4': request.form.get('recipe_instruction.4'),
        'recipe_instruction5': request.form.get('recipe_instruction.5'),
        'recipe_instruction6': request.form.get('recipe_instruction.6'),
        'recipe_instruction7': request.form.get('recipe_instruction.7'),
        'recipe_instruction8': request.form.get('recipe_instruction.8'),
        'recipe_instruction9': request.form.get('recipe_instruction.9'),
        'course_type': request.form.get('course_type'),
        'price_tag': request.form.get('price_tag'),
        'recipe_img': request.form.get('recipe_img'),
        'vegetarian_recipe': request.form.get('vegetarian_recipe'),
    })
    #return redirect(url_for('home_page'))
    return render_template("confirm_update.html")


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
        'recipe_name': request.form.get('recipe_name').capitalize(),
        'recipe_description': request.form.get('recipe_description').capitalize(),
        'recipe_img': request.form.get('recipe_img'),
        'recipe_country': request.form.get('recipe_country'),
        'course_type': request.form.get('course_type'),
        'vegetarian_recipe': request.form.get('vegetarian_recipe'),
        'recipe_ingredient0': request.form.get('recipe_ingredient.0').capitalize(),
        'recipe_ingredient1': request.form.get('recipe_ingredient.1').capitalize(),
        'recipe_ingredient2': request.form.get('recipe_ingredient.2').capitalize(),
        'recipe_ingredient3': request.form.get('recipe_ingredient.3').capitalize(),
        'recipe_ingredient4': request.form.get('recipe_ingredient.4').capitalize(),
        'recipe_ingredient5': request.form.get('recipe_ingredient.5').capitalize(),
        'recipe_ingredient6': request.form.get('recipe_ingredient.6').capitalize(),
        'recipe_ingredient7': request.form.get('recipe_ingredient.7').capitalize(),
        'recipe_ingredient8': request.form.get('recipe_ingredient.8').capitalize(),
        'recipe_ingredient9': request.form.get('recipe_ingredient.9').capitalize(),
        'recipe_ingredients_quantity0': request.form.get('recipe_ingredients_quantity.0').capitalize(),
        'recipe_ingredients_quantity1': request.form.get('recipe_ingredients_quantity.1').capitalize(),
        'recipe_ingredients_quantity2': request.form.get('recipe_ingredients_quantity.2').capitalize(),
        'recipe_ingredients_quantity3': request.form.get('recipe_ingredients_quantity.3').capitalize(),
        'recipe_ingredients_quantity4': request.form.get('recipe_ingredients_quantity.4').capitalize(),
        'recipe_ingredients_quantity5': request.form.get('recipe_ingredients_quantity.5').capitalize(),
        'recipe_ingredients_quantity6': request.form.get('recipe_ingredients_quantity.6').capitalize(),
        'recipe_ingredients_quantity7': request.form.get('recipe_ingredients_quantity.7').capitalize(),
        'recipe_ingredients_quantity8': request.form.get('recipe_ingredients_quantity.8').capitalize(),
        'recipe_ingredients_quantity9': request.form.get('recipe_ingredients_quantity.9').capitalize(),
        'recipe_instruction0': request.form.get('recipe_instruction.0').capitalize(),
        'recipe_instruction1': request.form.get('recipe_instruction.1').capitalize(),
        'recipe_instruction2': request.form.get('recipe_instruction.2').capitalize(),
        'recipe_instruction3': request.form.get('recipe_instruction.3').capitalize(),
        'recipe_instruction4': request.form.get('recipe_instruction.4').capitalize(),
        'recipe_instruction5': request.form.get('recipe_instruction.5').capitalize(),
        'recipe_instruction6': request.form.get('recipe_instruction.6').capitalize(),
        'recipe_instruction7': request.form.get('recipe_instruction.7').capitalize(),
        'recipe_instruction8': request.form.get('recipe_instruction.8').capitalize(),
        'recipe_instruction9': request.form.get('recipe_instruction.9').capitalize(),
        'price_tag': request.form.get('price_tag')
    })
    #return redirect(url_for('confirm_addition'))
    return render_template("confirm_addition.html")



@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return render_template("confirm_deletion.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)