from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class FuelForm(FlaskForm):
      gallon = IntegerField('# of Gallons', validators=[DataRequired()])
      address = StringField('Address')
      d_deliver = DateField('Date Delivery', validators=[DataRequired()])
      suggestp = DecimalField('Suggested Price')
      totalp = DecimalField('Total Price')
      submit = SubmitField('Calculate Fuel Rate')


