## Description
- integration of external service oauth2 with Auth0 or Cognito (other might be possible with current token validation);
- two factor auth for django admin interface;
- best practices applied for configuration split and project structure;
- django generic permission system integrated;
- crud api with custom overwrite of methods and filter integration for demo purpose (please don't use this naming)
- manually create a migration with python script;

## Requirements
It is assumed that:
- You have Python installed. If not, then download latest version:
    * [Python](https://www.python.org/downloads/)
    * [PyCharm Community - optional](https://www.jetbrains.com/pycharm/download/#section=windows)

    
## Installation
As IDE is recommended to use PyCharm from Intellij. Community edition is free of charge.
Fallow next steps in the exact mentioned order:
- `git clone git@github.com:sorin-sabo/django-rest-api-oauth.git`
- Install virtual environment using one of the next 3 options: 
    1) If using PyCharm can be done from interface:
        - File -> Settings -> Project Interpreter -> (On top right click) Click on rim button -> Add -> OK
    2) Install virtualenv globally:
        -`pip install virtualenv`;
        -`virtualenv venv` - inside project 
        - if using pyCharm open a new terminal after running this command so virtual environment is detected;
    3) Create a venv using python command:
        - `python -m venv /path/to/new/virtual/environment`
- `pip install -r requirements.txt` - install requirements inside venv;
- fill local.py using your database and external auth service credentials;
- `python manage.py migrate` - create a local test database with the name given in local.py

## Run
    * python manage.py runserver <optional_port_id>
    * localhost:port_id/api/ - endpoints
    * localhost:port_id/docs/ - documentation
    
## Files
* `DjangoTemplateProject`: Django settings files
* `config/`: Django settings files per environment - add here local.py
* `apps/`: Back-end code
* `venv/`: Virtual environment files used to generate requirements;

    
## Test
Run command:
* python manage.py test -k --verbosity 2
* python manage.py test {app_name} -k --verbosity 2
    * [Important] 
        * To use same database for test and development `-k ( -keepdb )`
            - otherwise django will try to create a separate new db '{db_name}_test'
        * Optional `--verbosity 2`
            - displays the result foreach test
        * To change test db change in `local.py` the DATABASES.TEST.NAME
        * If tests are not working make sure all migrations are done : 
            `python manage.py migrate`
        * If a test function is not working check renaming it to `test_{function_name}`
        
## Project standards
- string format is done with latest python formatter
    - example: f'{variable}'
- strings are defined with '' not "";
- use """...""" for functions/ classes comments; leave an empty line after those comments for code readability;
- always specify in comments parameter and return type;
- always give a default value to functions parameters and class arguments - helps a lot testing;
- always store external imports in .__init__.py files to avoid circular dependency and bad architecture;
- always inspect code before deploy and fix PEP warnings or suppress the irrelevant ones;
- do not use as line split '\' - use ();
- always run the tests before deploy;
- Model design standard documentation:
    * [Designing Better Models](https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html)
    Many thanks to Vitor Freitas(https://github.com/vitorfs)
    * [Two Scoops of Django 1.11]() - Daniel Greenfeld

- Admin design documentation:
    * [Django Admin Cookbook](https://buildmedia.readthedocs.org/media/pdf/django-admin-cookbook/latest/django-admin-cookbook.pdf)
