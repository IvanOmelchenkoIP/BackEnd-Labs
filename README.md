# BackEnd Laboratory Works

## Laboratory Work 1 Task

Create REST API app about cost accounting

### Required Functionality:

- Creating new user
- Creating new category
- Creating new record
- Receiving categories list
- Receiving list of records for one user
- Receiving list of records by category of the user

### Data Structure:

| User      |
| --------- |
| id        |
| user name |

| Category      |
| ------------- |
| id            |
| category name |

| Record           |
| ---------------- |
| id               |
| user id          |
| category id      |
| date of creation |
| sum              |

## Laboratory Work 2 Task

- Add data validation
- Add error handling
- Add ORM models
- Add functionality by variant

### Functionality By Variant:

Group number - IP-04

04 mod 3 = 1

**Variant 1.** Add currency

#### Currency:

- Add Currency entity
- Default currency can be added for every user
- When creating a record, a currency can be set, but it is not mandatory
- If a record was not set when creating a record, a default currency of a user will be used

#### Resulting Data Structure Used In Solution:

| Currency      |
| ------------- |
| id            |
| currency name |

| User        |
| ----------- |
| id          |
| user name   |
| currency id |

| Category      |
| ------------- |
| id            |
| category name |

| Record           |
| ---------------- |
| id               |
| user id          |
| category id      |
| date of creation |
| sum              |
| currency id      |

## Laboratory Work 3 Task

- Create registration and login endpoints
- Protect other endpoints so that only logged in users have access to them

## Local Launch

**Make sure that you have [Python](https://www.python.org/downloads/) installed (program was written in Python 3.10.5)**

Clone git repository:

    git clone https://github.com/IvanOmelchenkoIP/BackEnd-Labs.git

Create virtual environment:

*For Windows:*

    py -3 -m venv env

*For Linux:*

    python3 -m venv env

Launch virtual environment:

*For Windows:*

    .\env\scripts\activate

*For Linux:*

    source ./env/bin/activate

Install dependencies:

    pip install -r requirements.txt

Deactivate virtual environment:

    deactivate

Set FLASK_APP variable:

*For Windows:*

    set FLASK_APP=backend

*For Linux:*

    export FLASK_APP=backend

Launch virtual environment again (described before). Run the app:

    flask run –host 0.0.0.0 -p 5005

### Local Launch of Lab 3

The same as the previous labs, but add JWT_SECRET_KEY after setting FLASK_APP, for this:

Access python console in your terminal by typing: 

    python

Proceed with the two following commands:

    import secrets
    secrets.SystemRandom().getRandBits(128)

You should receive a result and set it to JWT_SECRET_KEY as following:

*For Windows:*

    set JWT_SECRET_KEY=<your key>

*For Linux:*

    export JWT_SECRET_KEY=<your key>

After that you can launch virtual environment and an the app   

### Dockerfile

To run Dockerfile use following commands:

    docker-compose build
    docker-compose up

### Testing

To test the program you must use [Postman](https://www.postman.com/)

For Laboratory Work 3 use [Insomnia](https://insomnia.rest/)

#### Laboratory Work 1

Creating new user (*required - user_name*):

    /newuser

Creating new category (*required - category_name*):

    /newcategory

Creating new record (*required - user_id, category_id, record_sum*):

    /newrecord

Getting users (was implemented for ability to keep track of user_id of created users as they are randomly generated):

    /users

Getting categories:

    /categories

Geting records:

    /records
    /records?user_id=<value>
    /records?user_id=<value>&category_id=<value>

#### Laboratory Work 2

Creating new currency (*required - currency_name*):

    /currency

Creating new user (*required - user_name, user_currency*):

    /user

Updating user default currency (*required - user_currency*):

    /user/<user_id_value>

Creating new category (*required - category_name*):

    /category

Creating new record (*required - user_id, category_id, record_sum, not mandatory - record_currency*):

    /record

Getting currencies:

    /currency

Getting currency by id:

    /currency/<currency_id_value>

Getting users:

    /user

Getting user by id:

    /user/<user_id_value>

Getting categories:

    /category

Getting category by id:

    /category/<category_id_value>

Geting records:

    /record
    /record?user_id=<value>
    /record?user_id=<value>&category_id=<value>

Getting record by id:

    /record/<record_id_value>

#### Laboratory Work 3 

Registering a user (*required - user_name, user_currency, user_password*):

    /register

Logging in (*required - user_name, user_password*):

    /login

Creating new currency (*required - currency_name, user has to be logged in*):

    /currency

Updating user default currency (*required - user_currency, user has to be logged in*):

    /user/<user_id_value>

Creating new category (*required - category_name, user has to be logged in*):

    /category

Creating new record (*required - user_id, category_id, record_sum, optional - record_currency, user has to be logged in*):

    /record

Getting currencies (*optional - being logged in*):

    /currency

Getting currency by id (*user has to be logged in*):

    /currency/<currency_id_value>

Getting users (*user has to be logged in*):

    /user

Getting user by id (*user has to be logged in*):

    /user/<user_id_value>

Getting categories (*user has to be logged in*):

    /category

Getting category by id (*user has to be logged in*):

    /category/<category_id_value>

Geting records (*user has to be logged in*):

    /record
    /record?user_id=<value>
    /record?user_id=<value>&category_id=<value>

Getting record by id (*user has to be logged in*):

    /record/<record_id_value>

## Deployment

### Heroku

[App on Heroku](https://backend-laboratory-works.herokuapp.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

#### Process

The app named backend-laboratory-works was created on Heroku and then deployed using GitHub Actions (*see ./github/workflows/heroku-deploy.yml*)

### Render

[App on Render](https://backend-labs.onrender.com/) - index page shows NotFound, but response will be shown upon using any of the paths described earlier

#### Process

The app was deployed on [render.com](https://render.com/) by creating a Web Service with the following parameters:

![render-deploy](https://github.com/IvanOmelchenkoIP/BackEnd-Labs/blob/main/readme/render-deploy.png)

The app uses [Free Web Service](https://render.com/docs/free) program