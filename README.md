
# Texas Fuel Rate Predictor

Software design project web app to predict the fuel reate based on the following criteria:
- Client Location
- Competitors rate
- Client rate history
- Gallons requested
- Company profit margin (%)
- Seasonal rate fluctuation (%)


## Getting Started

```
python run.py
```

Open your browser and go to 127.0.0.1:5000

### Prerequisites

What things you need to install the software and how to install them

I followed this playlist extensively 
https://www.youtube.com/watch?v=QnDWIZuWYW0

Make sure you use python3.6.x or any up-to-date python version

First, create a virtual environment
Within your source code directory or main project directory run:
```
virtualenv venv
```

To use a specific python version use:

```
virtualenv -p /usr/bin/python* venv
```

Now enter the environment:

```
. venv/bin/activate
```

To leave run:

```
deactivate
```

To delete a virtual environment remove the directory:

```
rm -rf venv
```

Flask requires pip To install (may need root privelages):

```
pip3 install flask
```

After you write some code run:

```
FLASK_APP=flaskblog.py flask run
```

All packages needed to get the app running:

```
pip install <package name>
```
bcrypt==3.1.7
blinker==1.4
cffi==1.12.3
Click==7.0
Flask==1.0.3
Flask-Bcrypt==0.7.1
Flask-Login==0.4.1
Flask-Mail==0.9.1
Flask-SQLAlchemy==2.4.0
Flask-WTF==0.14.2
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
Pillow==6.0.0
pycparser==2.19
six==1.12.0
SQLAlchemy==1.3.5
Werkzeug==0.15.4
WTForms==2.2.1

More on WTForms
https://wtforms.readthedocs.io/en/stable/

We used Flask-SQLAlchemy for the database 
see https://tinyurl.com/y65ko6h3 for info

Go to http://flask.pocoo.org/ for info on the flask framework


### Installing

Nothing else needed other than python, flask, and pip packages described above.


## Deployment

Coming soon.

## Bluepring structure
[01;34m.[00m
├── NOTES
├── README
├── requirements.txt
├── run.py
├── structure.txt
└── [01;34mtexasfuelratepredictor[00m
    ├── config.py
    ├── [01;34merrors[00m
    │   ├── handlers.py
    │   └── __init__.py
    ├── [01;34mfuel[00m
    │   ├── forms.py
    │   ├── __init__.py
    │   └── routes.py
    ├── __init__.py
    ├── [01;34mmain[00m
    │   ├── __init__.py
    │   └── routes.py
    ├── models.py
    ├── site.db
    ├── [01;34mstatic[00m
    │   ├── main.css
    │   └── [01;34mprofile_pics[00m
    │       ├── [01;35m1043cc1d2701e122.jpeg[00m
    │       ├── [01;35m6579f5003164503a.png[00m
    │       ├── [01;35ma20fc178dc710925.jpg[00m
    │       ├── [01;35me4933d1708b1b89d.jpg[00m
    │       └── [01;35mfba763a58376adfe.png[00m
    ├── [01;34mtemplates[00m
    │   ├── about.html
    │   ├── account.html
    │   ├── [01;34merrors[00m
    │   │   ├── 403.html
    │   │   ├── 404.html
    │   │   └── 500.html
    │   ├── fuel_form.html
    │   ├── fuel_history.html
    │   ├── home.html
    │   ├── layout.html
    │   ├── login.html
    │   ├── past_quote.html
    │   ├── register.html
    │   ├── reset_request.html
    │   └── reset_token.html
    └── [01;34musers[00m
        ├── forms.py
        ├── __init__.py
        ├── routes.py
        └── utils.py

9 directories, 40 files

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask SQLAlchemy] (https://tinyurl.com/y65ko6h3) - The database used
* [Python] (https://python.org)
* [Bootstrap] (https://getbootstrap.com/)

## Authors

* **Hoang Vo** - [Hoangvo92](https://github.com/Hoangvo92)
* **Leonel Garcia** - [garcialeonel](https://github.com/garcialeonel)

## Acknowledgments

* Thanks to Corey Schafer and his most helpful YouTube channel 
https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
