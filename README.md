# Recipe Maker: Foodgram (Docker Edition) #

### Technology Stack ###
Python 3.7 / Django 2.2.19 / Django REST framework 3.13.1 / PostgreSQL 13.0 / Djoser 2.1.0 / Docker 20.10.17 / Node.js 13.12.0 (used in prearranged frontend made with React)
### Description ###
Foodgram is a site that stores, shows and filters recipes from different authors. Via Foodgram users can create and update their own recipes with text description, single image, ingredients with amount. Ingreients preadded into database, list of ingredients can be expanded in admin zone. Every recipe has tags which are useful for filtering and brief insight on recipe features. Unauthorized users can browse recipes, filter them by tags and get to recipe page. Authorized users can subscribe to authors, add recipes to favorites and add recipes to shopping cart. Shopping cart can be downloaded as pdf shopping list which summarizes amounts of equal ingredients and shows total amount. When the project will be activated full API documentation will be available here: http://localhost/api/docs/
### Try it out via Docker ###
```
# clone repository
git clone https://github.com/Immalakhovskii/recipe-maker-local.git

# change directory to infra/
cd foodgram-project-react-local/infra

# copy .env.example with valid data as .env
cp .env.example .env

# create and activate Docker containers
docker-compose up -d --build
```
Now Foodgram available at http://localhost/, admin zone at http://localhost/admin/. New ingredients and tags can be added only in admin zone, recipes and users can be created and updated via general Foodgram interface
```
# log in to site and admin zone as Admin superuser
email: adminmail@mail.com
password: youllneverguess
```
Foodgram database already has 10 recipes, 48 ungredients, 5 tags and 5 users including 1 superuser. All data comes from prearranged database dump. If you need clear project:
```
# delete these commands from docker-compose.yml:
python manage.py loaddata db_dump.json &&
cp -r data/db_dump_images/. media/recipes/image &&

# stop and delete containers with static directories
docker-compose down -v

# assemble new containers:
docker-compose up -d

# create superuser in case you need access to admin site
docker-compose exec backend python manage.py createsuperuser
```
- Note that to perform docker comands **Docker must be installed and running** on your computer (https://www.docker.com/products/docker-desktop/)
### Admin Zone ###
Admin zone has some special features: 
- Recipes can be searched by name, author username and tags; ingredients can be searched by name
- Recipe model has ingredients ManyToManyField with throgh property so recipe creation page in admin zone has IngredientInline with formset restriction so admin won't be able to create recipe without ingredients
### CSV Script ###
The project has prearranged CSV file with 2.2K ingredients with measurement units. They are can be installed with custom CSV script:
```
docker-compose exec backend python manage.py csv_script
```
- Note that file contains strings in Russian
### GitHub Actions ###
![Workflow badge](https://github.com/Immalakhovskii/recipe-maker-local/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)  
On every push to GitHub the project passes Flake8 tests and updated version of backend Docker image pushes to Docker Hub
