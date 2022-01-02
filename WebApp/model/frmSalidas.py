from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmSalidas(FlaskForm):
    empleado_que_recibe = SelectField("Empleado que recibe:", coerce = str)
    descripcion = SelectField("Descripción:",validators=[DataRequired()])
    observacion = SelectField("Observación:", choices=[('Ninguno', 'Ninguno'), ('Devolucion', 'Devolución por daño')],validators=[DataRequired()])
    cantidad = StringField("Cantidad:",validators=[DataRequired()])
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')