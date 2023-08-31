# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/pravan97/microblogBE.git
    $ cd microblogBE
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:
  
    $ python manage.py makemigrations  
    $ python manage.py migrate
It might not migrate properly since it doesnt have migrations folder
run following command
    $python manage.py migrate --run-syncdb

Create a superuser

    $ python manage.py createsuperuser

You can now run the development server:

    $ python manage.py runserver
