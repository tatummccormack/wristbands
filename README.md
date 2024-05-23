# <img src="/static/wristbandslogo.png">

Wristbands stems from a childhood dream of mine to create and own my own music festival. With Music festivals taking over the music industry the demand is high and the resources are limited. That's why I created my flask app wristbands, a one stop shop for all things Music festivals. 

## Table of Contents🐛

* [Tech Stack](#tech-stack)
* [Features](#features)
* [Setup/Installation](#installation)
* [To-Do](#future)
* [License](#license)

## <a name="tech-stack"></a>Tech Stack

__Frontend:__ HTML5, Javascript, CSS <br/>
__Backend:__ Python, Flask, PostgreSQL, SQLAlchemy, Jinja<br/>

## <a name="features"></a>Features 📽

Register or login to view all things festivals.  
  
![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/LOGIN%3ACREATE.gif)
<br/><br/><br/>
Search for Festivals by name, location, date, line-up artists. 
  
![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/SEARCH.gif)
<br/><br/><br/>
Make posts on homepage/general feed
  
![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/HOMEPOST.gif)
<br/><br/><br/>
Like/Unlike posts
  
![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/LIKES.gif)
<br/><br/><br/>
Post on individual festival pages 
  
![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/FESTPOST.gif)
<br/><br/><br/>
Attend or Unattend festivals to then display on profile page

![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/ATTEND.gif)
<br/><br/><br/>
User's can update profile photo

![](https://github.com/tatummccormack/wristbands/blob/main/static/readmeimg/PROFILE.gif)




## <a name="installation"></a>Setup/Installation ⌨️

#### Requirements:

- PostgreSQL
- Python 3.9


To have this app running on your local computer, please follow the below steps:

Clone repository:
```
$ git clone https://github.com/tatummccormack/wristbands
```
Create a virtual environment🔮:
```
$ virtualenv env
```
Activate the virtual environment:
```
$ source env/bin/activate
```
Install dependencies🔗:
```
$ pip install -r requirements.txt
```

Create database 'festivals'.
```
$ createdb festivals
```
Create your database tables and seed🌱 example data.
```
$ python model.py
```
Run the app from the command line.
```
$ python server.py
```
If you want to use SQLAlchemy to query the database, run in interactive mode
```
$ python -i model.py
```

## <a name="future"></a>TODO✨
* Add ability for users to plan festival trips with their friends
* Use API's to import festival data 
* Add ability for users to direct message 
* Integrate Google OAuth for easy sign up
* Add safe Buying/Selling ticket feature

## <a name="license"></a>License

The MIT License (MIT)
Copyright (c) 2016 Agne Klimaite 

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.