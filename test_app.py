from app import app
from flask import session
from unittest import TestCase
import random
import string


app.config['TESTING'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['WTF_CSRF_ENABLED'] = False

def random_string():
    letters = string.ascii_letters
    return (''.join(random.choice(letters) for i in range(10)))

class RouteTest(TestCase):
    """Testing Routes"""
    def new_user(self):
        client = app.test_client()
        res = client.post("/login", data = {"username" : "testuser", "password" : "testuser"})
        html = res.get_data(as_text = True)
        print(html)

    def test_login_page(self):
        client = app.test_client()
        res = client.get("/login")
        self.assertEqual(res.status_code, 200)

    def test_show_homepage(self):
        client = app.test_client()
        res = client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_register_page(self):
        client = app.test_client()
        res = client.get("/register")
        self.assertEqual(res.status_code, 200)

class OnboardingTest(TestCase):
    """ Testing for the Onboarding Process"""
    def test_register_installer(self):
        with app.test_client() as client:
            res = client.post('/register', data = {'current_dealership': '1',
            'first_name':'Breeana', 'last_name':'Payton', 'department': '2',
            'title':'Implementation Specialist', 'phone_num':'848-761-1543', 'email':'breeana.payton@gmail.com', 
            'username': random_string(), 'password':'happybirthday'})
            html = res.get_data(as_text = True)
            self.assertEqual(res.status_code, 302)


        


    