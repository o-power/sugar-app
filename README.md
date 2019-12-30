<h1 id="title">The Sugar Catalog</h1>

1. [Introduction](#introduction)
2. [Demo](#demo)
3. [UX](#ux)
4. [Technologies/Libraries](#technologies)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

<h2 id="introduction">Introduction</h2>

The Sugar Catalog is a MongoDB-backed Flask app for sharing the sugar content of foods. The motivation for users is that they can compare their favourite foods to other foods in terms of sugar content. The motivation for the site owner is building up a useful database that can be used for educating the community and improving health.

<h2 id="demo">Demo</h2>

A live demo of The Sugar Catalog app can be found [here]() on Heroku.

<img src="static/img/siteonipadandiphone.png" alt="Image of app" width="700px">

<h2 id="ux">UX</h2>

### User Stories

1. As a user, I want to be able to compare a list of foods based on grams of sugar per 100 grams so that I can identify high, medium and low sugar foods.
2. As a user, I want to be able to compare a list of foods based on grams of sugar per serving so that I can understand how much sugar is in a serving of my favourite foods.
3. As a user, I want to be able to add new foods to the catalog so that I can compare them to other foods and also share them with the community.
4. As a user, I want to be able to add new food groups to the catalog so that I can then add new foods which fall into those groups.
5. As a user, I want to be able to edit foods in the catalog so that I can make corrections and also mark entries as reviewed.
6. As a user, I want to be able to search the catalog based on food group so that I can quickly find foods in a particular group.
7. As a user, I want to be able to sort the catalog by sugar content (high to low or low to high) so that I can quickly find either high or low sugar foods.
8. As a user, I want to be able to sort the catalog alphabetically (A to Z or Z to A) so that I can quickly find particular foods.

### Database

Behind the app there is a single MongoDB database called sugar_app which contains 2 collections: foods and food_groups. A food belongs to one food group, although a food group can have many foods.

foods
- name (string)
- group (string)
- sugar_g_per_100g (double)
- sugar_g_per_serving (double)
- serving_description (string)
- reviewed (Boolean)

food_groups
- group (string)

### Navigation

The app consists of 6 views. There are 10 functions which handle the rendering of these views:
1. home(): renders the home page.
2. search_catalog(): if request method is POST, then renders the searchcatalog.html page with the values submitted in the form. If the request method is GET, then renders the searchcatalog.html page with the default values.
3. add_to_catalog(): renders the addtocatalog page.
4. insert_food(): Inserts the food as submitted through the form into the catalog and renders the default searchcatalog.html page by calling the search_catalog function.
5. add_group(): renders the addgroup.html page. 
6. insert_group(): inserts the food group as submitted through the form into the catalog and renders the addtocatalog.html page by calling the add_to_catalog function.
7. edit_catalog(): renders the editcatalog.html page with the default values. 
8. search_edit_catalog(): renders the editcatalog.html page with the values submitted in the form. 
9. edit_food(food_id): renders the editfood.html page with the details for the user-selected food.
10. update_food(food_id): Updates the food in the catalog with the values submitted through the form and renders the default searchcatalog.html page by calling the search_catalog function.

<img src="static/img/navigation_flow.jpg" alt="Image of app" width="700px">

<h2 id="technologies">Technologies/Libraries</h2>

1. [MongoDB](https://www.mongodb.com/) was used as the NoSQL database for the app.
2. [Python](https://www.python.org/), and specifically [Flask](https://flask.palletsprojects.com/en/1.1.x/), was used as the back-end language.
3. [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) was used as the templating language for rendering the pages.
4. [Materialize](https://materializecss.com/) was used as the front-end framework.
5. Microsoft PowerPoint was used to create the logo.
6. [Gimp](https://www.gimp.org/) was used to reduce the file size of the background photo and thereby speed up how fast it loads.
7. [Heroku](https://www.heroku.com/) was used to deploy the app.

<h2 id="features">Features</h2>

### Existing
- User can filter catalog by food group.
- User can choose the sugar measure to be either grams per 100g or grams per serving.
- User can sort the catalog alphabetically (A to Z or Z to A).
- User can sort the catalog by sugar content (high to low or low to high).
- User can add a new food group to the catalog e.g. Confectionery, Cereal etc.
- User can add a new food to the catalog.
- User can edit the details of any food in the catalog.
- User can mark a food as reviewed (by default, each food is not reviewed).
- Site is responsive, i.e. the navigation bar and page contents resize based on screen size. This is achieved using the Materialize grid and media queries.

### Future
- Add the ability to add drinks to the sugar catalog. This will involve adding a g per 100ml measure.
- Add error messages if the user fails to enter data correctly in the forms.

<h2 id="testing">Testing</h2>

### General Testing

During development, the Chrome DevTools console was used regularly to log the data to ensure that it was being correctly retrieved from MongoDB.

The HTML was checked using the [W3C Markup Validation Service](https://validator.w3.org/). This identified an incorrectly used paragraph element.

The CSS was checked using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). This returned one error which said the property "r" does not exist. However, "r" is a property of the circle svg.

### User Story Testing

<h2 id="deployment">Deployment</h2>

The app is deployed on Heroku. Before deploying the app on Heroku, ensure that the project includes the files requirements.txt and Procfile. To create the requirements.txt file, run the following command in the terminal:
pip3 freeze --local > requirements.txt
To create the Procfile, run the following command in the terminal:
echo web: python app.py > Procfile

Next, create a new app within the Heroku web application. Under Settings add the environment variables:
IP
PORT
MONGO_URI (connection string for the MongoDB)

To deploy the app from the local repository, run the following commands in the terminal:
heroku login
git remote add heroku https://git.heroku.com/<insert app name>.git
git push -u heroku master

<h2 id="credits">Credits</h2>

### Content
- The survey questions were adapted from []().

### Media
- The background image was taken by myself and edited using Gimp.
- The site logo was created using Microsoft PowerPoint.

### Acknowledgements
* Shortcut icon generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 12th December 2019].
