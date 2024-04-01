**Configure your environment**

- $ python -m venv
- $ venv\Scripts\activate - windows
- $ source venv/bin/activate - macos/linux
- $ pip install -r requirements.txt`
- $ python manage.py runserver

**For environment variables**
_Reservamos_

you need your own BASE_URL_RESERVAMOS

_OPEN WEATHER_

you need your own API_KEY and BASE_URL_OPEN_WEATHER

**For run application**

- python manage.py runserver

It will run on http://127.0.0.1:8000/

**Endpoints:**

http://127.0.0.1:8000/weather?cityname=
_example:_
http://127.0.0.1:8000/weather?cityname=mexico

**even you can check the application in this link:**

https://reservamos-1.onrender.com/weather/?cityname=
_example:_

https://reservamos-1.onrender.com/weather/?cityname=culiacan
