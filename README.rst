new-web-python-spain
####################

This is the code for the new Python Spain website. The main goal is to creat a management platform for the Python Spain association that can be easly customized to be used for other Python associations or more generic associations.

We're in the first stages of developing. Contributors wellcome.

This project is a Python3 project.


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

The best way to contribute is to create a github fork and make pull requests.

1. Create a branch for each feature you want to work on. So from master ::

   git checkout -b my_cool_feature

2. Work on it, make as many changes as you like. Do not forget to add the commit comments. Please read http://chris.beams.io/posts/git-commit/ if you're not sure about how to write good commit messages.

3. Once you're ready with your work you can make a rebase if it makes the work clearer ::

   git rebase -i

4. Then you can make a push ::

   git push -u origin my_cool_feature

5. And create a pull request from github


Getting changes
~~~~~~~~~~~~~~~

To obtain the changes from the main repo first you have to add the remote to your project ::

    git remote add upstream https://github.com/python-spain/new-web-python-spain

check that the upstream is there with ::

    git remote -v

if the python-spain report appears in the upstream section you should be ready, so you can make ::

    git fetch upstream
    git merge upstream/master

to get the new changes from the master report. Now you're ready to start again


Development hints
-----------------

If you're devoping and want to avoid adding the settins parameter try: ::

    export DJANGO_SETTINGS_MODULE=pywebes.settings.develop

We have added the django-extension tools to the project, so you can run ::

    python manage.py shell_plus

to get a shell command with all the models imported.

