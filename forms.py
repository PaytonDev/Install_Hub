from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    """Form for installers to Login"""

    username = StringField("Username", validators=[DataRequired(message="Username required. Please enter username.")])
    password = PasswordField("Password", validators = [DataRequired(message="Password required. Please enter password.")])

class RegisterForm(FlaskForm):
    """Form for adding new installers"""

    username = StringField("Username", validators=[DataRequired(message="Username required. Please enter username.")])
    password = PasswordField("Password", validators = [DataRequired(message="Password required. Please enter password.")])
    first_name = StringField("First Name", validators=[DataRequired(message="First name required. Please enter first name.")])
    last_name = StringField("Last Name", validators=[DataRequired(message="Last name required. Please enter last name.")])
    phone_num = StringField("Phone Number", validators=[DataRequired(message="Phone number required. Please enter phone number.")])
    email = StringField("Email", validators=[DataRequired(message="Email required. Please enter email.")])
    title = SelectField("Job Title", validators=[DataRequired(message="Please select job title.")], choices=[('', 'Job Title'), ('Implementation Specialist', 'IS'), ('Sr. Implementation Specialist', 'SIS'), ('Implementation Manager', 'IM')])
    department = SelectField('Department', validators=[DataRequired(message="Please select department")], choices=[('', 'Department'), (1, "Accounting"), (2, "Business Office"), (3, "Parts"), (4, "Service")])
    current_dealership = IntegerField('DTID', validators=[DataRequired(message="Please enter DTID")])