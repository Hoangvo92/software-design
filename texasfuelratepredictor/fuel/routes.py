from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, login_required
from texasfuelratepredictor import db
from texasfuelratepredictor.models import User, ClientInformation, Quote
from texasfuelratepredictor.fuel.forms import FuelForm
import datetime

fuel = Blueprint('fuel', __name__)

#to create a new fuel rate quote
@fuel.route("/fuel_rate_price",  methods=['GET', 'POST'])
@login_required
def fuel_rate_cal():
    form = FuelForm()
    client = ClientInformation.query.filter_by(client=current_user.email).first()
    clientHistory = Quote.query.filter_by(client_em=current_user.email)
    if form.validate_on_submit():
        newFuel = Quote(gallon=form.gallon.data, 
                         address=form.address.data, 
                         datedelivery=form.d_delivery.data, 
                         sugggested_price=form.suggestp.data,
                         total_price =form.totalp.data,
                         client_em=current_user.email)
        db.session.add(newFuel)
        db.session.commit()
        flash('New Fuel Rate Quote in history', 'success')
        return redirect(url_for('main.home'))
    return render_template('fuel_form.html', title='Fuel Quote Form',
                form = form, legend='Fuel Rate Quote', client= client,
                totalp=0, suggestp=0, clientHistory=clientHistory)

#pricing module
@fuel.route("/fuel_rate_price/price",  methods=['GET', 'POST'])
@login_required
def pricing_module():
    form = FuelForm()
    gallon = form.gallon.data # input parameter later from html
    dateform = datetime.date(2019, 9,15) #input parameter later from html
    email = current_user.email
    client = ClientInformation.query.filter_by(client=email).first()
    clientHistory = Quote.query.filter_by(client_em=email)
    timePeriod = datetime.datetime.strptime(dateform,"%Y-%m-%d")
    month = timePeriod.month
    current_p = 1.5
    location_f = 0.02 if client.state=="TX" else 0.04
    history_f = 0 if clientHistory.count()==0 else 0.01
    gallon_f = 0.02 if gallon> 1000 else 0.03
    company_f = 0.1
    fluctuation_f = 0.04 if month>5 and month<9 else 0.03
    margin = current_p*(location_f-history_f+gallon_f+company_f+fluctuation_f)
    suggested_price = current_p + margin
    total_price = gallon * suggested_price
    return render_template('fuel_form.html', title='Fuel Quote Form',
                form = form, legend='Fuel Rate Quote', client= client,
                totalp=total_price, suggestp=suggested_price)

#to check fuel quote history
@fuel.route("/fuel_history",  methods=['GET', 'POST'])
@login_required
def history():
    email = current_user.email
    user = ClientInformation.query.filter_by(client=email).first_or_404()
    page = request.args.get('page', 1, type=int)
    clientHistory = Quote.query.filter_by(client_em=email)\
                 .order_by(Quote.id.desc())\
                 .paginate(per_page=5, page=page)

    return render_template('fuel_history.html', title='Fuel Quote History',
                legend='Fuel Quote History', listQuote= clientHistory, user=user)

#to see a past fuel quote
@fuel.route("/fuel_history/<int:quote_id>",  methods=['GET', 'POST'])
@login_required
def pastQuote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    user = ClientInformation.query.filter_by(client=current_user.email).first_or_404()
    return render_template('past_quote.html', title='Past Fuel Quote', quote=quote, user=user)

  
#delete a past quote
@fuel.route("/fuel_history/<int:quote_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_quote(quote_id):
    quote = Quote.query.get_or_404(quote_id)
    db.session.delete(quote)
    db.session.commit()
    flash('A past quote has been erased!', 'success')
    return redirect(url_for('fuel.history'))
