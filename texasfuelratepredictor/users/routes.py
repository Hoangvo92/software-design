from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from texasfuelratepredictor import db, bcrypt
from texasfuelratepredictor.models import User, ClientInformation
from texasfuelratepredictor.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                           RequestResetForm, ResetPasswordForm)
from texasfuelratepredictor.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.about'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.about'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    client_info = ClientInformation(fullname=form.fullname.data,
            address1=form.address1.data,
            address2=form.address2.data,
            city=form.city.data,
            state=form.state.data,
            zipcode=form.zipcode.data,
            client=current_user.email)
    db.session.add(client_info)
<<<<<<< HEAD
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file) #

    if form.validate_on_submit():
        client_info = ClientInformation.query.filter_by(client=current_user.email).first()#fix the issue of wrong update
=======
    if request.method == 'POST' and form.validate_on_submit():
>>>>>>> c1deffe82bea58814d50e840230a2ccf5f14c4a3
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        client_info.fullname = form.fullname.data
        client_info.address1 = form.address1.data
        client_info.address2 = form.address2.data
        client_info.city = form.city.data
        client_info.state = form.state.data
        client_info.zipcode = form.zipcode.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
<<<<<<< HEAD
       # return redirect(url_for('users.account'))
        return render_template('account.html', title='Account',
            image_file=image_file, form=form, client=client_info)
=======
        return redirect(url_for('users.account'))
>>>>>>> c1deffe82bea58814d50e840230a2ccf5f14c4a3

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.fullname.data = client_info.fullname
        form.address1.data = client_info.address1
        form.address2.data = client_info.address2
        form.city.data = client_info.city
        form.state.data = client_info.state
        form.zipcode.data = client_info.zipcode

    return render_template('account.html', title='Account',
            image_file=image_file, form=form, client=client_info)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password. Please check your email.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Invalid token or token expired', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Password Updated! You are now able to log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
