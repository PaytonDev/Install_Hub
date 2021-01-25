from flask import Flask, render_template, redirect, request, flash, jsonify, g, session
from forms import LoginForm, RegisterForm
from models import db, connect_db, Dealership, Project, Employee, Task, Department, User
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
# from flask_cors import CORS

USER_KEY = 'curr_user'
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///install'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "super-extra-secretive"

connect_db(app)

@app.before_request
def add_to_global():
    """ If user is logged in then add them to Flask globally"""

    if USER_KEY in session:
        g.user = User.query.get(session[USER_KEY])
    else:
        g.user = None

def login_user(user):
    """ Log in user """
    session[USER_KEY] = user.userid

def logout_user():
    """Logout user"""
    if USER_KEY in session:
        del session[USER_KEY]


@app.route('/')
def show_homepage():
    return render_template("homepage.html")


@app.route("/login", methods=["GET", 'POST'])
def login():
    """handle login validation"""
    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            login_user(user)
            flash(f'Welcome, {user.full_name()}!', "success")
            return redirect(f'/user/{user.userid}/detail')

        flash("Invalid login.", "danger")

    return render_template('login.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Adding new user to the database"""
    form = RegisterForm()

    if form.validate_on_submit():
        # try:
        user = User.signup(
            username = form.username.data,
            i_password = form.password.data,
            i_firstname = form.first_name.data,
            i_lastname = form.last_name.data,
            i_title = form.title.data,
            phone = form.phone_num.data,
            email = form.email.data,
            i_department = form.department.data,
            current_dealership = form.current_dealership.data
        )
        db.session.commit()

        # except IntegrityError:
        #     flash("Username is taken", "danger")
        #     return render_template('register.html', form=form)

        login_user(user)
        return redirect(f"/user/{user.userid}/detail")

    else:
        flash('OOOPS!')
        return render_template("register.html", form=form)

@app.route('/user/<int:userid>/detail', methods=['GET', 'POST'])
def show_install_detail(userid):
    """Loading data about the install to show on the page"""

    user = User.query.get_or_404(userid)
    dealer = Dealership.query.get_or_404(user.current_dealership)


    return render_template('user/install-detail.html', user=user, dealer=dealer)