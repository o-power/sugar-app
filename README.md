<h1 id="title">Sugar App</h1>

1. [Introduction](#introduction)
2. [Demo](#demo)
3. [UX](#ux)
4. [Technologies/Libraries](#technologies)
5. [Features](#features)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

<h2 id="introduction">Introduction</h2>

This project is a MongoDB-backed Flask app for sharing the sugar content of foods and drinks. In addition, users can complete a survey and the results of this survey advance the site owner's goal of gathering information on people's understanding of matters relating to sugar content.

<h2 id="demo">Demo</h2>

<h2 id="ux">UX</h2>

### Wireframes

Conceptual Design - Entity-Relationship Data Model
A food category has many foods.
A drink category has many drinks.
A survey has many questions.
A question has multiple options. One option is correct. The rest are incorrect.
A survey has many responses.
A response has a score (number of correct responses).

Database statistics
Number of Food categories
Number of Drink categories
Number of Foods (by category)
Number of Drinks (by category)
Survey responses.

Recommended daily intake
40g = 4g by 10
Sugar in foods (g/100g or g per serving/portion, % sugar)
Sugar in drinks (g/100ml or g per serving/portion, % sugar based on density of water)

### User Stories
1. As a user, I want to be able to add the sugar content of foods and drinks so that I can share them with the community.
2. As a user, I want to be able to compare the sugar content of foods and drinks so that I can choose options with a lower sugar content.
3. As a user, I want to be able to complete a survey so that I can test my knowledge on the sugar content of foods and drinks.
4. As a user, I want to be able to see the aggregated survey results of everyone who has taken the survey so that I can see how much the community knows about the sugar content of foods and drinks.
5. As a user, I want to be able to see statistics on the database so that I can see how complete a resource the site is.

<h2 id="technologies">Technologies/Libraries</h2>

1. [MongoDB](https://www.mongodb.com/)
2. [Heroku](https://www.heroku.com/)
3. Microsoft PowerPoint was used to create the logo.
4. [Gimp](https://www.gimp.org/) was used to reduce the file size of the background photo and thereby speed up how fast it loads.

[Materialize]() or [Bootstrap]()
[Python]()
[Heroku](https://www.heroku.com)

<h2 id="features">Features</h2>

Create: Add sugar content of a food or drink.
Read: List sugar content of foods and drinks.
Update: Edit sugar content of a food or drink.
Delete: sugar content of a food or drink.
Survey
Display survey results
Sorting
Filtering

### Existing
### Future

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
### Media
### Acknowledgements
* Shortcut icon generated using [Favicon Generator](https://realfavicongenerator.net/) [accessed 12th December 2019].
