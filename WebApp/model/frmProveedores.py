from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired
class FrmProveedores(FlaskForm):
    proveedor = StringField("Agregar proveedor:",validators=[DataRequired()])