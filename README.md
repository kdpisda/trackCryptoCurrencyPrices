# Crypto Currency Dashboard
Its made as per the part of Coding Challenge (Advanced) for **Student Developers program by [SV.CO](https://www.sv.co/)**.
As per the description of the Coding Challenge (Advanced) we have to build a cryptocurrency dashboard. I will be including those features as a TO-DO list.

## Technology Stack

- Django (1.11)
- PyJWT
- MaterializeCSS

## Build Locally

Build locally in Ubuntu.

```
$ mkdir cryptoDashboardServer
$ cd cryptoDashboardServer
$ git clone https://github.com/kdpisda/trackCryptoCurrencyPrices.git cryptoDashboard
$ python3 -m venv env
$ source env/bin/activate
$ cd cryptoDashboard
```
Now make a file `.env` and update your credentials for the facebook and github client ID and secret
```
SECRET_KEY=)$8z^+6ys%vd6b2u_r)zf7q(c*g=xd_7x&&$@euxends*i&^=%
DEBUG=True
DB_NAME=cryptoDashboardDB
DB_USER=web
DB_PASSWORD=hA8(scA@!fg3*sc&xaGh&6%-l<._&xCf
DB_HOST=127.0.0.1
GITHUB_CLIENT_ID=******
GITHUB_CLIENT_SECRET=**********
FACEBOOK_CLIENT_ID=**************
FACEBOOK_CLIENT_SECRET=*****************************
```
Then run following commands in terminal
```
$ pip install -r requirements.txt
$ ./manage.py runserver
```

Now open browser and enter `127.0.0.1:8000`.

## To Does
- [ ] Authentication
- [ ] Social media authentication
- [ ] Tracking 3 popular cryptocurrencies
- [ ] Price alert notifications
- [ ] Currency swing notifications
- [ ] Displaying Google Trends information with correlation between Trends data and pricec fluctuations.

## Android App

There is a separate repo for android app. And the contributors are

* [Samveg Thaker](https://github.com/thakersamveg608)
* [Vrihas Pathak](https://github.com/Vrihas123)
