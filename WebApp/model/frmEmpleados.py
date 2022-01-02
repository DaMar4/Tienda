from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class FrmEmpleados(FlaskForm):
    nombre_empleado = StringField("Nombre del empleado:",validators=[DataRequired()])
    area = StringField("Area:",validators=[DataRequired()])