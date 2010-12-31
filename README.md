Templates for vanillons.
========================

First, install this package.

    python setup.py install

It will add templates to the paster create command. You can create a new
vanillons project like this:

    paster create -t vanillons MyRadProject

It requires the Quaid js lib, which you can install via git.

    cd myradproject
    git init
    git submodule add git://github.com/benogle/quaid.git myradproject/public/j/quaid

It also requires pylons_common at https://github.com/benogle/pylons_common

Install your rad project

    sudo python setup.py develop

DB
-----

This assumes a postgres db named myradproject (or whatev the package ends
up being named). Change this in development.ini and test.ini to reflect your
db:
    
    sqlalchemy.default.url = postgresql://myuser:password@localhost/dbname

Make a myradproject DB and a myradproject_test DB, pick a db user and run
in psql:

    CREATE DATABASE myradproject;
    CREATE DATABASE myradproject_test;
    GRANT ALL PRIVILEGES ON DATABASE myradproject TO myuser;
    GRANT ALL PRIVILEGES ON DATABASE myradproject_test TO myuser;

Have your new project generate the proper tables in your fresh new db by
running

    paster setup-app development.ini

Running it
----------

Tests are run via:

    nosetests -s --tests=myradproject

And the webserver is run via

    paster serve --reload development.ini

Head over to http://localhost:5000/ and register a user. The first one
registered will be donned the admin cap.