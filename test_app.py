from app import app
from flask import session
from unittest import TestCase

app.config['TESTING'] = True
app.config['SQLALCHEMY_ECHO'] = True

class OnboardingTest(TestCase):
    """ Testing for the Onboarding Process"""
    def test_show_homepage(self):
        client = app.test_client()
        res = client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_login(self):
        client = app.test_client()
        res = client.get("/login")
        self.assertEqual(res.status_code, 200)

    def test_register(self):
        client = app.test_client()
        res = client.get("/register")
        self.assertEqual(res.status_code, 200)

    def test_register(self):
        with app.test_client() as client:
            res = client.post('/register', data = {'current_dealership': 1,
            'i_firstname':'Breeana', 'i_lastname':'Payton', 'i_department': 2,
            'i_title':'Implementation Specialist', 'phone':'848-761-1543', 'email':'breeana.payton@gmail.com', 
            'username':'BPayton3', 'i_password':'happy_birthday'})
            html = res.get_data(as_text = True)
            # print(res.data)
            self.assertEqual(res.status_code, 302)

    