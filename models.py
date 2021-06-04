import datetime
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import codecs

codecs.register_error("strict", codecs.ignore_errors)

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
    d_city = db.Column(db.Text, nullable=False)
    d_phone = db.Column(db.Text, nullable=False)
    services = db.Column(db.ARRAY(db.Text), nullable=False)
    departments = db.Column(db.ARRAY(db.Text), nullable=False)
    employees = db.Column(db.ARRAY(db.Text), nullable=False)

class Project(db.Model):
    __tablename__ = "projects"

    projectid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    title = db.Column(db.Text, nullable=False)
    dealership = db.Column(db.Integer, db.ForeignKey('dealerships.dtid'))
    user = db.Column(db.ARRAY(db.Integer), nullable=False)
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

class User(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    current_dealership = db.Column(db.Integer, db.ForeignKey("dealerships.dtid"))
    i_firstname = db.Column(db.Text, nullable = False)
    i_lastname = db.Column(db.Text, nullable = False)
    i_department = db.Column(db.Integer, db.ForeignKey("departments.departmentid"))
    i_title = db.Column(db.Text, nullable = False)
    phone = db.Column(db.Text, nullable = False)
    email = db.Column(db.Text, nullable = False)
    username = db.Column(db.Text, nullable = False, unique=True)
    i_password = db.Column(db.Text, nullable = False, unique=True)
    dept = db.relationship('Department')
    dealer = db.relationship('Dealership')

    @classmethod
    def signup(cls, username, i_password, current_dealership, i_firstname,
    i_lastname, i_department, i_title, phone, email):

        encoded_pass = i_password.encode(encoding='utf-8', errors='ignore')
        hashed_pwd = bcrypt.hashpw(encoded_pass, bcrypt.gensalt())

        user = User(
            username = username,
            i_password = hashed_pwd,
            current_dealership = current_dealership,
            i_firstname = i_firstname, 
            i_lastname = i_lastname,
            i_department = i_department,
            i_title = i_title,
            phone = phone, 
            email = email
        )
        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, i_password):
        user = cls.query.filter_by(username=username).first()

        encodedpw = i_password.encode(encoding="utf-8", errors='ignore')

        if user:
            is_auth = bcrypt.checkpw(encodedpw, user.i_password)
            if is_auth:
                return user


class Task(db.Model):
    __tablename__ = 'tasks'

    taskid = db.Column(db.Integer, autoincrement = True, primary_key = True)
    t_description = db.Column(db.Text, nullable = False)
    t_department = db.Column(db.Integer, db.ForeignKey("departments.departmentid"))
    t_status = db.Column(db.Boolean)
    dept = db.relationship('Department')
