# Test project with Django&Stripe

For launch you need as follow:
```
git clone https://github.com/Act0r1/test-stripe && cd test-stripe
python3 -m venv venv && source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver
```
But before this you need set public and secret key in ```test_site/settings.py```, these key you can find here - https://dashboard.stripe.com/test/apikeys

In browser open http://127.0.0.1:8000/item/{id}, this ```id``` - any int.
