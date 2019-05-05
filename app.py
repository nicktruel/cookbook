import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbookRecipe'
app.config["MONGO_URI"] = 'mongodb+srv://nickTruel:CamronLouis@myfirstcluster-i1crt.mongodb.net/cookbookRecipe?retryWrites=true'
                            
mongo = PyMongo(app)

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("home.html")
    
@app.route('/view_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)