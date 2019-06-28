from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, login_required
from texasfuelratepredictor import db
from texasfuelratepredictor.models import User, ClientInformation, Quote
from texasfuelratepredictor.fuel.forms import FuelForm

fuel = Blueprint('fuel', __name__)

@fuel.route("/fuel_rate_price")
@login_required
def fuel_rate_cal():
    form = FuelForm()
    #client = ClientInformation.query.filter_by(email=current_user.email).first()
    client = ClientInformation.query.filter_by(person_name=current_user.username).first()
    if form.validate_on_submit():
        form.totalp.data = form.gallon.data * form.suggestp.data
        newFuel = Quote(gallon=form.gallon.data, 
                         address=form.address.data, 
                         datedelivery=form.d_delivery.data, 
                         sugggested_price=form.suggestp.data,
                         total_price =form.totalp.data,
                         client_name=current_user.username)
        db.session.add(newFuel)
        db.session.commit()
        flash('New Fuel Rate Quote in history', 'success')
        return redirect(url_for('main.home'))
    return render_template('fuel_form.html', title='Fuel Quote Form',
                form = form, legend='Fuel Rate Quote', client= client)

  
