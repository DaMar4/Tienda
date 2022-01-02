from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmEditSalida(FlaskForm):
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')