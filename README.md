# PDD Tvoy Gorod #
## Установка ##

1. Установить `python`, `postgreSQL`

2. Создать Базу Данных:

    ```
    $ sudo -u postgres psql CREATE DATABASE myproject;
    ```

    ### Создание пользователя ###
    ```
    CREATE USER myprojectuser WITH PASSWORD 'password';
    ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
    ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myprojectuser SET timezone TO 'UTC';
    ```

    ### Предоставление прав пользователю ###
    ```
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    ```

    Выйти из postgres:
    ```
    \q
    ```

3. Скопировать `local_settings_example.py` как `local_settings.py`, заполнить поля Базы Данных.

4. Создать виртуальную среду:
    ## Установка virtualenv ##
    ```
    $ sudo -H pip3 install --upgrade pip
    $ sudo -H pip3 install virtualenv
    ```

    ## Создание среды ##
    Перейти в каталог приложения и выполнить:
    ```
    $ virtualenv pdd_tvoy_gorod_env
    ```

    ## Активация ##
    ```
    $ source pdd_tvoy_gorod_env/bin/activate
    ```

5. Установить пакеты:
    ```
    $ pip install django psycopg2-binary pillow
    ```

6. Для запуска движка выполнить:
    ```
    $ python manage.py runserver
    ```

7. Перейти по адресу: `127.0.0.1:8000`
