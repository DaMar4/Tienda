from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmIngresos(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    proveedor = StringField("Proveedor:",validators=[DataRequired()])
    descripcion = SelectField("Descripción:",validators=[DataRequired()],coerce=str)
    unidad = SelectField("Unidad:",validators=[DataRequired()],coerce=str)
    categoria = SelectField("Categoría:",validators=[DataRequired()],coerce=str)
    cantidad = StringField("Cantidad:",validators=[DataRequired()])