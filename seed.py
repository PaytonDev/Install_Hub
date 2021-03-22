from models import Department, Employee, User, Task, Dealership, Project, db
from app import app
import random
import string

db.drop_all()
db.create_all()

d1 = Department(department="Accounting")
d2 = Department(department="Business Office")
d3 = Department(department="Parts")
d4 = Department(department="Service")

e1 = Employee(e_firstname="Jennifer", e_lastname="Finch", e_department=1, e_title="Controller", phone="555-555-5555", email="jen.finch@janeford.com")
e2 = Employee(e_firstname="Thadeus", e_lastname="Gathercoal", e_department=2, e_title="Sales Manager", phone="777-777-77777", email="thad.gathercoal@janeford.com'")
e3 = Employee(e_firstname="Sonja", e_lastname="Pauley", e_department=3, e_title="Parts Manager", phone="888-888-8888", email="sonja.pauley@janeford.com")
e4 = Employee(e_firstname="Waneta", e_lastname="Skeleton", e_department=4, e_title="Service Manager", phone="999-999-9999", email="waneta.skeleton@janeford.com")
e5 = Employee(e_firstname="Cohen", e_lastname="Norton", e_department=1, e_title="Controller", phone="963-852-8527", email="cohen.norton@johnnissan.com")
e6 = Employee(e_firstname="Loretta", e_lastname="Elwyn", e_department=2, e_title="", phone="", email="")
e7 = Employee(e_firstname="", e_lastname="", e_department=3, e_title="", phone="", email="")
e8 = Employee(e_firstname="", e_lastname="", e_department=4, e_title="", phone="", email="")