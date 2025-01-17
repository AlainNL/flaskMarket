from flask import Blueprint, redirect, render_template, url_for
from market.models import User, Item, db
from market.forms import RegisterForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home_page():
    return render_template('home.html')

@main.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@main.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_adresss=form.email_adress.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html', form=form)
