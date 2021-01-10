from flask import Flask, render_template, redirect, request, flash, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Dealership, Project, Employee, Task, Department, Installer
# from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///install'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "super-extra-secretive"

connect_db(app)