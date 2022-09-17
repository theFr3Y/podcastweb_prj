# podcastweb_prj
testing + api

###description
in this project, i made a podcast blog that has newer features than <a href="https://github.com/theFr3Y/weblog_django_prj.git">weblog</a> such as:<br>
-JWT API and DRF(for watch codes go to this path:"apiapp")<br>
-Testing(for watch codes go to this path:"mainapp/tests.py")

## Install and Run
```bash
cd directory
mkdir podcast
cd podcast 
git clone https://github.com/theFr3Y/podcastweb_prj.git
pip install -r require.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
