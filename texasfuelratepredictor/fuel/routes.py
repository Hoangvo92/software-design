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
    count = clientHistory.count()#
    if form.validate_on_submit():
        newFuel = Quote(gallon=form.gallon.data, 
                         address=form.address.data, 
                         datedelivery=form.d_deliver.data, 
                         suggested_price=float(form.suggestp.data), # will try to fix in html later
                         total_price =float(form.totalp.data),      # will try to fix in html later
                         client_em=current_user.email)
        db.session.add(newFuel)
        db.session.commit()
        flash('New Fuel Rate Quote in History', 'success')
        return redirect(url_for('main.home'))
    return render_template('fuel_form.html', title='Fuel Quote Form',
                form = form, legend='Fuel Rate Quote', client= client,
                clientHistory=count)


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
