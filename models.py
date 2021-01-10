import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Dealership(db.Model):
    __tablename__ = 'dealerships'

    dtid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    store_num = db.Column(db.Text, nullable=False)
    ent_code = db.Column(db.Text, nullable=False)
    d_name = db.Column(db.Text, nullable=False)
    d_address = db.Column(db.Text, nullable=False)
    d_phone = db.Column(db.Text, nullable=False)
    services = db.Column(db.ARRAY(db.Text), nullable=False)
    departments = db.Column(db.ARRAY(db.Text), nullable=False)
    employees = db.Column(db.ARRAY(db.Text), nullable=False)

class Project(db.Model):
    __tablename__ = "projects"

    projectid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.Text, nullable=False)
    dealership = db.Column(db.Integer, db.ForeignKey('dealerships.dtid'))
    installers = db.Column(db.ARRAY(db.Integer), nullable=False)
    project_date = db.Column(db.DateTime, default=datetime.date.today())
    dealer = db.relationship('Dealership')

class Department(db.Model):
    __tablename__ = "departments"

    departmentid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    department = db.Column(db.Text, nullable = False)

class Employee(db.Model):
    __tablename__ = 'employees'

    eid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    e_firstname = db.Column(db.Text, nullable = False)
    e_lastname = db.Column(db.Text, nullable = False)
    e_department = db.Column(db.Integer, db.ForeignKey("departments.departmentid"))
    e_title = db.Column(db.Text, nullable = False)
    phone = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False)
    dept = db.relationship('Department')

class Installer(db.Model):
    __tablename__ = 'installers'

    installerid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    current_dealership = db.Column(db.Integer, db.ForeignKey("dealerships.dtid"))
    i_firstname = db.Column(db.Text, nullable = False)
    i_lastname = db.Column(db.Text, nullable = False)
    i_department = db.Column(db.Integer, db.ForeignKey("departments.departmentid"))
    i_title = db.Column(db.Text, nullable = False)
    phone = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False)
    dept = db.relationship('Department')
    dealer = db.relationship('Dealership')

class Task(db.Model):
    __tablename__ = 'tasks'

    taskid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    t_description = db.Column(db.Text, nullable = False)
    t_department = db.Column(db.Integer, db.ForeignKey("departments.departmentid"))
    t_status = db.Column(db.Boolean)
    dept = db.relationship('Department')
