new-web-python-spain
####################

This is the code for the new Python Spain website. The main goal is to creat a management platform for the Python Spain association that can be easly customized to be used for other Python associations or more generic associations.

We're in the first stages of developing. Contributors wellcome.


How to start
------------

1. Create a virtual environment with Python3
2. Execute: ::
   
    pip install -r requirements

3. Execute: ::

   python manage.py runserver --settings pywebes.settings.develop

4. Install bower (if its not on your system)

4. Execute ::

   bower install

 
How to contribute
-----------------

The best way to contribute is to create a github fork and make pull requests

Development hints
-----------------

If you're devoping and want to avoid adding the settins parameter try: ::

    export DJANGO_SETTINGS_MODULE=pywebes.settings.develop


