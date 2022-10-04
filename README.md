# Recipe Maker: Foodgram (Local Edition) #

---
#### Technology Stack ####
Python 3.7 / Django 2.2.19 / Django REST framework 3.13.1 / PostgreSQL 13.0 / Djoser 2.1.0 / Docker 20.10.17 / Node.js 13.12.0 (used in prearranged frontend made with React)
#### Description ####
Foodgram is a site that stores, shows and filters recipes from different authors. Via Foodgram users can create and update their own recipes with text description, single image, ingredients with amount. Ingreients preadded into database, list of ingredients can be expanded in admin zone. Every recipe has tags which are useful for filtering and brief insight on recipe features. Unauthorized users can browse recipes, filter them by tags and get to recipe page. Authorized users can subscribe to authors, add recipes to favorites and add recipes to shopping cart. Shopping cart can be downloaded as pdf shopping list which summarizes amounts of equal ingredients and shows total amount. When the project will be activated full API documentation will be available here: http://localhost/api/docs/redoc.html
#### Try it out ####

#### GitHub Actions ####
![Workflow badge](https://github.com/Immalakhovskii/recipe-maker-local/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)  

On every push the project passes Flake8 tests and new version of backend Docker image pushes to Docker Hub