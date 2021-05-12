DJANGO TEMPLATE REST API
========================

### Description
-   Rest Warehouse API;
-   Django generic permission system integrated;
-   Oauth2 using Cognito or Auth0;
-   Two-factor authentication for Django admin interface;
-   Best practices for configuration split and project structure;

### Requirements

-   It is assumed that you have Python and PostgreSQL installed. If not, then download the latest versions from:
    * [Python](https://www.python.org/downloads/)
    * [PostgreSQL](https://www.postgresql.org/download/)
-   Optionally - one of the best tools for python development free of charge:
    * [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=windows)

    
### Installation

1. **Clone git repository**:
    ```bash
    git clone https://github.com/sorin-sabo/django-rest-api-oauth.git
    ```

2. **Create virtual environment**
    ```bash
    python -m venv $(pwd)/venv
    source venv/bin/activate
    ```   

3. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Fill your local configurations**:
   - fill settings/environments/local.py using your database and external auth service credentials;   

5. **Make migrations**:
    ```bash
    python manage.py makemigrations
    ```

6. **Migrate**:
    ```bash
    python manage.py migrate
    ```
   
7. **Collect static files**
    ```bash
    python manage.py collectstatic
    ```

### Run

-   Run APP using command:
    ```bash
    python manage.py runserver <optional_port_id>
    ```
- Localhost resources:
    localhost:<port_id>/admin/ - admin login page
    localhost:<port_id>/api/   - endpoints
    localhost:<port_id>/docs/  - documentation
    
## Files
* `DjangoTemplateProject` - Django settings files
* `config/` - Django settings files per environment - add here local.py
* `apps/` - Back-end code
* `venv/` - Virtual environment files used to generate requirements;

    
## Test
Run command:
* python manage.py test -k --verbosity 2
* python manage.py test {app_name} -k --verbosity 2
    * [Important] 
        * To use same database for test and development `-k ( -keepdb )`
            - otherwise, django will try to create a separate new db '{db_name}_test'
        * Optional `--verbosity 2`
            - displays the result foreach test
        * To change test db change in `local.py` the DATABASES.TEST.NAME
        * If tests are not working make sure all migrations are done : 
            `python manage.py migrate`
        * In case a test function is not working check renaming it to `test_{function_name}`
        
## Project standards
- string format is done with the latest python formatter
    - example: f'{variable}'
- strings are defined with '' not "";
- use """...""" for functions/ classes comments; leave an empty line after those comments for code readability;
- always specify in comments parameter and return type;
- always give a default value to function parameters and class arguments - helps a lot of testing;
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

## Useful commands
    python manage.py dumpdata --format=json api > apps/api/fixtures/initial_data.json
    python manage.py loaddata initial_data.json