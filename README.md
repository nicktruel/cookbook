# Nick's Cookbook
Built by **_Nicolas Truel_**

---
> Web application allowing users to easily store, access, update, add and delete cooking recipes.
Being an avide amateur of good food and cooking myself, the aim of that app was to make it as practical as possible for finding recipes, updating them and being able to follow them while cooking (as if reading recipes from a cookbook on a stand in your kitchen).

> The deployed version is available here: [Nick's Cookbook](https://cookbook-milestone-3.herokuapp.com/home_page)

#### Table of content
1. [UX](#UX)
2. [Features](#Features)
3. [Technologies](#Technologies)
    1. [Installing](#Installing)
    2. [Building](#Building)
4. [Testing](#Testing)
    1. [Android](#Android)
    2. [IOS](#IOS)
    3. [Browsers](#Browsers)
5. [Deployment](#Deployment)
6. [Credits](#Credits)
    1. [Content](#Content)
    2. [Media](#Media)
    

## <a name="UX"> UX</a>

> The app is designed to keep your recipes in one place as if it was an old cookbook folder; easy to add, update, delete and search for recipes, it should be simple and intiutive to use. 

> Built as user friendly as possible, the app should be simple and fast to use. On one click of a button the user can access recipes classified by country, type, price etc...

> First drawing on paper before realisation:

![wireframe](/assets/img_readme/wireframe.jpg)

##  <a name="Features">Features</a>

* The main page offers the users a way to search through different type of recipes via a navbar; recipes can be searched by countries of origin, cost and whether they are vegetarian or not. A link to add new recipes is also available in the search bar.

![Home page](/assets/img_readme/home-page.png)

* Each recipe can than be displayed in details on one page with the full list of ingredients, their quantities and the steps to follow for making it. The options of modifying or deleting the recipe are given also on that page.

![Detailed recipe](/assets/img_readme/detail-page.png)

* One page allows the users to add their own recipes to the app with all the options available.

![Add recipe](/assets/img_readme/add-page.png)

* The update page can be use for editing recipes (ie. change ingredients or quantities, name, change instructions or image, add or delete step, ingredient, image etc...)

> At a future date, a log in system will be added for the user to be able to keep his recipes safe. An E-mail address and password will be required to create your own cookbook, untouchable from other users.


##  <a name="Technologies">Technologies</a>

<dl>
  <dt>HTML5</dt>
  <dt>CSS3</dt>
  <dt>PYTHON</dt>
  <dt>Flask framework</dt>
  <dt>PYMONGO</dt>
  <dt>Google Fonts</dt>
  
  [https://fonts.google.com/](https://fonts.google.com/)
  <dt>JQuery (For dropdown of navbar)</dt>
  
  [https://jquery.com/](https://jquery.com/)
  <dt>BOOTSTRAP 3.7 (Navbar, Carousel, cards in recipe, and recipe details, forms in add recipe and update recipe)</dt>
  
  [https://getbootstrap.com/docs/3.3/](https://getbootstrap.com/docs/3.3/)
  <dt>Recipes are kept in mongodb</dt>
  
  [https://www.mongodb.com/](https://www.mongodb.com/)
</dl>

### <a name="Installing">Installing</a>

> **Requirements**

    Click==7.0
    Flask==1.0.2
    Flask-PyMongo==2.3.0
    Jinja2==2.10.1
    MarkupSafe==1.1.1
    Werkzeug==0.15.2
    chardet==2.2.1
    colorama==0.2.5
    dnspython==1.16.0
    html5lib==0.999
    itsdangerous==1.1.0
    pycurl==7.19.3
    pymongo==3.8.0
    requests==2.2.1
    six==1.5.2
    urllib3==1.7.1
    wheel==0.24.0   
    
### <a name="Building">Building</a>  

> **Screen shot of mongo DB**

![recipe in mongoDB ](/assets/img_readme/recipe-mongo.png)

> **Definition to render recipes with France for origin:**

    @app.route('/french_recipes')
    def french_recipes():
        return render_template("recipes.html", recipes=mongo.db.recipes.find({"recipe_country": "option1"}).sort("recipe_name"))
        
> **Definition to render the recipe chosen in details:**

    @app.route('/recipe_details/<recipe_id>')
    def recipe_details(recipe_id):
        the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        return render_template("recipe_details.html", recipe=the_recipe)

> **Definition to delete a recipe:**

    @app.route('/delete_recipe/<recipe_id>')
    def delete_recipe(recipe_id):
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        return render_template("confirm_deletion.html")

> **Definition to insert data in a new object in mongodb:**

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
            'recipe_ingredients_quantity0': request.form.get('recipe_ingredients_quantity.0').capitalize(),
            'recipe_instruction0': request.form.get('recipe_instruction.0').capitalize(),
            'price_tag': request.form.get('price_tag')
    })
    return render_template("confirm_addition.html")

## <a name="Testing">Testing </a>

<dl>
 <dt>Android <a name="Android"></a></dt>
 <dl>Samsung Galaxy A3
 <dl>Samsung Galaxy J5
 <dl>Samsung Galaxy TAB A
 <dl>Huawei P20 Lite
 <dt>IOS <a name="IOS"></a></dt>
 <dl>Iphone 5s
 <dl>Iphone 6
 <dl>Macbook
 <dt>Browsers <a name="Browsers"></a></dt>
 <dl>Google Chrome (Version 75.0.3770.100)
 <dl>Explorer (42.17134.1.0)
</dl>

* CSS codes were checked with W3C CSS Validation Service (https://jigsaw.w3.org/css-validator/)
* base.html, home.html, recipes.html, recipe_details.html, add_recipe.html and update_recipe.html were checked with W3C Markup Validation Service (https://validator.w3.org/)
* Chrome DevTools

##  <a name="Deployment">Deployment</a>

The code, (built in [AWS Cloud9](https://us-east-1.console.aws.amazon.com/cloud9/ide/be66c5ceaa5246709c7dfe7d64710a13)) is pushed to a remote repository on GitHub and the site is published on GitHub pages https://github.com/nicktruel/cookbook).

The application is deployed to Heroku: https://cookbook-milestone-3.herokuapp.com/

The database of all recipes is stored with mongoDB: https://www.mongodb.com/


##  <a name="Credits">Credits</a>

####  <a name="Content">Content</a>
The was inspired from various recipe websites such as Marmiton (https://www.marmiton.org/), 750g (https://www.750g.com/) and many more due to my passion for food and cooking. 
The main color of the app (Orange) is taken from the Marmiton website.


####  <a name="Media">Media</a>
The main color of the app (Orange) is taken from the "Marmiton" website.

THe food icon in the recipe cards when no image is added is made by "Freepik from www.flaticon.com".
